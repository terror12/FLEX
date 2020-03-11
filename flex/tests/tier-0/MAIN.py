
from flex.lib.connect.connect_to_sheets import GoogleSheetsConnector
from flex.lib.data_clean.fix_df import FixUpDf
from flex.lib.data_clean.remove import Remove


FLEX = GoogleSheetsConnector('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')

# Start using methods
FLEX.get_credentials()
FLEX.rd_sheet()
full_df = FLEX.result_to_df()

FixUpDf = FixUpDf()
full_df_head = FixUpDf.fix_header(full_df)

Remove = Remove()
Remove.columns(full_df_head)
