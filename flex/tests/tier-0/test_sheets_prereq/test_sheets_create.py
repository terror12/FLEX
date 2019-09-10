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
        prereq.createNewSheet(credentials, '2019 Week1 STD')

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
        #self.spreadsheetId = deftestdata['spreadsheetId']
        #self.rangeName = deftestdata['rangeName']

        g.log.info('Instantiate SheetsConnector object')
        FLEX = SheetsConnector()
        g.log.info('Get Credentials')
        credentials = FLEX.get_credentials()

        g.log.info('Instantiate Prereqs')
        prereq = PreReqs()
        g.log.info('create New sheet')
        spreadsheetId = deftestdata['spreadsheetId']
        prereq.editSheet(credentials, spreadsheetId)