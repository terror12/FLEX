import pytest
from flex.utils.read_cli import read_cli


def pytest_addoption(parser):
    parser.addoption("--testdata", action="append", help="testdata vars")


def pytest_generate_tests(metafunc):

    if 'testdata' in metafunc.fixturenames:
        metafunc.parametrize("testdata", metafunc.config.getoption('testdata'))

@pytest.fixture(scope='session')
def deftestdata(request):
    testdata = request.config.option.testdata[0]
    deftestdata = read_cli(testdata)

    return deftestdata