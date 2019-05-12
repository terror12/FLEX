from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import GoogleSheetsConnector
from flex.lib.data_clean.fix_df import FixUpDf
from flex.lib.data_clean.remove import Remove
#from schema import Schema, And, Use, Optional
import os.path
from os import path
import pytest
from pandas import Series, DataFrame
from pandas import Series
import pandas


class TestCleanup:

    #g.add_log(g.log, filename='STDOUT')
    g.add_log(g.log, filename='./logs/Dataframecleanuplog')


    @pytest.mark.header
    def test_header(self, rawDataframe, print_logging):
        """
        Method to replace numbered header with proper headers from Google Sheets
        :param rawDataframe: Fixture to run all code to read Googlesheet and create Dataframe
        :param print_logging: Fixture to initialize logging.
        :return: True or False
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
        Method to remove all unneeded columns from Dataframe.
        :param rawDataframe: Fixture to run all code to read Googlesheet and create Dataframe
        :param print_logging: Fixture to initialize logging.
        :return: True or False
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
        Method to remove all Free Agents from Dataframe.
        :param rawDataframe: Fixture to run all code to read Googlesheet and create Dataframe
        :param print_logging: Fixture to initialize logging.
        :return: True or False
        """

        g.log.info('Connect to Googlesheet and prep the data')

        df = FixUpDf()
        df = df.fix_header(rawDataframe)

        g.log.info('Instantiate Remove() object')
        rm = Remove()
        g.log.info('Removing All Free Agents using rm_FA()')


        df = rm.rm_FA(df)
        df.values.tolist()

        for i in df.team:
            if i == 'FA':
                g.log.info('Free Agents Exist When They Shouldnt!!')
                assert False

        g.log.info('All FAs have Been Removed!!')
        assert True

    @pytest.mark.NA
    def test_rm_NA(self, rawDataframe, print_logging):
        """
        Method to remove all Non-Available from Dataframe.
        :param rawDataframe: Fixture to run all code to read Googlesheet and create Dataframe
        :param print_logging: Fixture to initialize logging.
        :return: True or False
        """

        g.log.info('Connect to Googlesheet and prep the data')

        df = FixUpDf()
        df = df.fix_header(rawDataframe)

        g.log.info('Instantiate Remove() object')
        rm = Remove()
        g.log.info('Removing All Not Available values from STD column using rm_NA()')
        df = rm.rm_NA(df)
        df.values.tolist()


        for i in df.STD:
            if i == '#N/A':
                g.log.info('Non Available Players Exist When They Shouldnt!!')
                assert False

        g.log.info('All Non-Available have Been Removed!!')
        assert True