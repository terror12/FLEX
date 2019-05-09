
class FixUpDf:


    def fix_header(self, full_df):

        # Create proper header
        #adam = solution.posDframe(spreadsheetId, rangeName)

        # Set column labels to equal values in the 1st row
        full_df.columns = full_df.iloc[0]
        full_df_head = full_df[1:]

 #       print(full_df_head.head(10))

        return full_df_head


# FLEX = GoogleSheetsConnector('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
#
# # Start using methods
# FLEX.get_credentials()
# FLEX.rd_sheet()
# full_df_head = FLEX.result_to_df()
#
# Remove = Remove()
# Remove.columns(full_df_head)