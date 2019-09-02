from glusto.core import Glusto as g


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