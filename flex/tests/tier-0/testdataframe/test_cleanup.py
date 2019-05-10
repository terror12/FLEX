from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import GoogleSheetsConnector
from flex.lib.data_clean.fix_df import FixUpDf
from flex.lib.data_clean.remove import Remove
#from schema import Schema, And, Use, Optional
import os.path
from os import path
import pytest


class TestCleanup:

    #g.add_log(g.log, filename='STDOUT')
    g.add_log(g.log, filename='./logs/Dataframecleanuplog')


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

    @pytest.mark.cols
    def test_rm_cols(self, rawDataframe, print_logging):
        """

        :param rawDataframe:
        :param print_logging:
        :return:
        """
        FixUp_df = FixUpDf()
        df = FixUp_df.fix_header(rawDataframe)

        rm = Remove()
        df = rm.rm_cols(df)

        schema = ['player', 'team', 'position', 'Actual_Points', 'FanDuel_Salary', 'Platform_AVG', 'STD']

        if df.columns.tolist() == schema:
            g.log.info('Success Only necessary Columns Exist!!')
            assert True
        else:
            g.log.info('Column Configuration is Incorrect!!')
            assert False


    @pytest.mark.FA
    def test_rm_FA(self, rawDataframe, print_logging):
        """

        :param rawDataframe:
        :param print_logging:
        :return:
        """
        df = FixUpDf()
        df = df.fix_header(rawDataframe)