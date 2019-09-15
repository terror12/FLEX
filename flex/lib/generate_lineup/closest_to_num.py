from glusto.core import Glusto as g


class ClosestToNum():
    """
    Class to hold all methods that aid in the creation of positional dataframes based on the
    STD passed to it.
    """

    def find_closest_STD(self, dfp, STD):
        """
        Calls a positional dataframe and needs a specific STD value. It will:
        - Seperate out just the STD column
        - Convert the column to a list
        - Find the STD value in the column that is closest to the STD passed
        :param STD: (int) number that represents the STD value we want to compare with
        :param dfp: (Dataframe) positional Dataframe
        :return dfpclosest: (int) The STD value that was the closest to the one passed to the function
        """

        # Use just to STD column
        dfpSTD = dfp['sdPts']

        # Convert values to a list
        dfpSTD = dfpSTD.values.tolist()

        # Find the next STD value with the smallest difference from the STD value passed in.
        dfpclosest = min(dfpSTD, key=lambda x: abs(x - STD))

        dfpclosest = (dfpSTD.index(dfpclosest))

        return dfpclosest

    def find_closest_pos(self, dfp, STD):
        """
        Calls a positional dataframe and needs a specific STD value. It will:
        - Separate out just the STD column
        - Convert the column to a list
        - Find the STD value in the column that is closest to the STD passed
        :param STD: (int) number that represents the STD value we want to compare with
        :param dfp: (Dataframe) positional Dataframe
        :return dfpposition: (list) The index that holds the player closest to target STD
        """

        # Use just to STD column
        dfpSTD = dfp['sdPts']

        # Convert values to a list
        dfpSTD = dfpSTD.values.tolist()

        # Find the next STD value with the smallest difference from the STD value passed in.
        dfpclosest = min(dfpSTD, key=lambda x: abs(x - STD))

        # Return the position in the list of the closest value
        dfpposition = (dfpSTD.index(dfpclosest))

        dfpos = dfp.values.tolist()

        dfpposition = (dfpos[dfpposition])

        return dfpposition

    def remove_closest(self, dfp, STD):
        """
        Remove the row in a Dataframe that has a STD value of int closest_STD
        :param dfp: (Dataframe) Positional Dataframe
        :param STD: (int) number that represents the STD value we want to compare with
        :return dfp: (Dataframe) Positional Dataframe with the closest_STD removed
        """

        # Use just to STD column
        dfpSTD = dfp['sdPts']

        # Convert values to a list
        dfpSTD = dfpSTD.values.tolist()

        # Find the next STD value with the smallest difference from the STD value passed in.
        dfpclosest = min(dfpSTD, key=lambda x: abs(x - STD))

        # Return the Dataframe with everything except the value = to dfpclosest
        dfp = dfp[dfp.sdPts != dfpclosest]

        return dfp
