"""Gets log from Sauce Labs"""

import base64
import requests


URL_BASE = "{api_endpoint}/{username}/jobs/{job_id}/assets/log.json"


def get_log(api_endpoint, admin, access_key, username, job_id, write=False):
    "Obtain log with username and job_id"

    url = URL_BASE.format(api_endpoint=api_endpoint, username=username,
                          job_id=job_id)
    log_name = "log_{}.log".format(job_id)
    resp = requests.get(url, auth=(username, access_key))

    if write:
        with open(log_name, 'w') as log:
            log.write(resp.text)
    return resp.text
