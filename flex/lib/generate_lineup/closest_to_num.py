from glusto.core import Glusto as g


class ClosestToNum():
    """
    Class to hold all methods that aid in the creation of positional dataframes based on the
    STD passed to it.
    """

    def find_closest(self, dfp, STD):
        """
        Calls a positional dataframe and needs a specific STD value. It will:
        - Seperate out just the STD column
        - Convert the column to a list
        - Find the value in the column that is closest to the STD passed
        :param dfp:
        :return :
        """

        # Use just to STD column
        dfpSTD = dfp['STD']

        # Convert values to a list
        dfpSTD = dfpSTD.values.tolist()

        # Find the next value with the smallest difference from the passed in Standard Deviation value
        dfpclosest = min(dfpSTD, key=lambda x: abs(x - STD))
        print(dfpclosest)

        # Return the
        dfpposition = (dfpSTD.index(dfpclosest))
        print(dfpposition)

        return dfpposition