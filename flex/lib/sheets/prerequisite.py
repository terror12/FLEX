from flex.lib.connect.connect_to_sheets import SheetsConnector
import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import gspread

class PreReqs():

    def createNewSheet(self, credentials, title):

        # FLEX = SheetsConnector()
        # FLEX.get_credentials()

        spreadsheet = {
            'properties': {
                'title': title
            }
        }

        service = discovery.build('sheets', 'v4', credentials=credentials)

        spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                            fields='spreadsheetId').execute()

        return spreadsheet

    def editSheet(self, credentials, spreadsheetId):

        

        # Read CSV file contents
        content = open('ffa_customrankings2019-1.csv', 'r').read()

        gc = gspread.authorize(credentials)



        gc.import_csv(spreadsheetId, content)

# TODO: Use these as examples for effort
# result = sheet.row_values(5) #See individual row
# # result = sheet.col.values(5) #See individual column
# #result = sheet.cell(5,2) # See particular cell
# pp = pprint.PrettyPrinter()

#https://medium.com/datadriveninvestor/use-google-sheets-as-your-database-using-python-77d40009860f
# Update a particular cell and lot more
# #update values
# sheet.update_cell(2,9,'500000')  #Change value at cell(2,9) in the sheet
# result = sheet.cell(2,9)
# pp.pprint(result)