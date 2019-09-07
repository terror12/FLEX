from glusto.core import Glusto as g
from flex.lib.generate_lineup.closest_to_num import ClosestToNum


class Assemble():
    """
    Class to hold functions needed to create a valid lineup.
    """
    # TODO: create __init__ method to instantiate assemble object

#    def buildLineup(self):
#        pass

    def sumTotalPoints(self, lineup):
        """
        Take the chosen lineup and sum the total points, then append
        that number to the end of lineup.
        :param lineup: (list) full 9-player lineup
        :return lineup: (list) full 9-player lineup + total points
        """

        if lineup[0][2] == 'NA':
            totalPoints = 0
            lineup.append(totalPoints)
        else:
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

        if (lineup[-1] > 59500 and lineup[-1] < 60000):
            return True
        else:

            return False

    def createLineup(self, QB, RB, WR, TE, FLX, DST, QB_STD, RB_STD, RB2_STD, WR_STD, WR2_STD, WR3_STD, TE_STD, FLX_STD, DST_STD):

        # TODO: Fix bug where FLX can be the same as a RB or WR or TE

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

        return_QB = QB
        return_RB = RB
        return_WR = WR
        return_TE = TE
        return_FLX = FLX
        return_DST = DST

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
        while FLX[closest_FLX_pos] == RB[closest_RB_pos] or FLX[closest_FLX_pos] == RB2[closest_RB2_pos] or FLX[closest_FLX_pos] == WR[closest_WR_pos] or FLX[closest_FLX_pos] == WR2[closest_WR2_pos] or FLX[closest_FLX_pos] == WR3[closest_WR3_pos] or FLX[closest_FLX_pos] == TE[closest_TE_pos]:
            return_FLX = Closest_to_num.remove_closest(return_FLX, FLX_STD)
            closest_FLX_pos = Closest_to_num.find_closest_STD(return_FLX, FLX_STD)
            FLX = return_FLX.values.tolist()
        lineup.append(FLX[closest_FLX_pos])
        lineup.append(DST[closest_DST_pos])

        # Instantiate assemble object
        assemble = Assemble()

        lineup = assemble.sumTotalPoints(lineup)
        lineup = assemble.sumTotalSalary(lineup)

        return lineup

    def findBestLineup(self, lineup, QB, RB, WR, TE, FLX, DST, QB_STD, RB_STD, RB2_STD, WR_STD, WR2_STD, WR3_STD, TE_STD, FLX_STD, DST_STD):

        g.log.info('Instantiate Closest_to_num object')
        Closest_to_num = ClosestToNum()

        # Instantiate assemble object
        assemble = Assemble()

        past = 'GO'
        count = 0
        for i in range(14):
            count += 1
            print(count)
            if assemble.hasValidSalary(lineup):
                #g.log.info('Your lineup is %s !!!!!!!!!!!!!!!!!!!!!!' % lineup)
                return lineup
            else:
                if past == 'GO':
                    # TODO: Figure out way to have the code loop back to rm QB(CHECK)

                    QB = Closest_to_num.remove_closest(QB, QB_STD)
                    g.log.info('Lineup failed salary check!!')
                    lineup = assemble.createLineup(QB, RB, WR, TE, FLX, DST, QB_STD, RB_STD, RB2_STD, WR_STD, WR2_STD, WR3_STD, TE_STD, FLX_STD, DST_STD)

                    past = 'RB'
                    g.log.info(lineup)
                elif past == 'RB':
                    RB = Closest_to_num.remove_closest(RB, RB_STD)
                    g.log.info('Lineup failed salary check!!')
                    lineup = assemble.createLineup(QB, RB, WR, TE, FLX, DST, QB_STD, RB_STD, RB2_STD, WR_STD, WR2_STD,
                                                   WR3_STD, TE_STD, FLX_STD, DST_STD)

                    past = 'WR'
                    g.log.info(lineup)
                elif past == 'WR':
                    WR = Closest_to_num.remove_closest(WR, TE_STD)
                    g.log.info('Lineup failed salary check!!')
                    lineup = assemble.createLineup(QB, RB, WR, TE, FLX, DST, QB_STD, RB_STD, RB2_STD, WR_STD, WR2_STD,
                                                   WR3_STD, TE_STD, FLX_STD, DST_STD)

                    past = 'TE'
                    g.log.info(lineup)
                elif past == 'TE':
                    TE = Closest_to_num.remove_closest(TE, TE_STD)
                    g.log.info('Lineup failed salary check!!')
                    lineup = assemble.createLineup(QB, RB, WR, TE, FLX, DST, QB_STD, RB_STD, RB2_STD, WR_STD, WR2_STD,
                                                   WR3_STD, TE_STD, FLX_STD, DST_STD)

                    past = 'FLX'
                    g.log.info(lineup)
                elif past == 'FLX':
                    FLX = Closest_to_num.remove_closest(FLX, FLX_STD)
                    g.log.info('Lineup failed salary check!!')
                    lineup = assemble.createLineup(QB, RB, WR, TE, FLX, DST, QB_STD, RB_STD, RB2_STD, WR_STD, WR2_STD,
                                                   WR3_STD, TE_STD, FLX_STD, DST_STD)

                    past = 'DST'
                    g.log.info(lineup)
                elif past == 'DST':
                    DST = Closest_to_num.remove_closest(DST, DST_STD)
                    g.log.info('Lineup failed salary check!!')
                    lineup = assemble.createLineup(QB, RB, WR, TE, FLX, DST, QB_STD, RB_STD, RB2_STD, WR_STD, WR2_STD,
                                                   WR3_STD, TE_STD, FLX_STD, DST_STD)

                    past = 'GO'
                    g.log.info(lineup)