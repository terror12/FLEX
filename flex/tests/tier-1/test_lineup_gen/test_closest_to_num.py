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
        This test will make sure that the closest value to the STD of 1 is being returned.
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

        STD = 10

        closest_QB = Closest_to_num.find_closest(QB, STD)

        QBSTD = QB['STD']

        # Convert values to a list
        QBSTD = QBSTD.values.tolist()
        # Test that the difference from the STD for the chosen index is always <= other index values
        test_position1 = (QBSTD[3])
        test_position2 = (QBSTD[5])
        test_position3 = (QBSTD[7])
        closest_position = (QBSTD[closest_QB])

        g.log.info('closest_QB')
        g.log.info(closest_QB)
        g.log.info(QB)


        g.log.info(closest_position)
        #g.log.info(closest_position['STD'])
        g.log.info(test_position1)

        diff = abs(closest_position - STD)
        g.log.info('diff')
        g.log.info(diff)
        diff_test1 = abs(test_position1 - STD)
        diff_test2 = abs(test_position2 - STD)
        diff_test3 = abs(test_position3 - STD)
        g.log.info('diff_test')
        g.log.info(diff_test1)
        g.log.info(diff_test2)
        g.log.info(diff_test3)

        if diff > diff_test1 or diff > diff_test2 or diff > diff_test3:
            g.log.info('Index Chosen does not hold the closest to STD!!')
            assert False

        else:
            g.log.info('The test values were not closer to STD value.. SUCCESS!')
            assert True