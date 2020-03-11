import pandas as pd
# from flex.lib.connect.connect_to_sheets import  SheetsConnector


class Remove:

    def rm_cols(self, df):
        """
        Remove all unnecessary columns from Dataframe
        :param df: The Dataframe
        :return df: The Dataframe without uneeded columns
        """

        df = df[['player', 'team', 'position', 'Actual_Points', 'FanDuel_Salary', 'sdPts']]
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

    def rm_NA(self, df):
        """
        Remove all Non-Available from Dataframe
        :param df: The Dataframe
        :return df: The Dataframe without NA's
        """

        df = df[df.sdPts.str.contains("#N/A") == False]  # noqa: E712
        df = df[df.sdPts.str.contains("NA") == False]  # noqa: E712
        df = df[df.Actual_Points.str.contains("#N/A") == False]  # noqa: E712
        df = df[df.FanDuel_Salary.str.contains("#N/A") == False]  # noqa: E712

        return df

    def rm_Low_Projections(self, df):
        """
        LEGACY CODE
        Remove all players with a Platform_AVG Less than 1.0
        :param df: The Dataframe
        :return df: The Dataframe without Players < 1 in Platform_AVG
        """

        df['Actual_Points'] = pd.to_numeric(df['Actual_Points'])

        df = df[~(df['Actual_Points'] <= 4.0)]

        return df

    def rm_High_Std(self, df):
        """
        Remove all players with STD > 10.0
        :param df: The Dataframe
        :return df: The Dataframe without players with STD > 10.0
        """

        # Convert STD Column to integers
        df['sdPts'] = pd.to_numeric(df['sdPts'])

        df = df[~(df['sdPts'] >= 10.0)]

        return df

    def rm_dupe(self, dfp):
        """
        Remove Players from a postional datfaframe that are on the same team so that there are no
        duplicates. Removing the lowest projected scorers first.
        :param dfp: The positional Dataframe
        :return: The Dataframe without any same team duplicates
        """

        dfp = dfp.sort_values('Platform_AVG', ascending=False).drop_duplicates('team').sort_index()

        return dfp

    def hit_Position_Limits(self, dfp, num):
        """
        Remove all but n players from dataframe. Remove from bottom of list to top.
        :param dfp: The positional Dataframe
        :return: The positional dataframe with length limits
        """

        if len(dfp) > num:
            dfp = dfp.sort_values(by=['Actual_Points'], ascending=False)
            diff = (len(dfp) - num)
            dfp = dfp[:-diff]

        return dfp

    def use_Needed_Cols(self, dfp):
        """
        Use only the needed columns 'player', 'team', 'Actual_Points', 'FanDuel_Salary', 'STD'
        This is meant to be run after dataframe is broken up into positional dataframe and cleanup tasks
        using 'Platform Avg have been done.
        :param dfp: The positional Dataframe
        :return: The positional dataframe with only needed columns
        """

        dfp = dfp[['player', 'team', 'position', 'Actual_Points', 'FanDuel_Salary', 'sdPts']]
        for i in dfp['Actual_Points']:
            if i == 'NA' or i == '#N/A':
                pass
            else:
                dfp['Actual_Points'] = dfp['Actual_Points'].astype('float')

        return dfp

    def use_cols_for_data(self, dfp):
        """
        Use only the needed columns 'Actual_Points', 'STD'
        This is meant to be run after dataframe is broken up into positional dataframe and cleanup tasks
        using 'Platform Avg have been done.
        :param dfp: The positional Dataframe
        :return: The positional dataframe with only needed columns
        """

        dfp = dfp[['Actual_Points', 'sdPts']]
        for i in dfp['Actual_Points']:
            if i == 'NA' or i == '#N/A':
                pass
            else:
                dfp['Actual_Points'] = dfp['Actual_Points'].astype('float')

        return dfp

    def clean_FanDuel_Salary(self, dfp):
        """
        The FanDuel Salary value format needs to change in order to be viewed as proper number
        :param dfp: Positional Dataframe
        :return dfp: With cleaned FanDuel salary value
        """

        dfp['FanDuel_Salary'] = [s.replace(']],', '') for s in dfp['FanDuel_Salary']]
        dfp['FanDuel_Salary'] = [s.replace('\'', '') for s in dfp['FanDuel_Salary']]
        dfp['FanDuel_Salary'] = [s.replace(']', '') for s in dfp['FanDuel_Salary']]
        dfp['FanDuel_Salary'] = [s.replace(',', '') for s in dfp['FanDuel_Salary']]
        dfp['FanDuel_Salary'] = [float(i) for i in dfp['FanDuel_Salary']]

        return dfp
