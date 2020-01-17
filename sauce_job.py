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

    def fetch_log(self, api_endpoint, admin, access_key, username, write):
        """Downloads log"""
        try:
            response = log_collector.get_log(api_endpoint, admin, access_key,
                                             username, self.job_id, write)
        except log_collector.AssetsNotFound:
            print("404 API response.  The assets for %s are no longer available\
(> 30 days since test creation) or do not exist." % self.job_id)
            return
        except log_collector.SomethingWentWrong:
            print("Something went wrong. Try running with '-v'")
            return
        if response:
            self.data = json.loads(response)

    def read_data(self, command):
        """Reads data and returns max, min, mean and total"""
        commands = []
        results = {}
        if self.data is None:
            results["mean"] = "n/a"
            results["max"] = "n/a"
            results["min"] = "n/a"
            results["total"] = "n/a"
            return results

        for log in self.data:
            # If "status" is present, a javascript title was sent
            if "status" in log:
                pass
            else:
                curr_command = log[command]
                if curr_command is not None:
                    commands.append(curr_command)
        if commands:  # Check if there's actual commands to process
            results["mean"] = Job.mean(commands)
            results["max"] = max(commands)
            results["min"] = min(commands)
            results["total"] = Job.total(commands)

        return results

    @staticmethod
    def print_results(results):
        "Prints results dict with the desired calculations"
        if results:
            print("  mean: {}".format(results["mean"]))
            print("  max: {}".format(results["max"]))
            print("  min: {}".format(results["min"]))
            print("  total: {}".format(results["total"]))
        else:
            print("There is no commands to be parsed")

    def examine_job(self):
        """Gets information from data"""
        if self.data is None:
            print("Could not download job id", self.job_id)
            return
        self.duration = self.read_data("duration")
        self.between_commands = self.read_data("between_commands")

        print("---")
        print("test_id: {}".format(self.job_id))
        print("duration:")
        Job.print_results(self.duration)
        print("between_commands:")
        Job.print_results(self.between_commands)
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
