# sauce-log-parser

Small python script that analyzes the log.json file provided by a Sauce Labs test.

It gets the time commands took to run and the time in between Sauce Labs sent a response and received another request.

With those two metrics it gets the average, min, max and total of them.

This can help determine if a "slow" test is because of Selenium commands/server issue or if there is latency in the connection

## Requirements 
- python 3

## Prerequisites
pip install requirements

## Usage

To analyze a pre-downloaded seleniumn log:
```
python sel_log_parser.py --user $SAUCE_USERNAME --access_key $SAUCE_ACCESS_KEY e7309a5c47ad412baa65f9d3454d8b0b
```

To analyze log that must be downloaded (must have Sauce Labs admin access):
```
python sel_log_parser.py --admin $SAUCE_USERNAME --access_key $SAUCE_ACCESS_KEY e7309a5c47ad412baa65f9d3454d8b0b
```

See `python sel_log_parser.py --help` for full argument list
