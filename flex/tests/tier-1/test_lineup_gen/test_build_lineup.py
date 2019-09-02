from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.data_clean.fix_df import FixUpDf
from flex.lib.data_clean.remove import Remove
from flex.lib.generate_lineup.closest_to_num import ClosestToNum
from flex.lib.generate_lineup.assemble_lineup import Assemble
import pytest
import random

class TestBuildLineup:

    g.add_log(g.log, filename='./logs/BuildLineupLog')

    @pytest.mark.build_lineup
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

        # Set the STD values for each position
        # TODO: Work on making this user input or autogenerated.
        QB_STD = random.randint(1, 10)
        RB_STD = random.randint(1, 10)
        RB2_STD = random.randint(1, 10)

        g.log.info(QB_STD)
        g.log.info(RB_STD)
        g.log.info(RB2_STD)

        # WR_STD = random.randint(1, 10)
        # TE_STD = random.randint(1, 10)
        # FLX_STD = random.randint(1, 10)
        # DST_STD = random.randint(1, 10)

        # Create the RB2 dfp, this consists of the RB dfp minus the chosen player
        RB2 = Closest_to_num.remove_closest(RB, RB_STD)
        # WR2 = Closest_to_num.remove_closest(WR, WR_STD)
        # WR3 = Closest_to_num.remove_closest(WR2, WR2_STD)

        closest_QB_pos = Closest_to_num.find_closest_STD(QB, QB_STD)
        closest_RB_pos = Closest_to_num.find_closest_STD(RB, RB_STD)
        closest_RB2_pos = Closest_to_num.find_closest_STD(RB2, RB2_STD)
        # closest_WR = Closest_to_num.find_closest_STD(WR, WR_STD)
        # closest_TE = Closest_to_num.find_closest_STD(TE, TE_STD)
        # closest_FLX = Closest_to_num.find_closest_STD(FLX, FLX_STD)
        # closest_DST = Closest_to_num.find_closest_STD(DST, DST_STD)

        #QB_pos = Closest_to_num.find_closest_pos(QB, STD)
        #RB_pos = Closest_to_num.find_closest_pos(RB, STD)
        #RB2_pos = Closest_to_num.find_closest_pos(RB2, STD)

        QB = QB.values.tolist()
        RB = RB.values.tolist()
        RB2 = RB2.values.tolist()

        # Create lineup object, this will be where the chosen players will be appended
        lineup = []

        lineup.append(QB[closest_QB_pos])
        lineup.append(RB[closest_RB_pos])
        lineup.append(RB2[closest_RB2_pos])

        g.log.info(lineup)

        #Assemble = Assemble()


