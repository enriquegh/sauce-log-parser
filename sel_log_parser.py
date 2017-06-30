"""Parse Sauce Labs log messages and analyze commands"""
from __future__ import print_function
import json
import re
import os
import os.path
import argparse
from log_collector import get_log
import glob


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
    file = glob.glob('log_{}.*'.format(job_id))
    log_name = file[0]
    # TODO: Move to main()
    # if not os.path.exists(log_name):
    #     get_log("ADMIN", "ACCESS_KEY", "USERNAME", job_id)
    print("test id: {}".format(job_id))
    print("Duration:")
    read_log(log_name, "duration")
    print("between_commands:")
    read_log(log_name, "between_commands")
    print("")

def is_log_downloaded(job_id):
    file = glob.glob('log_{}.*'.format(job_id))
    if file:
        return True
    return False

def main():
    """Main function"""
    # For now, format MUST be in the order log_JOB_ID.something
    # if len(sys.argv) <= 1:
    #     print("Please enter files to examine")
    # else:
    #     for i in range(1, len(sys.argv)):
    #         examine_job(sys.argv[i])

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-a", "--admin", help="Sauce admin username")
    arg_parser.add_argument("-u", "--user", help="Sauce username")
    arg_parser.add_argument("-k", "--access_key", help="Sauce access key")
    arg_parser.add_argument("job_id", nargs="+", help="Job id to be examined")

    args = arg_parser.parse_args()


    if not args.user:
        args.user = os.environ.get('SAUCE_USERNAME')
    if not args.access_key:
        args.access_key = os.environ.get('SAUCE_ACCESS_KEY')

    for job in args.job_id:
        print(job)
        if is_log_downloaded(job):
            examine_job(job)
        else:
            #NEED TO HAVE ADMIN USER AND ACCESS_KEY
            if args.user and args.access_key and args.admin:
                print("We can't download logs just yet. :/")
            else:
                print("Can't download log without credentials")


    #TODO: use argparse to create a ArgumentParser


if __name__ == '__main__':
    main()
