from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.sheets.prerequisite import PreReqs
# from apiclient import discovery
# from schema import Schema, And, Use, Optional
# import os.path
# from os import path
import pytest
# import time
# import webbrowser


class TestSheetsCreate:

    g.add_log(g.log, filename='./logs/sheets_create')

    @pytest.mark.create_sheet
    @pytest.mark.regression
    def test_create_sheet(self, print_logging):
        """
        Test that we can read a sheet using the credential object
        :return:
        """

        g.log.info('Instantiate SheetsConnector object')
        FLEX = SheetsConnector()
        g.log.info('Get Credentials')
        credentials = FLEX.get_credentials()

        g.log.info('Instantiate Prereqs')
        prereq = PreReqs()
        g.log.info('create New sheet')
        prereq.createNewSheet(credentials, 'Pytest Test Sheet')

        # TODO: add remove GoogleSheet

    @pytest.mark.import_data
    def test_import_data(self, deftestdata, print_logging):
        """
        Test that we can read a sheet using the credential object
        Requires testdata[] pointing to valid sheet
        :return:
        """
        projections = deftestdata['projections']
        FanDuel_Salaries = deftestdata['FanDuel_Salaries']
        Sheet_Name = deftestdata['Sheet_Name']
        questionable = deftestdata['questionable']

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

        prereq.addTab(spreadsheet, service, 'FanDuel')

        prereq.importSpecificTabData(credentials, spreadsheet, 'FanDuel', FanDuel_Salaries)

        sheetId0 = prereq.gatherFacts(spreadsheet, service, 0)
        sheetId1 = prereq.gatherFacts(spreadsheet, service, 1)

        # ================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 5, 6)

        result = prereq.writeToCell(spreadsheet, service, 'w/o quote', "FanDuel!F1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(D2, "\'","")', "FanDuel!F2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 5, 6)

        # ================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 6, 7)

        result = prereq.writeToCell(spreadsheet, service, 'w/o II', "FanDuel!G1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(F2, " III","")', "FanDuel!G2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 6, 7)

        # ================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 7, 8)

        result = prereq.writeToCell(spreadsheet, service, 'w/o Jr', "FanDuel!H1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(G2, " Jr.","")', "FanDuel!H2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 7, 8)

        # ================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 8, 9)

        result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!I1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(H2, "DJ","D.J.")', "FanDuel!I2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 8, 9)
        # =================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 9, 10)

        result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!J1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(I2, " II","")', "FanDuel!J2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 9, 10)
        # =================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 10, 11)

        result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!K1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(J2, " V","")', "FanDuel!K2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 10, 11)

        # =================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 11, 12)

        result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!L1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        if (questionable == 'true'):
          result = prereq.writeToCell(spreadsheet, service, '=IF (OR(S2="IR", S2="D", AND(S2="O", B2<>"QB")), "#N/A", K2)', "FanDuel!L2")
          g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
          g.log.info('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        else:
          result = prereq.writeToCell(spreadsheet, service, '=IF (OR(S2="IR", S2="D", S2="O", AND(S2="Q", B2<>"QB")), "#N/A", K2)', "FanDuel!L2")
          g.log.info('{0} cells updated.'.format(result.get('updatedCells'))) 
          g.log.info('_____________________________________________________')

        prereq.copyFormula(spreadsheet, service, sheetId1, 11, 12)

        # =REGEXREPLACE(D41, "Jr.","")
        # =REGEXREPLACE(D133, " Jr.","")
        # =REGEXREPLACE(D219, "DJ","D.J.")

        prereq.addCol(spreadsheet, service, sheetId0, 8, 9)

        result = prereq.writeToCell(spreadsheet, service, 'FanDuel_Salary', 'I1')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        # Previouse example for reference '=IF(D2="DST", VLOOKUP(B2,{FanDuel!$E$2:$E$1000,FanDuel!$H$2:$H$1000},2,FALSE), VLOOKUP(B2,{FanDuel!$D$2:$D$1000,FanDuel!$H$2:$H$1000},2,FALSE))', 'I2')  # noqa E501
        result = prereq.writeToCell(spreadsheet, service, '=IF(D2="DST", VLOOKUP(B2,{FanDuel!$E$2:$E$1000,FanDuel!$O$2:$O$1000},2,FALSE), VLOOKUP(B2,{FanDuel!$L$2:$L$1000,FanDuel!$O$2:$O$1000},2,FALSE))', 'I2')  # noqa E501
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId0, 8, 9)

        # Rename to Actual_Points bc this is what my code looks for
        result = prereq.writeToCell(spreadsheet, service, 'Actual_Points', "H1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

    @pytest.mark.sht_pretest
    def test_sheet_pre_test(self, shtCreatePreReq, print_logging):
        """
        This test is meant to test the fixture sht_create_pretest
        Which is meant to be a common way to create the base of all
        of our google sheets and start to correct naming convention.
        Requires testdata[] pointing to valid sheet.
        :param self:
        :param deftestdata:
        :param print_logging:
        :return:
        """

        g.log.info('Instantiate the spreadsheet object')
        spreadsheet = shtCreatePreReq
        g.log.info(spreadsheet)

    @pytest.mark.create_15_16_gsheet
    def test_import_historic_data_15_16(self, shtCreatePreReq, deftestdata, print_logging):
        """
        Creates google sheet for 2015 to 2016 season.
        Requires testdata[] pointing to valid sheet
        :return:
        """
        year = deftestdata["year"]
        g.log.info('Instantiate the spreadsheet object')
        spreadsheet, service, sheetId0, sheetId1 = shtCreatePreReq
        g.log.info(spreadsheet)
        g.log.info('Instantiate the prereq object')
        prereq = PreReqs()
        prereq.pyau_sheets(spreadsheet)
        g.log.info("Call to Gsheet function to fix DSTs and finish gsheet config")
        prereq.Gsheet_dst_plus_config(spreadsheet, service, sheetId0, sheetId1, year)

    @pytest.mark.create_17_19_gsheet
    def test_import_historic_data_17_19(self, shtCreatePreReq, deftestdata, print_logging):
        """
        Creates google sheet for 2017 to 2019 season.
        Requires testdata[] pointing to valid sheet
        :return:
        """
        g.log.info('Instantiate the spreadsheet object')
        spreadsheet, service, sheetId0, sheetId1 = shtCreatePreReq
        g.log.info(spreadsheet)
        g.log.info('Instantiate the prereq object')
        prereq = PreReqs()
        prereq.pyau_sheets(spreadsheet)
        g.log.info("Call to Gsheet function to fix DSTs and finish gsheet config")
        prereq.Gsheet_dst_plus_config_17_19(spreadsheet, service, sheetId0, sheetId1)
