from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.data_clean.fix_df import FixUpDf
from flex.lib.data_clean.remove import Remove
from flex.lib.generate_lineup.closest_to_num import ClosestToNum
import pytest
import random

class TestSTDPerPosition:

    g.add_log(g.log, filename='./logs/STDPerPositionLog')

    @pytest.mark.beststd
    def test_find_best_STD(self, rawDataframe, print_logging, full_dataframe_prep):
        """
        This test will drive the investigation into what STD is best per position
        :param rawDataframe:
        :param print_logging:
        :param full_dataframe_prep:
        :return:
        """
        # g.log.info('Instantiate Closest_to_num object')
        # Closest_to_num = ClosestToNum()

        g.log.info('Instantiate the positional dataframes')
        QB, RB, WR, TE, FLX, DST = full_dataframe_prep

        g.log.info(QB)

        # TODO: change STD value to hundreths 22.42


        # TODO: list from highest to lowest Actual points


        # TODO: figure out how to analyze the data, we need to find which STD comes up the highest most frequently.


        # g.log.info(RB)
        # g.log.info(WR)
        # g.log.info(TE)
        g.log.info(DST)
        # g.log.info(FLX)