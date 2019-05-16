from glusto.core import Glusto as g
from flex.lib.data_clean.fix_df import FixUpDf
import pytest


class TestCreation:

    g.add_log(g.log, filename='./logs/DataframeCreationLog')

    @pytest.mark.flx
    def test_flx_create(self, rawDataframe, print_logging):
        """
        Create the FLX Dataframe
        :param self:
        :param rawDataframe:
        :param print_logging:
        :return:
        """

        g.log.info('Instantiate FixUpDF() object')
        FixUp_df = FixUpDf()
        df = FixUp_df.fix_header(rawDataframe)

        g.log.info('Seperating Full Dataframe Into Positional Dataframes')
        QB, RB, WR, TE, DST = FixUp_df.seperate_positions(df)

        g.log.info('Create FLX Dataframe')
        FLX = FixUp_df.flx_Create(RB, WR, TE)

        for i in FLX.position:
            if i in ('QB','DST'):
                g.log.info('There is either a Defense or QB in the FLX!!')
                assert False
            elif i not in ('RB', 'WR', 'TE'):
                g.log.info('One of the Positions is not a RB, WR, or TE!!')
                assert False

        g.log.info('All test conditions passed FLX Dataframe is good')
        assert True
