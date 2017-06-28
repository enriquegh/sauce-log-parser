"""Gets log from Sauce Labs"""

import base64
import httplib2


URL_BASE = "https://saucelabs.com/rest/v1/{username}/jobs/{job_id}/assets/log.json"


def get_log(admin, access_key, username, job_id):
    "Obtain log with username and job_id"

    url = URL_BASE.format(username=username, job_id=job_id)
    print url
    log_name = "log_{}.log".format(job_id)
    http_conn = httplib2.Http()
    # http_conn.add_credentials(admin, access_key)
    user_pass = base64.b64encode("{}:{}".format(admin, access_key))
    headers = {'Authorization' : 'Basic {}'.format(user_pass)}
    _, response = http_conn.request(url, method="GET", headers=headers)


    with open(log_name, 'w') as log:
        log.write(response)
    print response
