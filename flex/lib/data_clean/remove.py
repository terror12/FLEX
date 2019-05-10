
from flex.lib.connect.connect_to_sheets import  GoogleSheetsConnector

class Remove:

    def columns(self, full_df_head):
        """

        :param full_df_head:
        :return:
        """
        # remove columns that I do not need
        df = full_df_head[['player', 'team', 'position', 'Actual_Points', 'FanDuel_Salary', 'Platform_AVG', 'STD']]
        print('\n %s' % df)
        return df


    def rm_cols(self, df):
        """
        Remove all unnecessary columns from Dataframe
        :param df: The Dataframe
        :return df: The Dataframe without uneeded columns
        """

        df = df[['player', 'team', 'position', 'Actual_Points', 'FanDuel_Salary', 'Platform_AVG', 'STD']]
        print('\n %s' % df)
        return df

    def rm_FA(self, df):
        """
        Remove all Free Agents from Dataframe
        :param df: The Dataframe
        :return df: The Dataframe without FA's
        """

        # Removes all free agents
        df = df[df.team != "FA"]

        return df

# FLEX = GoogleSheetsConnector('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
#
# # Start using methods
# FLEX.get_credentials()
# FLEX.rd_sheet()
# full_df_head = FLEX.result_to_df()
#
# Remove = Remove()
# Remove.columns(full_df_head)