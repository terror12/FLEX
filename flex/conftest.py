import pytest
from flex.utils.read_cli import read_cli
from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.data_clean.remove import Remove
from flex.lib.data_clean.fix_df import FixUpDf
from flex.lib.sheets.prerequisite import PreReqs
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
def shtCreatePreReq(deftestdata, print_logging):
    """
    #Test that we can read a sheet using the credential object
    #:return:
    """
    projections = deftestdata['projections']
    FanDuel_Salaries = deftestdata['FanDuel_Salaries']
    Sheet_Name = deftestdata['Sheet_Name']

    g.log.info('Instantiate SheetsConnector object')
    FLEX = SheetsConnector()
    g.log.info('Get Credentials')
    credentials = FLEX.get_credentials()

    g.log.info('Instantiate Prereqs')
    prereq = PreReqs()
    g.log.info('create New sheet')
    spreadsheet, service = prereq.createNewSheet(credentials, Sheet_Name)

    g.log.info('Instantiate Prereqs')
    prereq = PreReqs()
    g.log.info('Upload Data')
    prereq.importData(credentials, spreadsheet, projections)

    result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(B2, "\.", "")', "A2")  # noqa W605

    prereq.addTab(spreadsheet, service, 'FanDuel')

    prereq.importSpecificTabData(credentials, spreadsheet, 'FanDuel', FanDuel_Salaries)

    sheetId0 = prereq.gatherFacts(spreadsheet, service, 0)
    sheetId1 = prereq.gatherFacts(spreadsheet, service, 1)

    g.log.info('Extend removal of dot')
    prereq.copyFormula(spreadsheet, service, sheetId0, 0, 1)

#    result = prereq.writeToCell(spreadsheet,service, '=REGEXREPLACE(B2, "\.","")', "sheetId0!A2")

    # ================================================
    g.log.info('Create pre_salary column')
    result = prereq.writeToCell(spreadsheet, service, 'pre_Salary', "FanDuel!E1")
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    g.log.info('Populate pre_salary column with $$$s removed')
    result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(TO_TEXT(D2), "\$","")', "FanDuel!E2")  # noqa W605
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    prereq.copyFormula(spreadsheet, service, sheetId1, 4, 5)

    g.log.info('Create Salary column')
    result = prereq.writeToCell(spreadsheet, service, 'Salary', "FanDuel!F1")
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    g.log.info('Populate Salary column with commas removed')
    result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(E2, "\,","")', "FanDuel!F2")  # noqa W605
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    prereq.copyFormula(spreadsheet, service, sheetId1, 5, 6)

    prereq.addCol(spreadsheet, service, sheetId1, 2, 3)

    g.log.info('Create Player column')
    result = prereq.writeToCell(spreadsheet, service, 'Player', "FanDuel!C1")
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    g.log.info('Populate PLayer column with Jr. removed')
    result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(B2, " Jr.","")', "FanDuel!C2")
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    prereq.copyFormula(spreadsheet, service, sheetId1, 2, 3)

    g.log.info('Create new Player column')
    prereq.addCol(spreadsheet, service, sheetId1, 3, 4)

    g.log.info('Create Salary column')
    result = prereq.writeToCell(spreadsheet, service, 'Player', "FanDuel!D1")
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    g.log.info('Populate Salary column with hyphen removed')
    result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(C2, "\'","")', "FanDuel!D2")
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    prereq.copyFormula(spreadsheet, service, sheetId1, 3, 4)

    g.log.info('Create new Player column')
    prereq.addCol(spreadsheet, service, sheetId1, 4, 5)

    g.log.info('Create Salary column')
    result = prereq.writeToCell(spreadsheet, service, 'Player', "FanDuel!E1")
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    g.log.info('Populate Salary column with II removed')
    result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(D2, "II","")', "FanDuel!E2")
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    prereq.copyFormula(spreadsheet, service, sheetId1, 4, 5)

    g.log.info('Create new Player column')
    prereq.addCol(spreadsheet, service, sheetId1, 5, 6)

    g.log.info('Create Salary column')
    result = prereq.writeToCell(spreadsheet, service, 'Player', "FanDuel!F1")
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    g.log.info('Populate Salary column with II removed')
    result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(E2, " I\,","\,")', "FanDuel!F2")  # noqa W605
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    prereq.copyFormula(spreadsheet, service, sheetId1, 5, 6)

    g.log.info('Create new Player column')
    prereq.addCol(spreadsheet, service, sheetId1, 6, 7)

    g.log.info('Create Salary column')
    result = prereq.writeToCell(spreadsheet, service, 'Player', "FanDuel!G1")
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    g.log.info('Populate Salary column with . removed')
    result = prereq.writeToCell(spreadsheet, service, '=IF(OR(REGEXMATCH(F2, "E.J."), REGEXMATCH(F2, "A.J."), REGEXMATCH(F2, "T.Y."), REGEXMATCH(F2, "D.J."), REGEXMATCH(F2, "J.J."), REGEXMATCH(F2, "T.J."), REGEXMATCH(F2, "C.J.")), REGEXREPLACE(F2, "\.",""), F2)', "FanDuel!G2")  # noqa E501
    g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

    prereq.copyFormula(spreadsheet, service, sheetId1, 6, 7)

    return spreadsheet, service, sheetId0, sheetId1


