from glusto.core import Glusto as g
# from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.data_clean.fix_df import FixUpDf
from flex.lib.data_clean.remove import Remove
# from schema import Schema, And, Use, Optional
# import os.path
# from os import path
import pytest
# from pandas import Series, DataFrame
# from pandas import Series
# import pandas


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
        schema = ['playerId', 'player', 'team', 'position', 'age', 'exp', 'bye', 'Actual_Points', 'FanDuel_Salary', 'upper', 'sdPts', 'positionRank']

        try:
            assert new_head.columns.tolist() == schema
        except ValueError as v_err:
            g.log.info(v_err)
        else:
            if new_head.columns.tolist() == schema:
                g.log.info('Success headers match!!')
            else:
                g.log.info('Headers DO NOT match')
                assert False

    @pytest.mark.cols
    @pytest.mark.regression
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

        schema = ['player', 'team', 'position', 'Actual_Points', 'FanDuel_Salary', 'sdPts']

        try:
            assert df.columns.tolist() == schema
        except ValueError as v_err:
            g.log.info(v_err)
        else:
            if df.columns.tolist() == schema:
                g.log.info('Success Only necessary Columns Exist!!')
            else:
                g.log.info('Column Configuration is Incorrect!!')
                assert False

    @pytest.mark.FA
    @pytest.mark.regression
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
    @pytest.mark.regression
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
        g.log.info('Removing All Not Available values from sdPts column using rm_NA()')
        df = rm.rm_NA(df)
        df.values.tolist()

        for i in df.sdPts:
            if i == '#N/A':
                g.log.info('Non Available Players Exist When They Shouldnt!!')
                assert False
        g.log.info('All Non-Available have Been Removed!!')
        assert True

    @pytest.mark.rm_low
    def test_rm_low_projections(self, rawDataframe, print_logging):
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
        g.log.info('Instantiate Remove() object')
        FixUp_df = FixUpDf()
        g.log.info('Removing N/A prior to testing rm low')
        df = rm.rm_NA(df)
        g.log.info('Removing All players with < 1 in Platform_AVG')
        df = rm.rm_Low_Projections(df)

        df.values.tolist()

        FixUp_df.convert_to_num(df, "upper")

        for i in df.upper:
            print(i)
            if i <= 1.0:
                g.log.info('Players With Platform_AVG under 1 Exist When They Shouldnt!!')
                assert False

        g.log.info('All Player With Platform_AVG Under 1 have Been Removed!!')
        assert True

    @pytest.mark.rm_high
    @pytest.mark.regression
    def test_rm_high_sdpts(self, rawDataframe, print_logging):
        """
        Method to remove all Players with sdPts greater then 10.
        :param rawDataframe: Fixture to run all code to read Googlesheet and create Dataframe
        :param print_logging: Fixture to initialize logging.
        :assert: True or False
        """
        FixUp_df = FixUpDf()
        df = FixUp_df.fix_header(rawDataframe)

        g.log.info('Instantiate Remove() object')
        rm = Remove()
        g.log.info('Removing All Not Available values from sdPts column using rm_NA()')
        df = rm.rm_NA(df)
        g.log.info('Removing All players with sdPts >= 10')
        df = rm.rm_High_Std(df)

        df.values.tolist()

        for i in df.sdPts:
            if i >= 10.0:
                g.log.info('Players With sdPts >= 10.0 Exist When They Shouldnt!!')
                assert False

        g.log.info('All players with sdPts >= 10.0 have Been Removed!!')
        assert True

    @pytest.mark.seperate
    @pytest.mark.regression
    def test_seperate_positions(self, rawDataframe, print_logging):
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

        if CHECK_QB:
            g.log.info('QB Positional Dataframe Created Succesfully!!')
            g.log.info('\n %s' % QB.head(3))
        if CHECK_RB:
            g.log.info('RB Positional Dataframe Created Succesfully!!')
            g.log.info('\n %s' % RB.head(3))
        if CHECK_WR:
            g.log.info('WR Positional Dataframe Created Succesfully!!')
            g.log.info('\n %s' % WR.head(3))
        if CHECK_TE:
            g.log.info('TE Positional Dataframe Created Succesfully!!')
            g.log.info('\n %s' % TE.head(3))
        if CHECK_DST:
            g.log.info('DST Positional Dataframe Created Succesfully!!')
            g.log.info('\n %s' % DST.head(3))

        if (CHECK_QB == CHECK_RB == CHECK_WR == CHECK_TE == CHECK_DST) is True:
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
    def test_dupe_positions(self, rawDataframe, print_logging):
        """
        Test to remove all duplicate players keeping the ones with the higher Platform_AVG.
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
    @pytest.mark.regression
    def test_hit_position_limit(self, rawDataframe, print_logging):
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

    # TODO: ensure that I can remove this code before actually deleting it
    # @pytest.mark.needed
    # def test_use_Needed_Cols(self, rawDataframe, print_logging):
    #     """
    #     Only the following 5 columns are needed to begin creating lineups from the dataframe.
    #     We need to check to make sure the columns that should have been removed were removed.
    #     :param rawDataframe: Fixture to run all code to read Googlesheet and create Dataframe
    #     :param print_logging: Fixture to initialize logging.
    #     :assert: True or False
    #     """
    #
    #     FixUp_df = FixUpDf()
    #     df = FixUp_df.fix_header(rawDataframe)
    #
    #     QB, RB, WR, TE, DST = FixUp_df.seperate_positions(df)
    #
    #     g.log.info('Instantiate Remove() object')
    #     rm = Remove()
    #     QB = rm.rm_NA(QB)
    #     g.log.info('Seperate out only the needed Columns player, team, Actual_Points, FanDuel_Salary, sdPts')
    #     g.log.info(f"Before: {QB.head(0)}")
    #     QB = rm.use_Needed_Cols(QB)
    #     g.log.info(f"After: {QB.head(0)}")
    #
    #     if ('position') in QB:
    #         g.log.info('Dataframe is holding columns that should have been removed')
    #         assert False
    #
    #     g.log.info('Only needed columns Remain!!')
    #     assert True
