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
import os
from glusto.core import Glusto as g

class PreReqs():

    g.add_log(g.log, filename='./logs/sheets_create')

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
        
        # Open url in a new window of the default browser, if possible
        webbrowser.open_new(a_website)
        time.sleep(55)
        # Click on FanDuel tab
        pyautogui.moveTo(367, 1180)    #1586, 192)
        pyautogui.click()
       
        time.sleep(15)
      
        # highlight entire player column
        pyautogui.moveTo(707, 303)   #1173)
        # time.sleep(30)
        pyautogui.click()
        time.sleep(5)
        # Click on 'Add-ons'
        pyautogui.moveTo(419, 213)  #295, 307)
        pyautogui.click()
        time.sleep(2)
       
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('enter')
        # Click start in add on
        time.sleep(15)
       
        pyautogui.moveTo(926, 846)
        pyautogui.click()
        time.sleep(15)
        # Close addon pop up
        pyautogui.moveTo(1033, 841)
        pyautogui.click()

        os.system("killall -9 'chromium-browse'")

        # TODO: close the window


    def Gsheet_dst_plus_config(self, spreadsheet, service, sheetId0, sheetId1, year):
        """
        used to create sheets for the 15-16 season
        :param spreadsheet:
        :param service:
        :param sheetId0:
        :param sheetId1:
        :param year:
        :return:
        """
        self.addCol(spreadsheet, service, sheetId1, 11, 12)

        result = self.writeToCell(spreadsheet, service, '=CONCATENATE(K2, H2, I2, " ", J2)', "FanDuel!L2")
        g.log.info('Concatenating split player names')
        g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

        self.copyFormula(spreadsheet, service, sheetId1, 11, 12)

        #######################################
        # Code to map team cities to team name
        #######################################

        self.addCol(spreadsheet, service, sheetId1, 12, 13)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(L2, "Arizona Defense", "Cardinals")',
                                    "FanDuel!M2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 12, 13)

        self.addCol(spreadsheet, service, sheetId1, 13, 14)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(M2, "New YorkJ Defense", "Jets")',
                                    "FanDuel!N2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 13, 14)

        self.addCol(spreadsheet, service, sheetId1, 14, 15)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(N2, "TampaBay Defense", "Buccaneers")',
                                    "FanDuel!O2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 14, 15)

        self.addCol(spreadsheet, service, sheetId1, 15, 16)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(O2, "Dallas Defense", "Cowboys")',
                                    "FanDuel!P2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 15, 16)

        self.addCol(spreadsheet, service, sheetId1, 16, 17)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(P2, "NewEngland Defense", "Patriots")',
                                    "FanDuel!Q2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 16, 17)

        self.addCol(spreadsheet, service, sheetId1, 17, 18)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(Q2, "Cincinnati Defense", "Bengals")',
                                    "FanDuel!R2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 17, 18)

        self.addCol(spreadsheet, service, sheetId1, 18, 19)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(R2, "KansasCity Defense", "Chiefs")',
                                    "FanDuel!S2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 18, 19)

        self.addCol(spreadsheet, service, sheetId1, 19, 20)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(S2, "Philadelphia Defense", "Eagles")',
                                    "FanDuel!T2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 19, 20)

        self.addCol(spreadsheet, service, sheetId1, 20, 21)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(T2, "Pittsburgh Defense", "Steelers")',
                                    "FanDuel!U2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 20, 21)

        self.addCol(spreadsheet, service, sheetId1, 21, 22)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(U2, "Minnesota Defense", "Vikings")',
                                    "FanDuel!V2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 21, 22)

        self.addCol(spreadsheet, service, sheetId1, 22, 23)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(V2, "NewOrleans Defense", "Saints")',
                                    "FanDuel!W2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 22, 23)

        self.addCol(spreadsheet, service, sheetId1, 23, 24)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(W2, "GreenBay Defense", "Packers")',
                                    "FanDuel!X2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells'))) 
        self.copyFormula(spreadsheet, service, sheetId1, 23, 24)

        self.addCol(spreadsheet, service, sheetId1, 24, 25)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(X2, "Houston Defense", "Texans")',
                                    "FanDuel!Y2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 24, 25)

        self.addCol(spreadsheet, service, sheetId1, 25, 26)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(Y2, "Atlanta Defense", "Falcons")',
                                    "FanDuel!Z2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 25, 26)

        self.addCol(spreadsheet, service, sheetId1, 26, 27)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(Z2, "Washington Defense", "Redskins")',
                                    "FanDuel!AA2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 26, 27)

        time.sleep(60)

        self.addCol(spreadsheet, service, sheetId1, 27, 28)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AA2, "Carolina Defense", "Panthers")',
                                    "FanDuel!AB2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 27, 28)

        self.addCol(spreadsheet, service, sheetId1, 28, 29)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AB2, "Seattle Defense", "Seahawks")',
                                    "FanDuel!AC2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 28, 29)

        self.addCol(spreadsheet, service, sheetId1, 29, 30)
        if (year == 15):
            result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AC2, "St.Louis Defense", "Rams")', "FanDuel!AD2")
        else:    
            result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AC2, "LosAngeles Defense", "Rams")', "FanDuel!AD2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        self.copyFormula(spreadsheet, service, sheetId1, 29, 30)

        self.addCol(spreadsheet, service, sheetId1, 30, 31)

        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AD2, "SanDiego Defense", "Chargers")',
                                    "FanDuel!AE2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        self.copyFormula(spreadsheet, service, sheetId1, 30, 31)

        self.addCol(spreadsheet, service, sheetId1, 31, 32)

        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AE2, "Indianapolis Defense", "Colts")',
                                    "FanDuel!AF2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        self.copyFormula(spreadsheet, service, sheetId1, 31, 32)

        self.addCol(spreadsheet, service, sheetId1, 32, 33)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AF2, "Oakland Defense", "Raiders")',
                                    "FanDuel!AG2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 32, 33)

        self.addCol(spreadsheet, service, sheetId1, 33, 34)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AG2, "Jacksonville Defense", "Jaguars")',
                                    "FanDuel!AH2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 33, 34)

        self.addCol(spreadsheet, service, sheetId1, 34, 35)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AH2, "Detroit Defense", "Lions")',
                                    "FanDuel!AI2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 34, 35)

        self.addCol(spreadsheet, service, sheetId1, 35, 36)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AI2, "Buffalo Defense", "Bills")',
                                    "FanDuel!AJ2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 35, 36)

        self.addCol(spreadsheet, service, sheetId1, 36, 37)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AJ2, "New YorkG Defense", "Giants")',
                                    "FanDuel!AK2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 36, 37)

        self.addCol(spreadsheet, service, sheetId1, 37, 38)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AK2, "Tennessee Defense", "Titans")',
                                    "FanDuel!AL2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 37, 38)

        self.addCol(spreadsheet, service, sheetId1, 38, 39)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AL2, "Chicago Defense", "Bears")',
                                    "FanDuel!AM2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 38, 39)

        self.addCol(spreadsheet, service, sheetId1, 39, 40)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AM2, "Miami Defense", "Dolphins")',
                                    "FanDuel!AN2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 39, 40)

        self.addCol(spreadsheet, service, sheetId1, 40, 41)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AN2, "Baltimore Defense", "Ravens")',
                                    "FanDuel!AO2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 40, 41)

        self.addCol(spreadsheet, service, sheetId1, 41, 42)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AO2, "SanFrancisco Defense", "49ers")',
                                    "FanDuel!AP2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 41, 42)

        self.addCol(spreadsheet, service, sheetId1, 42, 43)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AP2, "Denver Defense", "Broncos")',
                                    "FanDuel!AQ2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 42, 43)

        self.addCol(spreadsheet, service, sheetId1, 43, 44)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AQ2, "Cleveland Defense", "Browns")',
                                    "FanDuel!AR2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 43, 44)

        result = self.writeToCell(spreadsheet, service, 'player', "FanDuel!AR1")

        #############################################################################

        result = self.writeToCell(spreadsheet, service, 'Actual_Points', 'H1')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        g.log.info('Copy Over points scored')
        result = self.writeToCell(spreadsheet, service,
                                    '=VLOOKUP(A2,{FanDuel!$AR$2:$AR$1000,FanDuel!$AS$2:$AS$1000},2,FALSE)', 'H2')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        self.copyFormula(spreadsheet, service, sheetId0, 7, 8)

        result = self.writeToCell(spreadsheet, service, 'FanDuel_Salary', 'I1')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        g.log.info('Copy over Salary')
        result = self.writeToCell(spreadsheet, service,
                                    '=VLOOKUP(A2,{FanDuel!$AR$2:$AR$1000,FanDuel!$AV$2:$AV$1000},2,FALSE)', 'I2')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        self.copyFormula(spreadsheet, service, sheetId0, 8, 9)

    def Gsheet_dst_plus_config_17_19(self, spreadsheet, service, sheetId0, sheetId1, year=None):
        """
        used to create sheets for the 17,18 and 19 season.
        :param spreadsheet:
        :param service:
        :param sheetId0:
        :param sheetId1:
        :param year:
        :return:
        """
        self.addCol(spreadsheet, service, sheetId1, 11, 12)

        result = self.writeToCell(spreadsheet, service, '=CONCATENATE(K2, H2, I2, " ", J2)', "FanDuel!L2")
        g.log.info('Concatenating split player names')
        g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

        self.copyFormula(spreadsheet, service, sheetId1, 11, 12)

        #######################################
        # Code to map team cities to team name
        #######################################

        self.addCol(spreadsheet, service, sheetId1, 12, 13)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(L2, "Arizona ", "Cardinals")',
                                    "FanDuel!M2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 12, 13)

        self.addCol(spreadsheet, service, sheetId1, 13, 14)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(M2, "New J", "Jets")',
                                    "FanDuel!N2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 13, 14)

        self.addCol(spreadsheet, service, sheetId1, 14, 15)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(N2, "Tampa Bay", "Buccaneers")',
                                    "FanDuel!O2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 14, 15)

        self.addCol(spreadsheet, service, sheetId1, 15, 16)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(O2, "Dallas ", "Cowboys")',
                                    "FanDuel!P2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 15, 16)

        self.addCol(spreadsheet, service, sheetId1, 16, 17)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(P2, "New England", "Patriots")',
                                    "FanDuel!Q2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 16, 17)

        self.addCol(spreadsheet, service, sheetId1, 17, 18)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(Q2, "Cincinnati ", "Bengals")',
                                    "FanDuel!R2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 17, 18)

        self.addCol(spreadsheet, service, sheetId1, 18, 19)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(R2, "Kansas City", "Chiefs")',
                                    "FanDuel!S2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 18, 19)

        self.addCol(spreadsheet, service, sheetId1, 19, 20)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(S2, "Philadelphia ", "Eagles")',
                                    "FanDuel!T2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 19, 20)

        self.addCol(spreadsheet, service, sheetId1, 20, 21)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(T2, "Pittsburgh ", "Steelers")',
                                    "FanDuel!U2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 20, 21)

        self.addCol(spreadsheet, service, sheetId1, 21, 22)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(U2, "Minnesota ", "Vikings")',
                                    "FanDuel!V2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 21, 22)

        self.addCol(spreadsheet, service, sheetId1, 22, 23)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(V2, "New Orleans", "Saints")',
                                    "FanDuel!W2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 22, 23)

        self.addCol(spreadsheet, service, sheetId1, 23, 24)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(W2, "Green Bay", "Packers")',
                                    "FanDuel!X2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 23, 24)

        self.addCol(spreadsheet, service, sheetId1, 24, 25)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(X2, "Houston ", "Texans")',
                                    "FanDuel!Y2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 24, 25)

        self.addCol(spreadsheet, service, sheetId1, 25, 26)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(Y2, "Atlanta ", "Falcons")',
                                    "FanDuel!Z2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 25, 26)

        self.addCol(spreadsheet, service, sheetId1, 26, 27)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(Z2, "Washington ", "Redskins")',
                                    "FanDuel!AA2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 26, 27)

        time.sleep(60)

        self.addCol(spreadsheet, service, sheetId1, 27, 28)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AA2, "Carolina ", "Panthers")',
                                    "FanDuel!AB2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 27, 28)

        self.addCol(spreadsheet, service, sheetId1, 28, 29)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AB2, "Seattle ", "Seahawks")',
                                    "FanDuel!AC2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 28, 29)

        self.addCol(spreadsheet, service, sheetId1, 29, 30)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AC2, "LA Rams ", "Rams")', "FanDuel!AD2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        self.copyFormula(spreadsheet, service, sheetId1, 29, 30)

        self.addCol(spreadsheet, service, sheetId1, 30, 31)

        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AD2, "LA Chargers ", "Chargers")',
                                    "FanDuel!AE2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        self.copyFormula(spreadsheet, service, sheetId1, 30, 31)

        self.addCol(spreadsheet, service, sheetId1, 31, 32)

        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AE2, "Indianapolis ", "Colts")',
                                    "FanDuel!AF2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        self.copyFormula(spreadsheet, service, sheetId1, 31, 32)

        self.addCol(spreadsheet, service, sheetId1, 32, 33)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AF2, "Oakland ", "Raiders")',
                                    "FanDuel!AG2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 32, 33)

        self.addCol(spreadsheet, service, sheetId1, 33, 34)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AG2, "Jacksonville ", "Jaguars")',
                                    "FanDuel!AH2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 33, 34)

        self.addCol(spreadsheet, service, sheetId1, 34, 35)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AH2, "Detroit ", "Lions")',
                                    "FanDuel!AI2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 34, 35)

        self.addCol(spreadsheet, service, sheetId1, 35, 36)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AI2, "Buffalo ", "Bills")',
                                    "FanDuel!AJ2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 35, 36)

        self.addCol(spreadsheet, service, sheetId1, 36, 37)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AJ2, "New G", "Giants")',
                                    "FanDuel!AK2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 36, 37)

        self.addCol(spreadsheet, service, sheetId1, 37, 38)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AK2, "Tennessee ", "Titans")',
                                    "FanDuel!AL2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 37, 38)

        self.addCol(spreadsheet, service, sheetId1, 38, 39)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AL2, "Chicago ", "Bears")',
                                    "FanDuel!AM2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 38, 39)

        self.addCol(spreadsheet, service, sheetId1, 39, 40)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AM2, "Miami ", "Dolphins")',
                                    "FanDuel!AN2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 39, 40)

        self.addCol(spreadsheet, service, sheetId1, 40, 41)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AN2, "Baltimore ", "Ravens")',
                                    "FanDuel!AO2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 40, 41)

        self.addCol(spreadsheet, service, sheetId1, 41, 42)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AO2, "San Francisco", "49ers")',
                                    "FanDuel!AP2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 41, 42)

        self.addCol(spreadsheet, service, sheetId1, 42, 43)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AP2, "Denver ", "Broncos")',
                                    "FanDuel!AQ2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 42, 43)

        self.addCol(spreadsheet, service, sheetId1, 43, 44)
        result = self.writeToCell(spreadsheet, service, '=REGEXREPLACE(AQ2, "Cleveland ", "Browns")',
                                    "FanDuel!AR2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        self.copyFormula(spreadsheet, service, sheetId1, 43, 44)

        result = self.writeToCell(spreadsheet, service, 'player', "FanDuel!AR1")

        #############################################################################

        result = self.writeToCell(spreadsheet, service, 'Actual_Points', 'H1')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        g.log.info('Copy Over points scored')
        result = self.writeToCell(spreadsheet, service,
                                    '=VLOOKUP(A2,{FanDuel!$AR$2:$AR$1000,FanDuel!$AS$2:$AS$1000},2,FALSE)', 'H2')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        self.copyFormula(spreadsheet, service, sheetId0, 7, 8)

        result = self.writeToCell(spreadsheet, service, 'FanDuel_Salary', 'I1')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        g.log.info('Copy over Salary')
        result = self.writeToCell(spreadsheet, service,
                                    '=VLOOKUP(A2,{FanDuel!$AR$2:$AR$1000,FanDuel!$AV$2:$AV$1000},2,FALSE)', 'I2')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        self.copyFormula(spreadsheet, service, sheetId0, 8, 9)

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
