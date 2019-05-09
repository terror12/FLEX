from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import GoogleSheetsConnector
from flex.lib.data_clean.fix_df import FixUpDf
#from schema import Schema, And, Use, Optional
import os.path
from os import path
import pytest


class TestCleanup:

    #g.add_log(g.log, filename='STDOUT')
    g.add_log(g.log, filename='./Dataframecleanuplog')


    @pytest.mark.header
    def test_header(self, rawDataframe, print_logging):
        """

        :return:
        """

        head = FixUpDf()
        new_head = head.fix_header(rawDataframe)
        schema = ['player', 'team', 'position', 'Actual_Points', 'CBS Projected Points', 'ESPN', 'NFL', 'FFToday', 'FanDuel_Salary', 'FanDuel', 'Platform_AVG', 'STD']

        if new_head.columns.tolist() == schema:
            g.log.info('Success headers match!!')
            assert True
        else:
            g.log.info('Headers DO NOT match')
            assert False