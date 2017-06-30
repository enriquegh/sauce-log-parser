"""Parse Sauce Labs log messages and analyze commands"""
from __future__ import print_function
import json
import sys
import re
import os
import os.path
from log_collector import get_log


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

def examine_job(log_name):
    """Parses job id from log name"""
    search_query = re.search(r'_(.+?)\.', log_name)
    if search_query:
        job_id = search_query.group(1)
    else:
        exit("Log name is not in the order log_JOB_ID.something")

    if not os.path.exists(log_name):
        get_log("ADMIN", "ACCESS_KEY", "USERNAME", job_id)
    print("test id: {}".format(job_id))
    print("Duration:")
    read_log(log_name, "duration")
    print("between_commands:")
    read_log(log_name, "between_commands")
    print("")

def main():
    """Main function"""
    # For now, format MUST be in the order log_JOB_ID.something
    if len(sys.argv) <= 1:
        print("Please enter files to examine")
    else:
        for i in range(1, len(sys.argv)):
            examine_job(sys.argv[i])


    #TODO: use argparse to create a ArgumentParser


if __name__ == '__main__':
    main()
