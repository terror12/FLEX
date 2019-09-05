from glusto.core import Glusto as g
from flex.lib.generate_lineup.closest_to_num import ClosestToNum


class Assemble():
    """
    Class to hold functions needed to create a valid lineup.
    """

#    def buildLineup(self):
#        pass

    def sumTotalPoints(self, lineup):
        """
        Take the chosen lineup and sum the total points, then append
        that number to the end of lineup.
        :param lineup: (list) full 9-player lineup
        :return lineup: (list) full 9-player lineup + total points
        """

        totalPoints = sum(
            [lineup[0][2], lineup[1][2], lineup[2][2], lineup[3][2], lineup[4][2], lineup[5][2], lineup[6][2], lineup[7][2],
             lineup[8][2]])

        lineup.append(totalPoints)

        return lineup

    def sumTotalSalary(self, lineup):
        """
        Take the chosen lineup and sum the total salary, then append
        that number to the end of lineup.
        :param lineup: (list) full 9-player lineup
        :return lineup: (list) full 9-player lineup + total salary
        """

        totalSalary = sum(
            [lineup[0][3], lineup[1][3], lineup[2][3], lineup[3][3], lineup[4][3], lineup[5][3], lineup[6][3], lineup[7][3],
             lineup[8][3]])

        lineup.append(totalSalary)

        return lineup

    def hasValidSalary(self, lineup):
        """
        Test if the chosen lineup is a valid one
        :param lineup: (list) full 9-player lineup + total points and total salary
        :return None:
        """

        if (lineup[-1] > 50000 and lineup[-1] < 65000):
            return True
        else:

            return False

    def createLineup(self, QB, RB, WR, TE, FLX, DST, QB_STD, RB_STD, RB2_STD, WR_STD, WR2_STD, WR3_STD, TE_STD, FLX_STD, DST_STD):

        g.log.info('Instantiate Closest_to_num object')
        Closest_to_num = ClosestToNum()

        RB2 = Closest_to_num.remove_closest(RB, RB_STD)
        WR2 = Closest_to_num.remove_closest(WR, WR_STD)
        WR3 = Closest_to_num.remove_closest(WR2, WR2_STD)

        closest_QB_pos = Closest_to_num.find_closest_STD(QB, QB_STD)
        closest_RB_pos = Closest_to_num.find_closest_STD(RB, RB_STD)
        closest_RB2_pos = Closest_to_num.find_closest_STD(RB2, RB2_STD)
        closest_WR_pos = Closest_to_num.find_closest_STD(WR, WR_STD)
        closest_WR2_pos = Closest_to_num.find_closest_STD(WR2, WR2_STD)
        closest_WR3_pos = Closest_to_num.find_closest_STD(WR3, WR3_STD)
        closest_TE_pos = Closest_to_num.find_closest_STD(TE, TE_STD)
        closest_FLX_pos = Closest_to_num.find_closest_STD(FLX, FLX_STD)
        closest_DST_pos = Closest_to_num.find_closest_STD(DST, DST_STD)

        QB = QB.values.tolist()
        RB = RB.values.tolist()
        RB2 = RB2.values.tolist()
        WR = WR.values.tolist()
        WR2 = WR2.values.tolist()
        WR3 = WR3.values.tolist()
        TE = TE.values.tolist()
        FLX = FLX.values.tolist()
        DST = DST.values.tolist()

        # Create lineup object, this will be where the chosen players will be appended
        lineup = []

        lineup.append(QB[closest_QB_pos])
        lineup.append(RB[closest_RB_pos])
        lineup.append(RB2[closest_RB2_pos])
        lineup.append(WR[closest_WR_pos])
        lineup.append(WR2[closest_WR2_pos])
        lineup.append(WR3[closest_WR3_pos])
        lineup.append(TE[closest_TE_pos])
        lineup.append(FLX[closest_FLX_pos])
        lineup.append(DST[closest_DST_pos])

        # Instantiate assemble object
        assemble = Assemble()

        lineup = assemble.sumTotalPoints(lineup)
        lineup = assemble.sumTotalSalary(lineup)

        return lineup