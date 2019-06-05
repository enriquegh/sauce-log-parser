Small python script that analyzes the log.json file provided by a Sauce Labs test.

It gets the time commands took to run and the time in between Sauce Labs sent a response and received another request.

With those two metrics it gets the average, min, max and total of them.

This can help determine if a "slow" test is because of Selenium commands/server issue or if there is latency in the connection

## Usage
Run against one session!

`python sel_log_parser.py -a $SAUCE_USERNAME -k $SAUCE_ACCESS_KEY -u some-username some-session-id`

Run against multiple sessions!

`python sel_log_parser.py -a $SAUCE_USERNAME -k $SAUCE_ACCESS_KEY -u some-username some-session-id another-session-id third-session-id ... Nth-session`

Output:

```
test id: your-session-id
Duration:
  mean is 0.33958974618178145
  max is 480.00422978401184
  min is 0.0022919178009033203
  total is 551.8333375453949
between_commands:
  mean is 0.1021887963922153
  max is 180.5098659992218
  min is -477.2646918296814
  total is 165.95460534095764
```

## Setup
Manual Setup via git master branch:
1. `cd` to a directory where you want the python tools/files.
1. `git clone git@github.com:enriquegh/sauce-log-parser.git`
1. `cd sauce-log-parser` and start looking at times!

