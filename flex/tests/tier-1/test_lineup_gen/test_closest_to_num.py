from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.data_clean.fix_df import FixUpDf
from flex.lib.data_clean.remove import Remove
from flex.lib.generate_lineup.closest_to_num import ClosestToNum
import pytest

class TestClosestToNum:

    g.add_log(g.log, filename='./logs/ClosesttoNumlog')


    @pytest.mark.close
    def test_closest_to_num(self, rawDataframe, print_logging, full_dataframe_prep):
        """

        :param rawDataframe:
        :param print_logging:
        :param full_dataframe_prep:
        :return:
        """
        g.log.info('Instantiate Closest_to_num object')
        Closest_to_num = ClosestToNum()

        g.log.info('Instantiate the positional dataframes')
        QB, RB, WR, TE, FLX, DST = full_dataframe_prep

        #g.log.info(QB, RB, WR, TE, FLX, DST)

        closest_QB = Closest_to_num.find_closest(QB, 1)



        g.log.info(closest_QB)
        g.log.info(RB)