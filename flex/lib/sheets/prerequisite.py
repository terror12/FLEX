from flex.lib.connect.connect_to_sheets import SheetsConnector
import httplib2
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import gspread
import pygsheets
import csv
import webbrowser
import time
import pyautogui

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

        response = service.spreadsheets().create(body=spreadsheet,
                                            fields='spreadsheetId').execute()
        print(response["spreadsheetId"])
        #print(spreadsheet.id)

        return response["spreadsheetId"], service

    def gatherFacts(self, spreadsheet, service, num):
        response = service.spreadsheets().get(spreadsheetId=spreadsheet).execute()
        #response = request.execute()

        #'sheets': [{'properties': {'sheetId'

        print(response)
        print(response["sheets"])
        print(response["sheets"][0])
        print(response["sheets"][0]["properties"])
        print(response["sheets"][0]["properties"]["sheetId"])
        print(response["sheets"][1]["properties"]["sheetId"])

        return response["sheets"][num]["properties"]["sheetId"]

    def importData(self, credentials, spreadsheetId, data_file):

        # Read CSV file contents
        content = open(data_file, 'r').read()

        gc = gspread.authorize(credentials)

        gc.import_csv(spreadsheetId, content)


    def pyau_sheets(self, spreadsheet):

        a_website = 'https://docs.google.com/spreadsheets/d/%s' % spreadsheet
            #
        # Open url in a new window of the default browser, if possible
        webbrowser.open_new(a_website)
            # # username = deftestdata['username']
            # # password = deftestdata['password']
            # # full_path_filename = deftestdata['full_path_filename']
            # #            spreadsheetID = deftestdata['full_path_filename']
            #
        time.sleep(55)
        # Click on FanDuel tab
        # Account for changes that were made!
        pyautogui.moveTo(367, 1180)    #1586, 192)
        pyautogui.click()
       
        time.sleep(20)
      
        # highlight entire player column
        pyautogui.moveTo(707, 303)   #1173)
        # time.sleep(30)
        pyautogui.click()
        time.sleep(10)
        # Click on 'Add-ons'
        pyautogui.moveTo(419, 213)  #295, 307)
        pyautogui.click()
        time.sleep(2)
       
        # Click on split names
        #pyautogui.moveTo(473,297)   #417, 213)
        #pyautogui.click()
        #time.sleep(2)
        #
        #pyautogui.moveTo(474, 297)
        #pyautogui.click()
        #time.sleep(2)
        # pyautogui.moveTo(1271, 691)
        #pyautogui.click()
        time.sleep(5)
        pyautogui.press('down')
        time.sleep(5)
#        pyautogui.press('down')
       
        pyautogui.press('enter')
       
        time.sleep(5)
       
        pyautogui.press('enter')
        # Click start in add on
        # pyautogui.moveTo(1664, 394)
        # pyautogui.click()
        time.sleep(30)
       
        # start of right to the source
        pyautogui.moveTo(926, 846)
        pyautogui.click()
        time.sleep(20)
        pyautogui.moveTo(1033, 841)
        pyautogui.click()


    def importSpecificTabData(self, credentials, spreadsheet, tab_name, data_file):
        gc = gspread.authorize(credentials)
        spreadsheet = spreadsheet  # Please set spreadsheet ID.
        tab_name = tab_name  # Please set sheet name you want to put the CSV data.
        data_file = data_file  # Please set the filename and path of csv file.

        sh = gc.open_by_key(spreadsheet)
        sh.values_update(
            tab_name,
            params={'valueInputOption': 'USER_ENTERED'},
            body={'values': list(csv.reader(open(data_file)))}
        )


    def addTab(self, spreadsheet, service, tab_name):
        #credentials = get_credentials(client_secret_file_path)
        #service = discovery.build('sheets', 'v4', credentials=credentials)
        add_tab_request = {
            "requests": {
                "addSheet": {
                    "properties": {
                        "title": tab_name
                    }
                }
            }
        }

        service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet, body=add_tab_request).execute()


    def addCol(self, spreadsheet, service, sheetId, start, end):

        add_col_request = {
            "requests": {
                "insertDimension": {
                    "range": {
                        "sheetId": sheetId,
                        "dimension": "COLUMNS",
                        "startIndex": start,
                        "endIndex": end
                    }
                }
            }
        }

        service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet, body=add_col_request).execute()

    def rmCol(self, spreadsheet, service, sheetId, start, end):

        add_col_request = {
            "requests": {
                "deleteDimension": {
                    "range": {
                        "sheetId": sheetId,
                        "dimension": "COLUMNS",
                        "startIndex": start,
                        "endIndex": end
                    }
                }
            }
        }

        service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet, body=add_col_request).execute()

    def writeToCell(self, spreadsheet, service, data, range):
        values = [
            [
                data
            ],
        ]
        body = {
            'values': values
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet, range=range,
            valueInputOption="USER_ENTERED", body=body).execute()

        return result

    def copyFormula(self, spreadsheet, service, sheetId, start_col, end_col):
        #service = build('sheets', 'v4', credentials=creds)
        #spreadsheet_id = '###'  # Please set Spreadsheet ID.
        #sheetId = "###"  # Please set sheet ID.

        batch_update_spreadsheet_request_body = {
            "requests": {
                "copyPaste": {
                    "source": {
                        "sheetId": sheetId,
                        "startRowIndex": 1,
                        "endRowIndex": 2,
                        "startColumnIndex": start_col,
                        "endColumnIndex": end_col
                    },
                    "destination": {
                        "sheetId": sheetId,
                        "startRowIndex": 2,
                        "endRowIndex": 1448,
                        "startColumnIndex": start_col,
                        "endColumnIndex": end_col
                    },
                    "pasteType": "PASTE_FORMULA"
                }
            }
        }

        # add_col_request = {
        #     "requests": {
        #         "insertDimension": {
        #             "range": {
        #                 "sheetId": sheetId,
        #                 "dimension": "COLUMNS",
        #                 "startIndex": 8,
        #                 "endIndex": 9
        #             }
        #         }
        #     }
        # }
        request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet,
                                                     body=batch_update_spreadsheet_request_body)
        response = request.execute()
        print(response)

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
