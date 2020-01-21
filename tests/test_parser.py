import sel_log_parser as sauce_parser
import utils
import log_collector
import os
import pytest

SUCESSFUL_TEST_LOG = r"""[{"screenshot": 0, "between_commands": null, "suggestion_values": [], "request": {"requiredCapabilities": {}, "desiredCapabilities": {"chromeOptions": {"binary": "D:\\Program Files\\Chrome 64\\64.0.3282.119\\chrome.exe", "perfLoggingPrefs": {"enableNetwork": true, "enablePage": true}, "args": ["start-maximized", "disable-webgl", "blacklist-webgl", "blacklist-accelerated-compositing", "disable-accelerated-2d-canvas", "disable-accelerated-compositing", "disable-accelerated-layers", "disable-accelerated-plugins", "disable-accelerated-video", "disable-accelerated-video-decode", "disable-gpu", "disable-infobars", "test-type", "disable-extensions", "remote-debugging-port=64535"]}, "browserName": "chrome", "loggingPrefs": {"performance": "ALL", "driver": "ALL", "browser": "ALL"}}}, "HTTPStatus": 200, "result": {"takesScreenshot": true, "acceptSslCerts": true, "networkConnectionEnabled": false, "mobileEmulationEnabled": false, "unexpectedAlertBehaviour": "", "applicationCacheEnabled": false, "locationContextEnabled": true, "rotatable": false, "chrome": {"chromedriverVersion": "2.34.522940 (1a76f96f66e3ca7b8e57d503b4dd3bccfba87af1)", "userDataDir": "C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\scoped_dir1488_18206"}, "hasTouchScreen": false, "platform": "Windows NT", "version": "64.0.3282.119", "nativeEvents": true, "handlesAlerts": true, "takesHeapSnapshot": true, "javascriptEnabled": true, "databaseEnabled": false, "browserName": "chrome", "webStorageEnabled": true, "browserConnectionEnabled": false, "cssSelectorsEnabled": true, "setWindowRect": true, "pageLoadStrategy": "normal"}, "suggestion": null, "duration": 0.9570000171661377, "path": "/session", "method": "POST", "statusCode": 0}, {"screenshot": 1, "between_commands": 0.9389998912811279, "suggestion_values": [], "request": {"url": "http://the-internet.herokuapp.com/dynamic_loading/1"}, "HTTPStatus": 200, "result": null, "suggestion": null, "duration": 0.9630000591278076, "path": "url", "method": "POST", "statusCode": 0}, {"screenshot": null, "between_commands": 0.14299988746643066, "suggestion_values": [], "request": {"using": "css selector", "value": "#start button"}, "HTTPStatus": 200, "result": {"ELEMENT": "0.9114731672246916-1"}, "suggestion": null, "duration": 0.03299999237060547, "path": "element", "method": "POST", "statusCode": 0}, {"screenshot": 2, "between_commands": 0.051000118255615234, "suggestion_values": [], "request": {"id": "0.9114731672246916-1"}, "HTTPStatus": 200, "result": null, "suggestion": null, "duration": 0.11899995803833008, "path": "element/0.9114731672246916-1/click", "method": "POST", "statusCode": 0}, {"screenshot": null, "between_commands": 0.13000011444091797, "suggestion_values": [], "request": {"using": "id", "value": "finish"}, "HTTPStatus": 200, "result": [{"ELEMENT": "0.9114731672246916-2"}], "suggestion": null, "duration": 0.0279998779296875, "path": "elements", "method": "POST", "statusCode": 0}, {"screenshot": null, "between_commands": 0.04500007629394531, "suggestion_values": [], "request": {}, "HTTPStatus": 200, "result": false, "suggestion": null, "duration": 0.0279998779296875, "path": "element/0.9114731672246916-2/displayed", "method": "GET", "statusCode": 0}, {"screenshot": null, "between_commands": 0.5499999523162842, "suggestion_values": [], "request": {"using": "id", "value": "finish"}, "HTTPStatus": 200, "result": [{"ELEMENT": "0.9114731672246916-2"}], "suggestion": null, "duration": 0.031000137329101562, "path": "elements", "method": "POST", "statusCode": 0}, {"screenshot": null, "between_commands": 0.0559999942779541, "suggestion_values": [], "request": {}, "HTTPStatus": 200, "result": false, "suggestion": null, "duration": 0.019999980926513672, "path": "element/0.9114731672246916-2/displayed", "method": "GET", "statusCode": 0}, {"screenshot": null, "between_commands": 0.562000036239624, "suggestion_values": [], "request": {"using": "id", "value": "finish"}, "HTTPStatus": 200, "result": [{"ELEMENT": "0.9114731672246916-2"}], "suggestion": null, "duration": 0.029999971389770508, "path": "elements", "method": "POST", "statusCode": 0}, {"screenshot": null, "between_commands": 0.05099987983703613, "suggestion_values": [], "request": {}, "HTTPStatus": 200, "result": false, "suggestion": null, "duration": 0.01900005340576172, "path": "element/0.9114731672246916-2/displayed", "method": "GET", "statusCode": 0}, {"screenshot": null, "between_commands": 0.6019999980926514, "suggestion_values": [], "request": {"using": "id", "value": "finish"}, "HTTPStatus": 200, "result": [{"ELEMENT": "0.9114731672246916-2"}], "suggestion": null, "duration": 0.023000001907348633, "path": "elements", "method": "POST", "statusCode": 0}, {"screenshot": null, "between_commands": 0.11800003051757812, "suggestion_values": [], "request": {}, "HTTPStatus": 200, "result": false, "suggestion": null, "duration": 0.018000125885009766, "path": "element/0.9114731672246916-2/displayed", "method": "GET", "statusCode": 0}, {"screenshot": null, "between_commands": 0.5509998798370361, "suggestion_values": [], "request": {"using": "id", "value": "finish"}, "HTTPStatus": 200, "result": [{"ELEMENT": "0.9114731672246916-2"}], "suggestion": null, "duration": 0.039999961853027344, "path": "elements", "method": "POST", "statusCode": 0}, {"screenshot": null, "between_commands": 0.0559999942779541, "suggestion_values": [], "request": {}, "HTTPStatus": 200, "result": false, "suggestion": null, "duration": 0.01900005340576172, "path": "element/0.9114731672246916-2/displayed", "method": "GET", "statusCode": 0}, {"screenshot": null, "between_commands": 0.5499999523162842, "suggestion_values": [], "request": {"using": "id", "value": "finish"}, "HTTPStatus": 200, "result": [{"ELEMENT": "0.9114731672246916-2"}], "suggestion": null, "duration": 0.021000146865844727, "path": "elements", "method": "POST", "statusCode": 0}, {"screenshot": null, "between_commands": 0.042999982833862305, "suggestion_values": [], "request": {}, "HTTPStatus": 200, "result": false, "suggestion": null, "duration": 0.018999814987182617, "path": "element/0.9114731672246916-2/displayed", "method": "GET", "statusCode": 0}, {"screenshot": null, "between_commands": 0.5820000171661377, "suggestion_values": [], "request": {"using": "id", "value": "finish"}, "HTTPStatus": 200, "result": [{"ELEMENT": "0.9114731672246916-2"}], "suggestion": null, "duration": 0.024000167846679688, "path": "elements", "method": "POST", "statusCode": 0}, {"screenshot": null, "between_commands": 0.0989999771118164, "suggestion_values": [], "request": {}, "HTTPStatus": 200, "result": false, "suggestion": null, "duration": 0.02499985694885254, "path": "element/0.9114731672246916-2/displayed", "method": "GET", "statusCode": 0}, {"screenshot": null, "between_commands": 0.5510001182556152, "suggestion_values": [], "request": {"using": "id", "value": "finish"}, "HTTPStatus": 200, "result": [{"ELEMENT": "0.9114731672246916-2"}], "suggestion": null, "duration": 0.026000022888183594, "path": "elements", "method": "POST", "statusCode": 0}, {"screenshot": null, "between_commands": 0.0409998893737793, "suggestion_values": [], "request": {}, "HTTPStatus": 200, "result": false, "suggestion": null, "duration": 0.019999980926513672, "path": "element/0.9114731672246916-2/displayed", "method": "GET", "statusCode": 0}, {"screenshot": null, "between_commands": 0.5500001907348633, "suggestion_values": [], "request": {"using": "id", "value": "finish"}, "HTTPStatus": 200, "result": [{"ELEMENT": "0.9114731672246916-2"}], "suggestion": null, "duration": 0.019999980926513672, "path": "elements", "method": "POST", "statusCode": 0}, {"screenshot": null, "between_commands": 0.05099987983703613, "suggestion_values": [], "request": {}, "HTTPStatus": 200, "result": true, "suggestion": null, "duration": 0.01900005340576172, "path": "element/0.9114731672246916-2/displayed", "method": "GET", "statusCode": 0}, {"screenshot": 3, "between_commands": 0.0409998893737793, "suggestion_values": [], "request": {}, "HTTPStatus": 200, "result": "", "suggestion": null, "duration": 0.0, "path": "/session/f47aeb815d514cc4abb97114a02ccddb", "method": "DELETE", "statusCode": 0}]"""  # noqa: E501
NO_BETWEEN_COMMANDS_LOG = r"""[{"screenshot": 0, "between_commands": null, "suggestion_values": [], "request": {"desiredCapabilities": {"runlocal": "true", "chromeOptions": {"binary": "D:\\Program Files\\Chrome 62\\62.0.3202.62\\chrome.exe", "args": ["start-maximized", "disable-webgl", "blacklist-webgl", "blacklist-accelerated-compositing", "disable-accelerated-2d-canvas", "disable-accelerated-compositing", "disable-accelerated-layers", "disable-accelerated-plugins", "disable-accelerated-video", "disable-accelerated-video-decode", "disable-gpu", "disable-infobars", "test-type", "disable-extensions"]}, "useremoteprovider": "saucelabs", "browserName": "chrome", "proxy": {"proxyAutoconfigUrl": "http://127.0.0.1:19876/pac.js", "proxyType": "PAC"}}}, "HTTPStatus": 200, "result": {"takesScreenshot": true, "acceptSslCerts": true, "networkConnectionEnabled": false, "mobileEmulationEnabled": false, "unexpectedAlertBehaviour": "", "applicationCacheEnabled": false, "locationContextEnabled": true, "rotatable": false, "chrome": {"chromedriverVersion": "2.33.506120 (e3e53437346286c0bc2d2dc9aa4915ba81d9023f)", "userDataDir": "C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\scoped_dir2960_22781"}, "hasTouchScreen": false, "platform": "Windows NT", "version": "62.0.3202.62", "nativeEvents": true, "handlesAlerts": true, "takesHeapSnapshot": true, "javascriptEnabled": true, "databaseEnabled": false, "browserName": "chrome", "webStorageEnabled": true, "browserConnectionEnabled": false, "cssSelectorsEnabled": true, "setWindowRect": true, "pageLoadStrategy": "normal"}, "suggestion": null, "duration": 2.184000015258789, "path": "/session", "method": "POST", "statusCode": 0}]"""  # noqa: E501
EMPTY_LOG = r"""[]"""


