
from flex.lib.connect.connect_to_sheets import  GoogleSheetsConnector

class Remove:

    def columns(self, full_df_head):
        """

        :param full_df_head:
        :return:
        """
        # remove columns that I do not need
        df = full_df_head[['player', 'team', 'position', 'Actual_Points', 'FanDuel_Salary', 'Platform_AVG', 'STD']]
        print('\n %s' % df.head(10))
        return df


    def rm_cols(self, df):
        """
        Remove all unnecessary columns from Dataframe
        :param df: The Dataframe
        :return df: The Dataframe without uneeded columns
        """

        df = df[['player', 'team', 'position', 'Actual_Points', 'FanDuel_Salary', 'Platform_AVG', 'STD']]
        print('\n %s' % df.head(10))
        return df

    def rm_FA(self, df):
        """
        Remove all Free Agents from Dataframe
        :param df: The Dataframe
        :return df: The Dataframe without FA's
        """

        # Removes all free agents
        df = df[df.team != "FA"]
        print('\n %s' % df.head(10))

        return df

    def rm_NA(self, df):
        """
        Remove all Non-Available from Dataframe
        :param df: The Dataframe
        :return df: The Dataframe without NA's
        """

        df = df[df.STD.str.contains("#N/A") == False]
        print('\n %s' % df.head(10))

        return df

    def Roster_cut(self, df):
        """
        Remove all players with a Platform_AVG of 0
        :param df: The Dataframe
        :return df: The Dataframe without 0's in Platform_AVG
        """

        df = df[df.Platform_AVG != '0']
        print('\n %s' % df.tail(10))

        return df