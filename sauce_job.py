"""Created objects needed for Sauce logs"""

import log_collector
import sel_log_parser as sel
import json

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

    def fetch_log(self, admin, access_key, username):
        response = log_collector.get_log(admin, access_key, username, self.job_id, write=False)
        if response is not None:
            self.data = json.loads(response)

    def read_log(self, command):
        """Reads in a log and returns a list of all the command values"""
        commands = []
        results = {}

        for log in self.data:
            curr_command = log[command]
            if curr_command != None:
                commands.append(curr_command)

        results["mean"] = sel.mean(commands)
        results["max"] = max(commands)
        results["min"] = max(commands)
        results["total"] = sel.total(commands)

        return results
