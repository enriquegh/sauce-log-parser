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

        for log in self.data:
            curr_command = log[command]
            if curr_command != None:
                commands.append(curr_command)

        print "  mean is {}".format(sel.mean(commands))
        print "  max is {}".format(max(commands))
        print "  min is {}".format(min(commands))
        print "  total is {}".format(sel.total(commands))
