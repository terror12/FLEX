import pandas as pd


class FixUpDf:

    def fix_header(self, df):
        """
        Creates proper header
        :param full_df:
        :return:
        """

        # Set column labels to equal values in the 1st row
        df.columns = df.iloc[0]
        df = df[1:]

        return df

    def seperate_positions(self, df):
        """
        Function to brak up full dataframe into postional dataframes
        :param df:
        :return:
        """

        # Create dataframe of just QBS
        QB = df.loc[df['position'] == 'QB']

        # Create dataframe of just RBS
        RB = df.loc[df['position'] == 'RB']

        # Create dataframe of just WRS
        WR = df.loc[df['position'] == 'WR']

        # Create dataframe of just TES
        TE = df.loc[df['position'] == 'TE']

        # Create dataframe of just DSTS
        DST = df.loc[df['position'] == 'DST']

        return QB, RB, WR, TE, DST

    def convert_to_num(self, df, col):
        """
        Convert Column into a numeric value.
        :param df:
        :return:
        """

        df[col] = pd.to_numeric(df[col])

        return df

    def hitpositionLimits(self, df, limit):
        """
        Remove the players at the bottom of the list
        to fit the specific dataframe list size
        :param df:
        :param limit:
        :return:
        """

        if len(df) > limit:
            diff = (len(df) - limit)
            df = df[:-diff]

        return df

    def order_STD(self, df, col):
        """

        :param df:
        :param col:
        :return:
        """

        df = df.sort_values(by=[col], ascending=True)

        return df

    def flx_Create(self, RB, WR, TE):
        """
        Create the FLX positional Dataframe
        :param RB: RB Dataframe
        :param WR: WR Dataframe
        :param TE: TE Dataframe
        :return: The FLX Dataframe
        """

        # Create the FLX dataframe
        FLX = pd.DataFrame()
        FLX = pd.concat([RB, WR, TE], ignore_index=True)

        return FLX


# FLEX = GoogleSheetsConnector('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
#
# # Start using methods
# FLEX.get_credentials()
# FLEX.rd_sheet()
# full_df_head = FLEX.result_to_df()
#
# Remove = Remove()
# Remove.columns(full_df_head)
