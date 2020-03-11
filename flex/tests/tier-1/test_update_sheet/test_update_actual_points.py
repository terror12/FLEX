from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
# from flex.lib.data_clean.fix_df import FixUpDf
# from flex.lib.data_clean.remove import Remove
# from flex.lib.generate_lineup.closest_to_num import ClosestToNum
# from flex.lib.generate_lineup.assemble_lineup import Assemble
from flex.lib.sheets.prerequisite import PreReqs

# from flex.utils.read_cli import read_cli
from apiclient import discovery
import httplib2
# from oauth2client import client
# from oauth2client import tools
# from oauth2client.file import Storage
# import os
# import pandas as pd
import pytest


class TestUpdateActualPoints:

    g.add_log(g.log, filename='./logs/UpdateActualPoints')

    @pytest.mark.update_points
    def test_update_points(self, deftestdata, rawDataframe, print_logging):

        spreadsheetId = deftestdata['spreadsheetId']
        rangeName = deftestdata['rangeName']
        sheets_object = SheetsConnector(spreadsheetId, rangeName)
        # Start using methods
        credentials = sheets_object.get_credentials()

        g.log.info('Instantiate Prereqs')
        prereq = PreReqs()

        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)

        sheetId0 = prereq.gatherFacts(spreadsheetId, service, 0)

        result = prereq.writeToCell(spreadsheetId, service, '=VLOOKUP(B2,{FanDuel!$AN$2:$AN$1000,FanDuel!$AO$2:$AO$1000},2,FALSE)', 'H2')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheetId, service, sheetId0, 7, 8)
        # result = sheets_object.rd_sheet()
        # g.log.info(result)
