"""Parse Sauce Labs log messages and analyze commands"""
from __future__ import print_function
import json
import os
import os.path
import argparse
import glob
import sauce_job


def mean(num_list):
    """Calculates mean of a list"""
    i = 0
    num_sum = 0.0
    for item in num_list:
        num_sum += item
        i += 1

    return num_sum/i

def total(num_list):
    """Calculates total of a list"""
    num_sum = 0.0
    for item in num_list:
        num_sum += item
    return num_sum

def read_log(log_name, command):
    """Reads in a log and returns a list of all the command values"""
    commands = []
    with open(log_name, 'r') as log:
        data = json.load(log)

    for log in data:
    #   curr_command = log["between_commands"]
        curr_command = log[command]
        if curr_command != None:
            commands.append(curr_command)

    print("  mean is {}".format(mean(commands)))
    print("  max is {}".format(max(commands)))
    print("  min is {}".format(min(commands)))
    print("  total is {}".format(total(commands)))

def examine_job(job_id):
    """Parses job id from log name"""
    files = glob.glob('log_{}.*'.format(job_id))
    log_name = files[0]

    print("test id: {}".format(job_id))
    print("Duration:")
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

def main():
    """Main function"""

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-a", "--admin", help="Sauce admin username")
    arg_parser.add_argument("-k", "--access_key", help="Sauce admin access key")
    arg_parser.add_argument("-u", "--user", help="Sauce username")
    arg_parser.add_argument("job_id", nargs="+", help="Job id to be examined")

    args = arg_parser.parse_args()


    if not args.user:
        args.user = os.environ.get('SAUCE_USERNAME')
    if not args.access_key:
        args.access_key = os.environ.get('SAUCE_ACCESS_KEY')

    for job in args.job_id:
        if is_log_downloaded(job):
            pass
        else:
            #NEED TO HAVE ADMIN USER AND ACCESS_KEY
            # Will create a Job instance

            if args.user and args.access_key and args.admin:
                job_instance = sauce_job.Job(job)
                job_instance.fetch_log(args.admin, args.access_key, args.user, True)

            else:
                print("Can't download job id {} without credentials. Please try again".format(job))
                continue
        examine_job(job)


if __name__ == '__main__':
    main()
