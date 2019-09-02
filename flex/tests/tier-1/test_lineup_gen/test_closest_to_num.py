from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.data_clean.fix_df import FixUpDf
from flex.lib.data_clean.remove import Remove
from flex.lib.generate_lineup.closest_to_num import ClosestToNum
import pytest
import random

class TestClosestToNum:

    g.add_log(g.log, filename='./logs/ClosesttoNumlog')


    @pytest.mark.find_close
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

        STD = random.randint(1, 10)

        g.log.info('set the STD value for run at %s' % STD)

        closest_QB = Closest_to_num.find_closest_STD(QB, STD)

        QBSTD = QB['STD']

        # Convert values to a list
        QBSTD = QBSTD.values.tolist()
        # Test that the difference from the STD for the chosen index is always <= other index values
        test_position1 = (QBSTD[3])
        test_position2 = (QBSTD[10])
        test_position3 = (QBSTD[20])
        closest_position_value = (QBSTD[closest_QB])

        g.log.info('Position in list of closest QB is %s' % closest_QB)

        g.log.info('closest position value is %s' % closest_position_value)
        g.log.info('test_position1 value is %s' % test_position1)
        g.log.info('test_position2 value is %s' % test_position2)
        g.log.info('test_position3 value is %s' % test_position3)

        diff = abs(closest_position_value - STD)
        g.log.info('The difference of the chosen position value is %s' % diff)
        diff_test1 = abs(test_position1 - STD)
        diff_test2 = abs(test_position2 - STD)
        diff_test3 = abs(test_position3 - STD)
        g.log.info('difference of test1 %s' % diff_test1)
        g.log.info('difference of test2 %s' % diff_test2)
        g.log.info('difference of test3 %s' % diff_test3)

        if diff > diff_test1 or diff > diff_test2 or diff > diff_test3:
            g.log.info('Index Chosen does not hold the closest to STD!!')
            assert False

        else:
            g.log.info('The test values were not closer to STD value.. SUCCESS!')
            assert True

    @pytest.mark.rm_close
    def test_rm_closest_to_num(self, rawDataframe, print_logging, full_dataframe_prep):
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

        # Generate Random int
        STD = random.randint(1, 5)
        g.log.info('set the STD value for run at %s' % STD)

        closest_QB_STD = Closest_to_num.find_closest_STD(QB, STD)
        g.log.info('The QB with the closest STD value is #%s in the list' % closest_QB_STD)

        closest_QB_pos = Closest_to_num.find_closest_pos(QB, STD)

        g.log.info('The QB to be removed is %s' % closest_QB_pos)

        QB = Closest_to_num.remove_closest(QB, closest_QB_STD)