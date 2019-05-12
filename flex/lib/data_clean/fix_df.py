
class FixUpDf:


    def fix_header(self, df):
        """

        :param full_df:
        :return:
        """

        # Create proper header
        #adam = solution.posDframe(spreadsheetId, rangeName)

        # Set column labels to equal values in the 1st row
        df.columns = df.iloc[0]
        df = df[1:]

 #       print(full_df_head.head(10))

        return df

    def seperate_positions(self, df):
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


# FLEX = GoogleSheetsConnector('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
#
# # Start using methods
# FLEX.get_credentials()
# FLEX.rd_sheet()
# full_df_head = FLEX.result_to_df()
#
# Remove = Remove()
# Remove.columns(full_df_head)