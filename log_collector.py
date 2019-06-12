"""Gets log from Sauce Labs"""

import base64
import httplib2


URL_BASE = "{api_endpoint}/{username}/jobs/{job_id}/assets/log.json"


def get_log(api_endpoint, admin, access_key, username, job_id, write=False):
    "Obtain log with username and job_id"

    url = URL_BASE.format(api_endpoint=api_endpoint, username=username, job_id=job_id)
    log_name = "log_{}.log".format(job_id)
    http_conn = httplib2.Http()
    # http_conn.add_credentials(admin, access_key)
    user_pass = base64.b64encode('{}:{}'.format(admin, access_key).encode('ascii'))
    headers = {'Authorization': 'Basic {}'.format(user_pass.decode('ascii'))}
    _, response = http_conn.request(url, method="GET", headers=headers)

    if write:
        with open(log_name, 'w') as log:
            log.write(response.decode('ascii'))
    return response
