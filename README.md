# Sauce Log Parser
[![Build Status](https://travis-ci.org/enriquegh/sauce-log-parser.svg?branch=master)](https://travis-ci.org/enriquegh/sauce-log-parser)

Small python script that analyzes the log.json file provided by a Sauce Labs test.

It gets the time commands took to run and the time in between Sauce Labs sent a response and received another request.
With those two metrics it gets the average, min, max and total of them.

This can help determine if a "slow" test is because of Selenium commands/server issue or if there is latency in the connection

**NOTE: There is a discrepancy between the total time posted on the Sauce Labs test details page and the total time of between_commands and duration.**

This is because the log.json file (which is used by this script) only takes into account test time but does not take into account start up and processing time.

```
python sel_log_parser.py -h
usage: sel_log_parser.py [-h] [-a ADMIN] [-k ACCESS_KEY] [-u USER] [-s]
                         [-r REGION] [-v] [--csv]
                         jobid [jobid ...]

positional arguments:
  jobid                Sauce Labs Session ID to be examined.

optional arguments:
  -h, --help            show this help message and exit
  -a ADMIN, --admin ADMIN
                        Sauce Admin username. For Saucers only.
  -k ACCESS_KEY, --access_key ACCESS_KEY
                        Sauce Admin access key. For Saucers only.
  -u USER, --user USER  Sauce username. Account Username of the Test Owner
                        that ran the session.
  -s, --save            Save the output as a .log file in cwd. Schema is
                        log_session-id.log.
  -r REGION, --region REGION
                        Sauce region where test was performed(us-west-1, us-
                        east-1, eu-central-1)
  -v, --verbose         Verbose flag to print at debug level
  --csv                 Save the output of all tests as csv in cwd. Schema is
                        date_job-ids.csv
```

## Usage
Run against one session!

`python sel_log_parser.py -a $SAUCE_USERNAME -k $SAUCE_ACCESS_KEY -u some-username --some-session-id`
It would look like this:
`python sel_log_parser.py -a $SAUCE_USERNAME -k $SAUCE_ACCESS_KEY -u awesome.userName --jobid 6e709ff746664fy896b467675b886e40`
or if you are using Python3
`python3 sel_log_parser.py -a $SAUCE_USERNAME -k $SAUCE_ACCESS_KEY -u awesome.userName --jobid 6e709ff746664fy896b467675b886e40`

Run against multiple sessions!

`python sel_log_parser.py -a $SAUCE_USERNAME -k $SAUCE_ACCESS_KEY -u some-username some-session-id another-session-id third-session-id ... Nth-session`

**NOTE: You only need to provide --jobid once when running analysis for multiple sessions in one command:

`python sel_log_parser.py -a $SAUCE_USERNAME -k $SAUCE_ACCESS_KEY -u awesome.userName --jobid 6e709ff746664fy896b467675b886e40 a3332d53yead44899962354drr789747`


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
1. `cd sauce-log-parser`
1. `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
1. Start analyzing tests!


## Contributing and Testing
Fork the remote master branch and make pull requests.  Open issues if something is wrong and copy-paste your input & output.

Launch tests with `py.test`. Pytest is used and the `/tests` directory should get you started on seeing what is covered and what tests should look like.