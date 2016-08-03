import pytest


@pytest.yield_fixture(scope='session', autouse=True)
def session_fixture():
    print('session setup')
    yield
    print('session teardown')
