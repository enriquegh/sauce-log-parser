import sauce_build as b
import tests.constants as consts


def test_get_build_id():
    build_id = 'UNIQUE_BUILD_ID'
    build = b.Build('https://myendpoint.com', 'username', build_id)

    assert build.build_id == build_id
    assert build.get_build_id() == build_id


def test_get_username():
    username = 'my_username'
    build = b.Build('https://myendpoint.com', username, 'build_id')

    assert build.username == username


def test_get_endpoint():
    endpoint = 'https://myendpoint.com'
    build = b.Build(endpoint, 'username', 'build_id')

    assert build.api_endpoint == endpoint


def test_get_job_list(requests_mock):
    build = b.Build('https://myendpoint.com/rest/v1', 'username', 'build_id')
    requests_mock.get('https://myendpoint.com/rest/v1/builds/' +
                      build.get_build_id() + '/jobs',
                      json=consts.BUILD_JOBS_RESP)

    build.get_job_ids('admin_creds', 'access_key')

    assert build.get_job_list() == consts.BUILD_JOBS_LIST


def test_build_jobs(requests_mock):
    pass
    # build = b.Build('https://myendpoint.com/rest/v1', 'username', 'build_id')
    # requests_mock.get('https://myendpoint.com/rest/v1/builds/' +
    #                   build.get_build_id() + '/jobs',
    #                   json=consts.BUILD_JOBS_RESP)
    # build.get_job_ids('admin_creds', 'access_key')
    # build.build_jobs('admin_creds', 'access_key', False)