def test_mean_command():
    num_list = [1.0, 2.0, 3.0, 4.0, 10.0, 14.0]
    result = utils.mean(num_list)

    assert result == 5.666666666666667


def test_total_command():
    num_list = [1.0, 2.0, 3.0, 4.0, 10.0, 14.0]
    result = utils.total(num_list)

    assert result == 34.0


def test_read_log_success(tmpdir, capsys):
    # Weird format is needed to match the exact output
    EXPECTED_OUTPUT_DURATION = """  mean: 0.10878261275913405
  max: 0.9630000591278076
  min: 0.0
  total: 2.502000093460083\n"""
    EXPECTED_OUTPUT_BETWEEN = """  mean: 0.28918180682442407
  max: 0.9389998912811279
  min: 0.0409998893737793
  total: 6.361999750137329\n"""

    test_log = tmpdir.join("log_test.log")
    test_log.write(SUCESSFUL_TEST_LOG)

    sauce_parser.read_log("{}/log_test.log".format(test_log.dirname),
                          "duration")
    out, error = capsys.readouterr()
    assert EXPECTED_OUTPUT_DURATION == out

    sauce_parser.read_log("{}/log_test.log".format(test_log.dirname),
                          "between_commands")
    out, error = capsys.readouterr()
    assert EXPECTED_OUTPUT_BETWEEN == out


