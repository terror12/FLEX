from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.sheets.prerequisite import PreReqs

#from schema import Schema, And, Use, Optional
import os.path
from os import path
import pytest

class TestSheetsCreate:

    g.add_log(g.log, filename='./logs/sheets_create')


    @pytest.mark.create_sheet
    def test_create_sheet(self, print_logging):
        """
        #Test that we can read a sheet using the credential object
        #:return:
        """
        #self.spreadsheetId = deftestdata['spreadsheetId']
        #self.rangeName = deftestdata['rangeName']

        g.log.info('Instantiate SheetsConnector object')
        FLEX = SheetsConnector()
        g.log.info('Get Credentials')
        credentials = FLEX.get_credentials()

        g.log.info('Instantiate Prereqs')
        prereq = PreReqs()
        g.log.info('create New sheet')
        prereq.createNewSheet(credentials, '2019 Week2 STD')

        #gsc = SheetsConnector(self.spreadsheetId, self.rangeName)

        #g.log.info('Read from Google sheet')
        #result = gsc.rd_sheet()

        #g.log.info('Print data type of Google sheet class object')
        #g.log.info(type(result))

        #assert isinstance(result, dict)

    @pytest.mark.import_data
    def test_import_data(self, deftestdata, print_logging):
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
        #spreadsheetId = deftestdata['spreadsheetId']
        prereq.importData(credentials, spreadsheet, projections)

        prereq.addTab(spreadsheet, service, 'FanDuel')

        prereq.importSpecificTabData(credentials, spreadsheet, 'FanDuel', FanDuel_Salaries)

        sheetId0 = prereq.gatherFacts(spreadsheet, service, 0)
        sheetId1 = prereq.gatherFacts(spreadsheet, service, 1)

        #================================================
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
        #=================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 9, 10)

        result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!J1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(I2, " II","")', "FanDuel!J2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 9, 10)
        #=================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 10, 11)

        result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!K1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(J2, " V","")', "FanDuel!K2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 10, 11)
        # =REGEXREPLACE(D41, "Jr.","")
        # =REGEXREPLACE(D133, " Jr.","")
        # =REGEXREPLACE(D219, "DJ","D.J.")


        prereq.addCol(spreadsheet, service, sheetId0, 8, 9)

        result = prereq.writeToCell(spreadsheet, service, 'FanDuel_Salary', 'I1')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

                                                        #'=IF(D2="DST", VLOOKUP(B2,{FanDuel!$E$2:$E$1000,FanDuel!$H$2:$H$1000},2,FALSE), VLOOKUP(B2,{FanDuel!$D$2:$D$1000,FanDuel!$H$2:$H$1000},2,FALSE))', 'I2')
        result = prereq.writeToCell(spreadsheet, service, '=IF(D2="DST", VLOOKUP(B2,{FanDuel!$E$2:$E$1000,FanDuel!$N$2:$N$1000},2,FALSE), VLOOKUP(B2,{FanDuel!$K$2:$K$1000,FanDuel!$N$2:$N$1000},2,FALSE))', 'I2')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId0, 8, 9)

        #prereq.addCol(spreadsheet, service, sheetId1, 9, 10)

        result = prereq.writeToCell(spreadsheet, service, 'Actual_Points', "H1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))