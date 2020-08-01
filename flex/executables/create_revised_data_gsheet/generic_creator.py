from glusto.core import Glusto as g
from flex.lib.sheets.prerequisite import PreReqs

import pytest


@pytest.mark.create_17_19_gsheet
def test_import_historic_data_17_19(self, shtCreatePreReq, deftestdata,
                                    print_logging):
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
    prereq.Gsheet_dst_plus_config_17_19(spreadsheet, service, sheetId0,
                                        sheetId1)
