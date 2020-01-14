"""Gets log from Sauce Labs"""
import requests


URL_BASE = "{api_endpoint}/{username}/jobs/{job_id}/assets/log.json"


class AssetsNotFound(Exception):
    """Asset(s) for a job were not present or the job does not exist"""
    pass


class SomethingWentWrong(Exception):
    """A non 200 HTTP status was returned.  Something bad may have happened"""
    pass


def get_log(api_endpoint, admin, access_key, username, job_id, write=False):
    "Obtain log with username and job_id"

    url = URL_BASE.format(api_endpoint=api_endpoint, username=username,
                          job_id=job_id)
    log_name = "log_{}.log".format(job_id)
    resp = requests.get(url, auth=(username, access_key))

    if write:
        with open(log_name, 'w') as log:
            log.write(resp.text)
    if resp.status_code == 404:
        raise AssetsNotFound
    if resp.status_code != 200:
        raise SomethingWentWrong
    return resp.text
