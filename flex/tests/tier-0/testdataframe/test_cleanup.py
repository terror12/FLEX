from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
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
        :assert: True or False
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
        :assert: True or False
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
        :assert: True or False
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

    @pytest.mark.rm_low
    def test_rm_Low_Projections(self, rawDataframe, print_logging):
        """
        Method to remove all players with < 1 in Platform_AVG in Dataframe.
        :param rawDataframe: Fixture to run all code to read Googlesheet and create Dataframe
        :param print_logging: Fixture to initialize logging.
        :assert: True or False
        """
        FixUp_df = FixUpDf()
        df = FixUp_df.fix_header(rawDataframe)

        g.log.info('Instantiate Remove() object')
        rm = Remove()
        g.log.info('Removing All players with < 1 in Platform_AVG')
        df = rm.rm_Low_Projections(df)

        df.values.tolist()

        for i in df.Platform_AVG:
            if i <= 1.0:
                g.log.info('Players With Platform_AVG under 1 Exist When They Shouldnt!!')
                assert False

        g.log.info('All Player With Platform_AVG Under 1 have Been Removed!!')
        assert True


    @pytest.mark.rm_high
    def test_rm_High_Std(self, rawDataframe, print_logging):
        """
        Method to remove all Players with STD greater then 10.
        :param rawDataframe: Fixture to run all code to read Googlesheet and create Dataframe
        :param print_logging: Fixture to initialize logging.
        :assert: True or False
        """
        FixUp_df = FixUpDf()
        df = FixUp_df.fix_header(rawDataframe)

        g.log.info('Instantiate Remove() object')
        rm = Remove()
        g.log.info('Removing All Not Available values from STD column using rm_NA()')
        df = rm.rm_NA(df)
        g.log.info('Removing All players with STD >= 10')
        df = rm.rm_High_Std(df)


        df.values.tolist()

        for i in df.STD:
            if i >= 10.0:
                g.log.info('Players With STD >= 10.0 Exist When They Shouldnt!!')
                assert False

        g.log.info('All players with STD >= 10.0 have Been Removed!!')
        assert True

    @pytest.mark.seperate
    def test_seperate_Positions(self, rawDataframe, print_logging):
        """
        Test that the full Dataframe is broken up by position
        :param rawDataframe: Fixture to run all code to read Googlesheet and create Dataframe
        :param print_logging: Fixture to initialize logging.
        :assert: True or False
        """

        g.log.info('Instantiate FixUpDF() object')
        FixUp_df = FixUpDf()
        df = FixUp_df.fix_header(rawDataframe)

        g.log.info('Seperating Full Dataframe Into Positional Dataframes')
        QB, RB, WR, TE, DST = FixUp_df.seperate_positions(df)


        g.log.info('Ensure that no other position is in QB Datframe')
        CHECK_QB = False
        for i in QB.position:
            if i in ('RB', 'WR', 'TE', 'DST'):
                assert False
            else:
                CHECK_QB = True
        g.log.info('Ensure that no other position is in RB Datframe')
        CHECK_RB = False
        for i in RB.position:
            if i in ('QB', 'WR', 'TE', 'DST'):
                assert False
            else:
                CHECK_RB = True
        g.log.info('Ensure that no other position is in WR Datframe')
        CHECK_WR = False
        for i in WR.position:
            if i in ('QB', 'RB', 'TE', 'DST'):
                assert False
            else:
                CHECK_WR = True
        g.log.info('Ensure that no other position is in TE Datframe')
        CHECK_TE = False
        for i in TE.position:
            if i in ('QB', 'RB', 'WR', 'DST'):
                assert False
            else:
                CHECK_TE = True
        g.log.info('Ensure that no other position is in DST Datframe')
        CHECK_DST = False
        for i in DST.position:
            if i in ('QB', 'RB', 'WR', 'TE'):
                assert False
            else:
                CHECK_DST = True

        if CHECK_QB == True:
            g.log.info('QB Positional Dataframe Created Succesfully!!')
            g.log.info('\n %s' % QB.head(3))
        if CHECK_RB == True:
            g.log.info('RB Positional Dataframe Created Succesfully!!')
            g.log.info('\n %s' % RB.head(3))
        if CHECK_WR == True:
            g.log.info('WR Positional Dataframe Created Succesfully!!')
            g.log.info('\n %s' % WR.head(3))
        if CHECK_TE == True:
            g.log.info('TE Positional Dataframe Created Succesfully!!')
            g.log.info('\n %s' % TE.head(3))
        if CHECK_DST == True:
            g.log.info('DST Positional Dataframe Created Succesfully!!')
            g.log.info('\n %s' % DST.head(3))


        if CHECK_QB == CHECK_RB == CHECK_WR == CHECK_TE == CHECK_DST == True:
            g.log.info('=================================================')
            g.log.info('All Positional Dataframes Created Succesfully!!')
            g.log.info('=================================================')
            assert True
        else:
            g.log.info('========================================================')
            g.log.info('All Positional Dataframes Were NOT Created Succesfully!!')
            g.log.info('========================================================')
            assert False

    @pytest.mark.dupe
    def test_seperate_Positions(self, rawDataframe, print_logging):
        """
        Test to remove all players except the one with the highest Platform_AVG.
        :param rawDataframe: Fixture to run all code to read Googlesheet and create Dataframe
        :param print_logging: Fixture to initialize logging.
        :assert: True or False
        """

        FixUp_df = FixUpDf()
        df = FixUp_df.fix_header(rawDataframe)

        QB, RB, WR, TE, DST = FixUp_df.seperate_positions(df)

        g.log.info('Instantiate Remove() object')
        rm = Remove()
        g.log.info('Removing All duplicate players from the same team except one w/ highest AVG')
        QB = rm.rm_dupe(QB)
        g.log.info("Change Dataframe to a list")
        QB.values.tolist()


        df_list = []
        g.log.info("Loop Through QB Dataframe and check for duplicates")
        for i in QB.team:
            if i in df_list:
                print("There was a team that was found more then once!!")
                assert False
            else:
                df_list.append(i)

        g.log.info('There is not any duplicate team values!!')
        assert True

    @pytest.mark.limit
    def test_hit_Position_Limit(self, rawDataframe, print_logging):
        """
        Test to make sure we can limit the length of the positional dataframes.
        :param rawDataframe: Fixture to run all code to read Googlesheet and create Dataframe
        :param print_logging: Fixture to initialize logging.
        :assert: True or False
        """

        FixUp_df = FixUpDf()
        df = FixUp_df.fix_header(rawDataframe)

        QB, RB, WR, TE, DST = FixUp_df.seperate_positions(df)

        g.log.info('Instantiate Remove() object')
        rm = Remove()

        g.log.info('Set position limits')
        QB = rm.hit_Position_Limits(QB, 32)
        RB = rm.hit_Position_Limits(RB, 150)
        WR = rm.hit_Position_Limits(WR, 150)
        TE = rm.hit_Position_Limits(TE, 90)
        DST = rm.hit_Position_Limits(DST, 32)

        if len(QB) > 32 or len(DST) > 32:
            g.log.info('Either QB or DST dataframe has too many entities')
            assert False
        if len(RB) > 150 or len(WR) > 150:
            g.log.info('Ethier RB or WR dataframe has too many entities')
            assert False
        if len(TE) > 90:
            g.log.info('TE dataframe has too many entities')
            assert False

        g.log.info('All dataframes hit position limits!!')
        assert True
    @pytest.mark.needed
    def test_use_Needed_Cols(self, rawDataframe, print_logging):
        """
        Only the following 5 coumns are needed to begin creating lineups from the datframe.
        We need to check to make sure the dataframes that should have been removed were removed.
        :param rawDataframe: Fixture to run all code to read Googlesheet and create Dataframe
        :param print_logging: Fixture to initialize logging.
        :assert: True or False
        """

        FixUp_df = FixUpDf()
        df = FixUp_df.fix_header(rawDataframe)

        QB, RB, WR, TE, DST = FixUp_df.seperate_positions(df)

        g.log.info('Instantiate Remove() object')
        rm = Remove()
        QB = rm.rm_NA(QB)
        g.log.info('Seperate out only the needed Columns player, team, Actual_Points, FanDuel_Salary, STD')
        g.log.info(QB)
        QB = rm.use_Needed_Cols(QB)

        if ('Platform_AVG', 'position') in QB:
            g.log.info('Dataframe is holding columns that should have been removed')
            assert False

        g.log.info('Only needed columns Remain!!')
        assert True