@pytest.fixture(scope='session')
def full_dataframe_prep(request, deftestdata, rawDataframe):
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

    slate = deftestdata['slate']
    g.log.info('Save Full Dataframe as a csv file.')
    with open(f'{slate}_slate_dataframe.csv', 'w') as f:
        df.to_csv(f, header=['player', 'team', 'position', 'FPPG', 'Opp', 'Injury_Indicator', 'Actual_Points', 'FanDuel_Salary', 'sdPts', 'positionRank'], index_label='id')

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

    # g.log.info(QB.head(5), RB.head(5), WR.head(5), TE.head(5), FLX.head(5), DST.head(5))

    return QB, RB, WR, TE, FLX, DST


@pytest.fixture(scope='session')
def full_dataframe_prep_for_data(request, rawDataframe, print_logging):
    """
    Fixture to do everything necessary to prepare dataframes for lineup creation
    :param request:
    :return:
    """

    FixUp_df = FixUpDf()
    df = FixUp_df.fix_header(rawDataframe)

    rm = Remove()
    # g.log.info('Remove uneeded columns')
    # df = rm.rm_cols(df)

    g.log.info('Removing All Free Agents using rm_FA()')
    df = rm.rm_FA(df)

    g.log.info('Removing All Not Available values from STD column using rm_NA()')
    df = rm.rm_NA(df)

    # g.log.info('Removing All players with < 1 in Platform_AVG')
    # df = rm.rm_Low_Projections(df)

    g.log.info('Removing All players with STD >= 10')
    df = rm.rm_High_Std(df)

    g.log.info('Converting STD Column to Integer Values')
    df = FixUp_df.convert_to_num(df, 'sdPts')

    g.log.info('Seperating Full Dataframe Into Positional Dataframes')
    QB, RB, WR, TE, DST = FixUp_df.seperate_positions(df)

    g.log.info('Set position limits')
    QB = rm.hit_Position_Limits(QB, 32)
    RB = rm.hit_Position_Limits(RB, 150)
    WR = rm.hit_Position_Limits(WR, 150)
    TE = rm.hit_Position_Limits(TE, 90)
    DST = rm.hit_Position_Limits(DST, 32)

    # g.log.info('Seperate out only the needed Columns player, team, Actual_Points, FanDuel_Salary, STD')
    # QB = rm.use_cols_for_data(QB)
    # RB = rm.use_cols_for_data(RB)
    # WR = rm.use_cols_for_data(WR)
    # TE = rm.use_cols_for_data(TE)
    # DST = rm.use_cols_for_data(DST)

    g.log.info('Create FLX Dataframe')
    FLX = FixUp_df.flx_Create(RB, WR, TE)
    # g.log.info(QB.head(5), RB.head(5), WR.head(5), TE.head(5), FLX.head(5), DST.head(5))

    return QB, RB, WR, TE, FLX, DST


@pytest.fixture(scope='session')
def print_logging():

    g.add_log(g.log, filename='STDOUT')