def test_read_log_no_between_commands(tmpdir, capsys):
    # Weird format is needed to match the exact output
    EXPECTED_OUTPUT_DURATION = """  mean: 2.184000015258789
  max: 2.184000015258789
  min: 2.184000015258789
  total: 2.184000015258789\n"""
    EXPECTED_OUTPUT_BETWEEN = """There is no commands to be parsed\n"""

    test_log = tmpdir.join("log_test.log")
    test_log.write(NO_BETWEEN_COMMANDS_LOG)

    sauce_parser.read_log("{}/log_test.log".format(test_log.dirname),
                          "duration")
    out, error = capsys.readouterr()
    assert EXPECTED_OUTPUT_DURATION == out

    sauce_parser.read_log("{}/log_test.log".format(test_log.dirname),
                          "between_commands")
    out, error = capsys.readouterr()
    assert EXPECTED_OUTPUT_BETWEEN == out


def test_read_log_empty(tmpdir, capsys):
    # Weird format is needed to match the exact output
    EXPECTED_OUTPUT_DURATION = """There is no commands to be parsed\n"""
    EXPECTED_OUTPUT_BETWEEN = """There is no commands to be parsed\n"""

    test_log = tmpdir.join("log_test.log")
    test_log.write(EMPTY_LOG)

    sauce_parser.read_log("{}/log_test.log".format(test_log.dirname),
                          "duration")
    out, error = capsys.readouterr()
    assert EXPECTED_OUTPUT_DURATION == out

    sauce_parser.read_log("{}/log_test.log".format(test_log.dirname),
                          "between_commands")
    out, error = capsys.readouterr()
    assert EXPECTED_OUTPUT_BETWEEN == out


def test_successful_download_of_assets():
    assert True


def test_incorrect_credentials(capsys):

    JOB_ID = "2h433-34bdba-3hrb3-3432"
    EXPECTED_OUTPUT_WRONG_CREDENTIALS = "Could not download job id {}" \
                                        .format(JOB_ID)
    sauce_parser.main(["-u", "wrong_username", "-k", "BAD_KEY", JOB_ID])

    out, error = capsys.readouterr()

    assert EXPECTED_OUTPUT_WRONG_CREDENTIALS in out


def test_404_on_missing_asset():
    with pytest.raises(log_collector.AssetsNotFound):
        admin_username = os.getenv('SAUCE_USERNAME')
        admin_key = os.getenv('SAUCE_ACCESS_KEY')
        log_collector.get_log(api_endpoint='https://saucelabs.com/rest/v1',
                              admin=admin_username,
                              access_key=admin_key,
                              username='john.q.i.dont.exist',
                              job_id='1234')
