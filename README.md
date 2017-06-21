Small python script that analyzes the log.json file provided by a Sauce Labs test.

It gets the time commands took to run and the time in between Sauce Labs sent a response and received another request.

With those two metrics it gets the average, min, max and total of them.

This can help determine if a "slow" test is because of Selenium commands/server issue or if there is latency in the connection
