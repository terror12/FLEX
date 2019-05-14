import pandas as pd
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

    def rm_Low_Projections(self, df):
        """
        Remove all players with a Platform_AVG Less than 1.0
        :param df: The Dataframe
        :return df: The Dataframe without Players < 1 in Platform_AVG
        """

        df['Platform_AVG'] = pd.to_numeric(df['Platform_AVG'])

        df = df[~(df['Platform_AVG'] <= 1.0)]
        print('\n %s' % df.tail(10))

        return df

    def rm_High_Std(self, df):
        """
        Remove all players with STD > 10.0
        :param df: The Dataframe
        :return df: The Dataframe without players with STD > 10.0
        """

        # Convert STD Column to integers
        df['STD'] = pd.to_numeric(df['STD'])

        df = df[~(df['STD'] >= 10.0)]
        print('\n %s' % df.tail(10))

        return df

    def rm_dupe(self, df):
        """
        Remove
        :param df:
        :return:
        """
