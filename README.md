# Sauce Log Parser 
[![Build Status](https://travis-ci.org/enriquegh/sauce-log-parser.svg?branch=master)](https://travis-ci.org/enriquegh/sauce-log-parser)

Small python script that analyzes the log.json file provided by a Sauce Labs test.

It gets the time commands took to run and the time in between Sauce Labs sent a response and received another request.

With those two metrics it gets the average, min, max and total of them.

This can help determine if a "slow" test is because of Selenium commands/server issue or if there is latency in the connection

```
python sel_log_parser.py -h
usage: sel_log_parser.py [-h] [-a ADMIN] [-k ACCESS_KEY] [-u USER] [-s]
                         job_id [job_id ...]

positional arguments:
  job_id                Sauce Labs Session ID to be examined.

optional arguments:
  -h, --help            show this help message and exit
  -a ADMIN, --admin ADMIN
                        Sauce Admin username. For Saucers only.
  -k ACCESS_KEY, --access_key ACCESS_KEY
                        Sauce Admin access key. For Saucers only.
  -u USER, --user USER  Sauce username. Account Username of the Test Owner
                        that ran the session.
  -s, --save            Save the output as a .log file in the cwd. Schema is
                        log_session-id.log.
  -r REGION, --region REGION
                        Sauce region where test was performed(us-west-1, us-
                        east-1)
```

## Usage
Run against one session!

`python sel_log_parser.py -a $SAUCE_USERNAME -k $SAUCE_ACCESS_KEY -u some-username some-session-id`

Run against multiple sessions!

`python sel_log_parser.py -a $SAUCE_USERNAME -k $SAUCE_ACCESS_KEY -u some-username some-session-id another-session-id third-session-id ... Nth-session`

Output:

```
---
test_id: your-session-id
duration:
  mean: 0.33958974618178145
  max: 480.00422978401184
  min: 0.0022919178009033203
  total: 551.8333375453949
between_commands:
  mean: 0.1021887963922153
  max: 180.5098659992218
  min: -477.2646918296814
  total: 165.95460534095764
```

## Setup
Manual Setup via git master branch:
1. `cd` to a directory where you want the python tools/files.
1. `git clone git@github.com:enriquegh/sauce-log-parser.git`
1. `cd sauce-log-parser` and start looking at times!


## Contributing and Testing
Fork the remote master branch and make pull requests.  Open issues if something is wrong and copy-paste your input & output.

Launch tests with `py.test`.  Pytest is used and the `/tests` directory should get you started on seeing what is covered and what tests should look like.