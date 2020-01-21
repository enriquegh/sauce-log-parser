"""Parse Sauce Labs log messages and analyze commands"""
from __future__ import print_function
import json
import os
import os.path
import argparse
import glob
import sauce_job
import logging
import csv
import datetime

import utils
import constants


def read_log(log_name, command):
    """Reads in a log and returns a list of all the command values"""
    commands = []
    with open(log_name, 'r') as log:
        data = json.load(log)

    for log in data:

        # If "status" is present, a javascript title was sent
        if "status" in log:
            pass
        else:
            curr_command = log[command]
            if curr_command is not None:
                commands.append(curr_command)
    if commands:  # Check if there's actual commands to process
        print("  mean: {}".format(utils.mean(commands)))
        print("  max: {}".format(max(commands)))
        print("  min: {}".format(min(commands)))
        print("  total: {}".format(utils.total(commands)))
    else:
        print("There is no commands to be parsed")


def examine_job(job_id):
    """Parses job id from log name"""
    files = glob.glob('log_{}.*'.format(job_id))
    log_name = files[0]

    print("testId: {}".format(job_id))
    print("duration:")
    read_log(log_name, "duration")
    print("between_commands:")
    read_log(log_name, "between_commands")
    print("")


def is_log_downloaded(job_id):
    """Checks if log exists in folder"""
    files = glob.glob('log_{}.*'.format(job_id))
    if files:
        return True
    return False


# build the job(s) objects for the Job IDs user supplied
def build_job(job,
              api_endpoint,
              args):
    job_instance = sauce_job.Job(job)
    job_instance.fetch_log(api_endpoint,
                           args.admin,
                           args.access_key,
                           args.user,
                           args.save)
    return job_instance


def main(arguments=None):
    """Main function"""

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-a", "--admin",
                            help="Sauce Admin username.  For Saucers only.")
    arg_parser.add_argument("-k", "--access_key",
                            help="Sauce Admin access key.  For Saucers only.")
    arg_parser.add_argument("-u", "--user",
                            help="Sauce username.  Account Username of the"
                            " Test Owner that ran the session.")
    arg_parser.add_argument("-s", "--save",
                            help="Save the output as a .log file in cwd. "
                            "Schema is log_session-id.log.",
                            action="store_true")
    arg_parser.add_argument("-r", "--region",
                            help="Sauce region where test was performed"
                            "(us-west-1, us-east-1, eu-central-1)")
    arg_parser.add_argument("-v", "--verbose",
                            help="Verbose flag to print at debug level",
                            action="store_true")
    arg_parser.add_argument("--csv",
                            help="Save the output of all tests as csv in cwd. "
                            "Schema is date_job-ids.csv",
                            action="store_true")
    arg_parser.add_argument("job_id", nargs="+",
                            help="Sauce Labs Session ID to be examined.")

    args = arg_parser.parse_args(arguments)

    if not args.user:
        args.user = os.environ.get('SAUCE_USERNAME')
    if not args.access_key:
        args.access_key = os.environ.get('SAUCE_ACCESS_KEY')
    if not args.region:
        args.region = 'us-west-1'

    api_endpoint = constants.API_ENDPOINT[args.region]

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    job_instances = [build_job(job, api_endpoint=api_endpoint, args=args)
                     for job in args.job_id]
    csv_raw_data = []
    for job in job_instances:
        job.examine_job()

        if args.csv:
            duration = utils.rename_command_dict("duration",
                                                 job.get_duration())
            between_commands = utils.rename_command_dict("between_commands", job.get_between_commands())  # noqa: E501

            all_commands = {"job_id": job.job_id,
                            **between_commands, **duration}
            csv_raw_data.append(all_commands)

    if args.csv:
        date = datetime.datetime.now().strftime('%Y%m%d-%X')
        filename = "{}-job-ids.csv".format(date)
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['job_id', 'between_commands_mean',
                          'between_commands_max', 'between_commands_min',
                          'between_commands_total', 'duration_mean',
                          'duration_max', 'duration_min', 'duration_total']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(csv_raw_data)
            print("CSV {} created.".format(filename))


if __name__ == '__main__':
    main()
