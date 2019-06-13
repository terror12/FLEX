from glusto.core import Glusto as g


class ClosestToNum():
    """
    Class to hold all methods that aid in the creation of positional dataframes based on the
    STD passed to it.
    """

    def find_closest(self, dfp, STD):
        """

        :param dfp:
        :return:
        """

        # Use just to STD column
        dfpSTD = dfp['STD']
        g.log.info('+++++++++++++++++++++++++++++++++++')
        g.log.info(dfpSTD.head(5))

        # Convert values to a list
        dfpSTD = dfpSTD.values.tolist()


        dfpclosest = min(dfpSTD, key=lambda x: abs(x - STD))

        return dfpclosest