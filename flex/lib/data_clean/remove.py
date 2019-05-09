
from flex.lib.connect.connect_to_sheets import  GoogleSheetsConnector

class Remove:

    def columns(self, full_df_head):
        # remove columns that I do not need
        df = full_df_head[['player', 'team', 'position', 'Actual_Points', 'FanDuel_Salary', 'Platform_AVG', 'STD']]
        print(df)
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