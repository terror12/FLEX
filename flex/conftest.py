import pytest
from flex.utils.read_cli import read_cli
from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.data_clean.remove import Remove
from flex.lib.data_clean.fix_df import FixUpDf

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
    """
    Fixture that handles all credentials and creation of a raw dataframe
    :param request:
    :return:
    """
    testdata = request.config.option.testdata[0]
    deftestdata = read_cli(testdata)
    spreadsheetId = deftestdata['spreadsheetId']
    rangeName = deftestdata['rangeName']

    FLEX = SheetsConnector(spreadsheetId, rangeName)
    FLEX.get_credentials()
    FLEX.rd_sheet()
    full_df = FLEX.result_to_df()

    return full_df

@pytest.fixture(scope='session')
def full_dataframe_prep(request, rawDataframe):
    """
    Fixture to do everything necessary to prepare dataframes for lineup creation
    :param request:
    :return:
    """

    FixUp_df = FixUpDf()
    df = FixUp_df.fix_header(rawDataframe)

    rm = Remove()
    g.log.info('Remove uneeded columns')
    df = rm.rm_cols(df)

    g.log.info('Removing All Free Agents using rm_FA()')
    df = rm.rm_FA(df)

    g.log.info('Removing All Not Available values from STD column using rm_NA()')
    df = rm.rm_NA(df)

    g.log.info('Removing All players with < 1 in Platform_AVG')
    df = rm.rm_Low_Projections(df)

    g.log.info('Removing All players with STD >= 10')
    df = rm.rm_High_Std(df)

    g.log.info('Converting STD Column to Integer Values')
    df = FixUp_df.convert_to_num(df, 'sdPts')

    g.log.info('Clean FanDuel_Salary column')
    rm.clean_FanDuel_Salary(df)

    g.log.info('Seperating Full Dataframe Into Positional Dataframes')
    QB, RB, WR, TE, DST = FixUp_df.seperate_positions(df)

    g.log.info('Set position limits')
    QB = rm.hit_Position_Limits(QB, 32)
    RB = rm.hit_Position_Limits(RB, 150)
    WR = rm.hit_Position_Limits(WR, 150)
    TE = rm.hit_Position_Limits(TE, 90)
    DST = rm.hit_Position_Limits(DST, 32)

    g.log.info('Seperate out only the needed Columns player, team, Actual_Points, FanDuel_Salary, STD')
    QB = rm.use_Needed_Cols(QB)
    RB = rm.use_Needed_Cols(RB)
    WR = rm.use_Needed_Cols(WR)
    TE = rm.use_Needed_Cols(TE)
    DST = rm.use_Needed_Cols(DST)

    g.log.info('Create FLX Dataframe')
    FLX = FixUp_df.flx_Create(RB, WR, TE)

    #g.log.info(QB.head(5), RB.head(5), WR.head(5), TE.head(5), FLX.head(5), DST.head(5))

    return QB, RB, WR, TE, FLX, DST

@pytest.fixture(scope='session')
def print_logging():

    g.add_log(g.log, filename='STDOUT')