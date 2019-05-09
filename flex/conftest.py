import pytest
from flex.utils.read_cli import read_cli
from flex.lib.connect.connect_to_sheets import GoogleSheetsConnector
from glusto.core import Glusto as g


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

@pytest.fixture(scope='session')
def rawDataframe(request):

    testdata = request.config.option.testdata[0]
    deftestdata = read_cli(testdata)
    spreadsheetId = deftestdata['spreadsheetId']
    rangeName = deftestdata['rangeName']

    FLEX = GoogleSheetsConnector(spreadsheetId, rangeName)
    FLEX.get_credentials()
    FLEX.rd_sheet()
    full_df = FLEX.result_to_df()

    return full_df


@pytest.fixture(scope='session')
def print_logging():

    g.add_log(g.log, filename='STDOUT')