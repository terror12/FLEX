from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
# from schema import Schema, And, Use, Optional
# import os.path
from os import path
import pytest


class TestConnection:

    g.add_log(g.log, filename='./logs/connectorlog')

    @pytest.mark.json
    @pytest.mark.regression
    def test_creds_file(self, print_logging):
        """
        Test the existence of the creds json file
        :return:
        """
        g.log.info('Assert that we have a .credentials object')
        assert path.exists("sheets.googleapis.com-python-quickstart.json")

        # TODO either extend this test to check for client_secret.json

    @pytest.mark.rd_sheet
    @pytest.mark.regression
    def test_read_sheet(self, deftestdata, print_logging):
        """
        Test that we can read a sheet using the credential object
        :return:
        """
        self.spreadsheetId = deftestdata['spreadsheetId']
        self.rangeName = deftestdata['rangeName']
        gsc = SheetsConnector(self.spreadsheetId, self.rangeName)

        g.log.info('Read from Google sheet')
        result = gsc.rd_sheet()

        g.log.info('Print data type of Google sheet class object')
        g.log.info(type(result))

        assert isinstance(result, dict)

    @pytest.mark.conn
    @pytest.mark.regression
    # TODO: move to tier-1 simple workflows
    def test_connectivity(self, deftestdata, print_logging):
        """
        Assert that we can connect with our creds file and return a Dataframe
        :return:
        """

        self.spreadsheetId = deftestdata['spreadsheetId']
        self.rangeName = deftestdata['rangeName']
        g.log.info('Instantiate SheetConnector object')
        gsc = SheetsConnector(self.spreadsheetId, self.rangeName)

        g.log.info('Get credentials...')
        gsc.get_credentials()
        g.log.info('Successfully got credentials!!')

        g.log.info('Read sheet to prove creds work...')
        gsc.rd_sheet()
        g.log.info('Successfully read sheet!!')

        g.log.info('Convert data into dataframe to return subset of data...')
        data = gsc.result_to_df()
        g.log.info(data.head(10))
        g.log.info('Successfully retrieved data set!!')

        g.log.info('We are checking the length of the data to make sure it is more then 300 rows.')
        g.log.info('If less then that we most likely have an issue with the data sheet!')
        g.log.info('Number of rows in data is %s' % (len(data)))

        if (len(data) >= 300):
            assert True
        else:
            assert False
