"""Created objects needed for Sauce logs"""

import json
import log_collector

class Job(object):
    """docstring for Job."""

    duration = {}
    between_commands = {}
    data = None

    def __init__(self, job_id):
        super(Job, self).__init__()
        self.job_id = job_id

    def get_duration(self):
        """Returns the duration dict"""
        return self.duration

    def get_between_commands(self):
        """Returns the duration dict"""
        return self.between_commands

    def fetch_log(self, admin, access_key, username, write):
        """Downloads log"""
        response = log_collector.get_log(admin, access_key, username, self.job_id, write)
        self.data = json.loads(response)

    def read_data(self, command):
        """Reads data and returns max, min, mean and total"""
        commands = []
        results = {}
        for log in self.data:
            curr_command = log[command]
            if curr_command != None:
                commands.append(curr_command)
        if len(commands) > 0:  # Check if there's actual commands to process

            results["mean"] = Job.mean(commands)
            results["max"] = max(commands)
            results["min"] = min(commands)
            results["total"] = Job.total(commands)

        return results

    @staticmethod
    def print_results(results):
        "Prints results dict with the desired calculations"
        if len(results) > 0:

            print("  mean is {}".format(results["mean"]))
            print("  max is {}".format(results["max"]))
            print("  min is {}".format(results["min"]))
            print("  total is {}".format(results["total"]))
        else:
            print("There is no commands to be parsed")

    def examine_job(self):
        """Gets information from data"""

        duration = self.read_data("duration")
        between_commands = self.read_data("between_commands")

        print("test id: {}".format(self.job_id))
        print("Duration:")
        Job.print_results(duration)
        print("between_commands:")
        Job.print_results(between_commands)
        print("")

    @staticmethod
    def mean(num_list):
        """Calculates mean of a list"""
        i = 0
        num_sum = 0.0
        for item in num_list:
            num_sum += item
            i += 1

        return num_sum/i

    @staticmethod
    def total(num_list):
        """Calculates total of a list"""
        num_sum = 0.0
        for item in num_list:
            num_sum += item
        return num_sum
