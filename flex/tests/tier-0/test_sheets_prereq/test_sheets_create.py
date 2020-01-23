from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.sheets.prerequisite import PreReqs
from apiclient import discovery
#from schema import Schema, And, Use, Optional
import os.path
from os import path
import pyautogui
import pytest
import time
import webbrowser

class TestSheetsCreate:

    g.add_log(g.log, filename='./logs/sheets_create')


    @pytest.mark.create_sheet
    def test_create_sheet(self, print_logging):
        """
        #Test that we can read a sheet using the credential object
        #:return:
        """
        #self.spreadsheetId = deftestdata['spreadsheetId']
        #self.rangeName = deftestdata['rangeName']

        g.log.info('Instantiate SheetsConnector object')
        FLEX = SheetsConnector()
        g.log.info('Get Credentials')
        credentials = FLEX.get_credentials()

        g.log.info('Instantiate Prereqs')
        prereq = PreReqs()
        g.log.info('create New sheet')
        prereq.createNewSheet(credentials, '2019 Week2 STD')

        #gsc = SheetsConnector(self.spreadsheetId, self.rangeName)

        #g.log.info('Read from Google sheet')
        #result = gsc.rd_sheet()

        #g.log.info('Print data type of Google sheet class object')
        #g.log.info(type(result))

        #assert isinstance(result, dict)

        # TODO: ADD functions to remove Le'veon bell issue
        # TODO: Group the common pieces into a function
        # TODO: should be creation and data slicing, then the pyauto gui can be put into a function, then
        # the last part too I bet

    @pytest.mark.import_data
    def test_import_data(self, deftestdata, print_logging):
        """
        #Test that we can read a sheet using the credential object
        #:return:
        """
        projections = deftestdata['projections']
        FanDuel_Salaries = deftestdata['FanDuel_Salaries']
        Sheet_Name = deftestdata['Sheet_Name']

        g.log.info('Instantiate SheetsConnector object')
        FLEX = SheetsConnector()
        g.log.info('Get Credentials')
        credentials = FLEX.get_credentials()

        g.log.info('Instantiate Prereqs')
        prereq = PreReqs()
        g.log.info('create New sheet')
        spreadsheet, service = prereq.createNewSheet(credentials, Sheet_Name)

        g.log.info('Instantiate Prereqs')
        prereq = PreReqs()
        g.log.info('Upload Data')
        #spreadsheetId = deftestdata['spreadsheetId']
        prereq.importData(credentials, spreadsheet, projections)

        prereq.addTab(spreadsheet, service, 'FanDuel')

        prereq.importSpecificTabData(credentials, spreadsheet, 'FanDuel', FanDuel_Salaries)

        sheetId0 = prereq.gatherFacts(spreadsheet, service, 0)
        sheetId1 = prereq.gatherFacts(spreadsheet, service, 1)

        #================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 5, 6)

        result = prereq.writeToCell(spreadsheet, service, 'w/o quote', "FanDuel!F1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(D2, "\'","")', "FanDuel!F2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 5, 6)

        # ================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 6, 7)

        result = prereq.writeToCell(spreadsheet, service, 'w/o II', "FanDuel!G1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(F2, " III","")', "FanDuel!G2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 6, 7)

        # ================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 7, 8)

        result = prereq.writeToCell(spreadsheet, service, 'w/o Jr', "FanDuel!H1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(G2, " Jr.","")', "FanDuel!H2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 7, 8)

        # ================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 8, 9)

        result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!I1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(H2, "DJ","D.J.")', "FanDuel!I2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 8, 9)
        #=================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 9, 10)

        result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!J1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(I2, " II","")', "FanDuel!J2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 9, 10)
        #=================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 10, 11)

        result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!K1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(J2, " V","")', "FanDuel!K2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 10, 11)



        #=================================================
        g.log.info('Start removing Punctuation')
        prereq.addCol(spreadsheet, service, sheetId1, 11, 12)

        result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!L1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=IF (OR(S2="IR", S2="D", S2="O", AND(S2="Q", B2<>"QB")), "#N/A", K2)', "FanDuel!L2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 11, 12)


        # =REGEXREPLACE(D41, "Jr.","")
        # =REGEXREPLACE(D133, " Jr.","")
        # =REGEXREPLACE(D219, "DJ","D.J.")


        prereq.addCol(spreadsheet, service, sheetId0, 8, 9)

        result = prereq.writeToCell(spreadsheet, service, 'FanDuel_Salary', 'I1')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

                                                        #'=IF(D2="DST", VLOOKUP(B2,{FanDuel!$E$2:$E$1000,FanDuel!$H$2:$H$1000},2,FALSE), VLOOKUP(B2,{FanDuel!$D$2:$D$1000,FanDuel!$H$2:$H$1000},2,FALSE))', 'I2')
        result = prereq.writeToCell(spreadsheet, service, '=IF(D2="DST", VLOOKUP(B2,{FanDuel!$E$2:$E$1000,FanDuel!$O$2:$O$1000},2,FALSE), VLOOKUP(B2,{FanDuel!$L$2:$L$1000,FanDuel!$O$2:$O$1000},2,FALSE))', 'I2')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId0, 8, 9)

        # Rename to Actual_Points bc this is what my code looks for
        result = prereq.writeToCell(spreadsheet, service, 'Actual_Points', "H1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))



        # TODO: ADD functions to remove Le'veon bell issue
        # TODO: Group the common pieces into a function
        # TODO: should be creation and data slicing, then the pyauto gui can be put into a function, then
        # the last part too I bet

    @pytest.mark.create_17_18_gsheet
    def test_import_historic_data(self, deftestdata, print_logging):
        """
        #Test that we can read a sheet using the credential object
        #:return:
        """
        projections = deftestdata['projections']
        FanDuel_Salaries = deftestdata['FanDuel_Salaries']
        Sheet_Name = deftestdata['Sheet_Name']

        g.log.info('Instantiate SheetsConnector object')
        FLEX = SheetsConnector()
        g.log.info('Get Credentials')
        credentials = FLEX.get_credentials()

        g.log.info('Instantiate Prereqs')
        prereq = PreReqs()
        g.log.info('create New sheet')
        spreadsheet, service = prereq.createNewSheet(credentials, Sheet_Name)

        g.log.info('Instantiate Prereqs')
        prereq = PreReqs()
        g.log.info('Upload Data')
        # spreadsheetId = deftestdata['spreadsheetId']
        prereq.importData(credentials, spreadsheet, projections)

        prereq.addTab(spreadsheet, service, 'FanDuel')

        prereq.importSpecificTabData(credentials, spreadsheet, 'FanDuel', FanDuel_Salaries)

        sheetId0 = prereq.gatherFacts(spreadsheet, service, 0)
        sheetId1 = prereq.gatherFacts(spreadsheet, service, 1)

        # ================================================
        g.log.info('Start removing $$$s')
        #prereq.addCol(spreadsheet, service, sheetId1, 3, 4)

        result = prereq.writeToCell(spreadsheet, service, 'pre_Salary', "FanDuel!E1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(TO_TEXT(D2), "\$","")', "FanDuel!E2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 4, 5)

        result = prereq.writeToCell(spreadsheet, service, 'Salary', "FanDuel!F1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(E2, "\,","")', "FanDuel!F2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 5, 6)

        # I will do player name data cleaning at the end of the spreadsheet. This will be in the 'AT' and on column range
        # This is the best way to use what I currently have which is working.

        # prereq.addCol(spreadsheet, service, sheetId1, 46, 47)
        #
        # result = prereq.writeToCell(spreadsheet, service, 'Player', "FanDuel!C1")
        # g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        # result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(B2, " E.J."," EJ")', "FanDuel!AT2")
        # g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        # #
        # prereq.copyFormula(spreadsheet, service, sheetId1, 46, 47)


        prereq.addCol(spreadsheet, service, sheetId1, 2, 3)

        result = prereq.writeToCell(spreadsheet, service, 'Player', "FanDuel!C1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(B2, " Jr.","")', "FanDuel!C2")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 2, 3)

        a_website = 'https://docs.google.com/spreadsheets/d/%s' % spreadsheet

        # Open url in a new window of the default browser, if possible
        webbrowser.open_new(a_website)
            # username = deftestdata['username']
            # password = deftestdata['password']
            # full_path_filename = deftestdata['full_path_filename']
#            spreadsheetID = deftestdata['full_path_filename']

        time.sleep(55)
        # Click on FanDuel tab
        pyautogui.moveTo(1586, 192)
        pyautogui.click()

        time.sleep(20)

        pyautogui.moveTo(366, 1173)
            #time.sleep(30)
        pyautogui.click()
        time.sleep(10)
        pyautogui.moveTo(295, 307)
        pyautogui.click()
        time.sleep(2)

        pyautogui.moveTo(417, 213)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(474, 297)
        pyautogui.click()
        time.sleep(2)
        #pyautogui.moveTo(1271, 691)
        pyautogui.click()
        time.sleep(5)
        pyautogui.press('down')
        time.sleep(5)

        pyautogui.press('enter')

        time.sleep(5)



        pyautogui.press('enter')
        # Click start in add on
        # pyautogui.moveTo(1664, 394)
        # pyautogui.click()
        time.sleep(30)

        # start of right to the source
        pyautogui.moveTo(934, 845)
        pyautogui.click()
        time.sleep(20)
        pyautogui.moveTo(1029, 847)
        pyautogui.click()

        prereq.addCol(spreadsheet, service, sheetId1, 9, 10)

        result = prereq.writeToCell(spreadsheet, service, '=CONCATENATE(I2, F2, G2, " ", H2)', "FanDuel!J2")
        g.log.info('Concatenating split player names')
        g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 9, 10)


        #time.sleep(200)
        #######################################
        # Code to map team cities to team name
        #######################################

        # prereq.addCol(spreadsheet, service, sheetId1, 7, 8)
        #
        # result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(G2, "Denver Defense", "Broncos")', "FanDuel!H2")
        #
        # g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        # #
        # prereq.copyFormula(spreadsheet, service, sheetId1, 7, 8)





        prereq.addCol(spreadsheet, service, sheetId1, 8, 9)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(H2, "Cleveland ", "Browns")', "FanDuel!I2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 8, 9)


        prereq.addCol(spreadsheet, service, sheetId1, 9, 10)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(I2, "Arizona ", "Cardinals")', "FanDuel!J2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 9, 10)

        prereq.addCol(spreadsheet, service, sheetId1, 10, 11)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(J2, "NewYork J", "Jets")', "FanDuel!K2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 10, 11)

        #time.sleep(200)

        prereq.addCol(spreadsheet, service, sheetId1, 11, 12)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(K2, "Tampa Bay", "Buccaneers")', "FanDuel!L2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 11, 12)

        prereq.addCol(spreadsheet, service, sheetId1, 12, 13)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(L2, "Dallas ", "Cowboys")', "FanDuel!M2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 12, 13)

        prereq.addCol(spreadsheet, service, sheetId1, 13, 14)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(M2, "New England", "Patriots")', "FanDuel!N2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 13, 14)

        prereq.addCol(spreadsheet, service, sheetId1, 14, 15)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(N2, "Cincinnati ", "Bengals")', "FanDuel!O2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 14, 15)

        prereq.addCol(spreadsheet, service, sheetId1, 15, 16)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(O2, "Kansas City", "Chiefs")', "FanDuel!P2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 15, 16)

        prereq.addCol(spreadsheet, service, sheetId1, 16, 17)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(P2, "Philadelphia ", "Eagles")', "FanDuel!Q2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 16, 17)

        prereq.addCol(spreadsheet, service, sheetId1, 17, 18)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(Q2, "Pittsburgh ", "Steelers")', "FanDuel!R2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 17, 18)

        prereq.addCol(spreadsheet, service, sheetId1, 18, 19)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(R2, "Minnesota ", "Vikings")', "FanDuel!S2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 18, 19)

        prereq.addCol(spreadsheet, service, sheetId1, 19, 20)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(S2, "New Orleans", "Saints")', "FanDuel!T2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 19, 20)

        prereq.addCol(spreadsheet, service, sheetId1, 20, 21)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(T2, "Green Bay", "Packers")', "FanDuel!U2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 20, 21)

        prereq.addCol(spreadsheet, service, sheetId1, 21, 22)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(U2, "Houston ", "Texans")', "FanDuel!V2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 21, 22)

        prereq.addCol(spreadsheet, service, sheetId1, 22, 23)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(V2, "Atlanta ", "Falcons")', "FanDuel!W2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 22, 23)

        prereq.addCol(spreadsheet, service, sheetId1, 23, 24)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(W2, "Washington ", "Redskins")', "FanDuel!X2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 23, 24)

        time.sleep(100)

        prereq.addCol(spreadsheet, service, sheetId1, 24, 25)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(X2, "Carolina ", "Panthers")', "FanDuel!Y2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 24, 25)

        prereq.addCol(spreadsheet, service, sheetId1, 25, 26)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(Y2, "Seattle ", "Seahawks")', "FanDuel!Z2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 25, 26)

        prereq.addCol(spreadsheet, service, sheetId1, 26, 27)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(Z2, "LA Rams ", "Rams")', "FanDuel!AA2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 26, 27)

        prereq.addCol(spreadsheet, service, sheetId1, 27, 28)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AA2, "LA Chargers ", "Chargers")', "FanDuel!AB2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 27, 28)

        prereq.addCol(spreadsheet, service, sheetId1, 28, 29)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AB2, "Indianapolis ", "Colts")', "FanDuel!AC2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 28, 29)

        prereq.addCol(spreadsheet, service, sheetId1, 29, 30)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AC2, "Oakland ", "Raiders")', "FanDuel!AD2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 29, 30)

        prereq.addCol(spreadsheet, service, sheetId1, 30, 31)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AD2, "Jacksonville ", "Jaguars")', "FanDuel!AE2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 30, 31)

        prereq.addCol(spreadsheet, service, sheetId1, 31, 32)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AE2, "Detroit ", "Lions")', "FanDuel!AF2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 31, 32)

        # prereq.addCol(spreadsheet, service, sheetId1, 32, 33)
        #
        # result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AF2, "Detroit  Defense", "Lions")', "FanDuel!AG2")
        #
        # g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        # #
        # prereq.copyFormula(spreadsheet, service, sheetId1, 32, 33)

        prereq.addCol(spreadsheet, service, sheetId1, 32, 33)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AF2, "Buffalo ", "Bills")', "FanDuel!AG2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 32, 33)

        prereq.addCol(spreadsheet, service, sheetId1, 33, 34)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AG2, "NewYork G", "Giants")', "FanDuel!AH2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 33, 34)

        prereq.addCol(spreadsheet, service, sheetId1, 34, 35)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AH2, "Tennessee ", "Titans")', "FanDuel!AI2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 34, 35)

        prereq.addCol(spreadsheet, service, sheetId1, 35, 36)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AI2, "Chicago ", "Bears")', "FanDuel!AJ2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 35, 36)

        prereq.addCol(spreadsheet, service, sheetId1, 36, 37)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AJ2, "Miami ", "Dolphins")', "FanDuel!AK2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 36, 37)

        prereq.addCol(spreadsheet, service, sheetId1, 37, 38)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AK2, "Baltimore ", "Ravens")', "FanDuel!AL2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 37, 38)

        prereq.addCol(spreadsheet, service, sheetId1, 38, 39)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AL2, "San Francisco", "49ers")', "FanDuel!AM2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 38, 39)

        prereq.addCol(spreadsheet, service, sheetId1, 39, 40)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AM2, "Denver ", "Broncos")', "FanDuel!AN2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
        #
        prereq.copyFormula(spreadsheet, service, sheetId1, 39, 40)

        result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!AN1")

        #############################################################################

        #=VLOOKUP(B2, {FanDuel!$AN$2:$AN$1000, FanDuel!$AO$2:$AO$1000}, 2, FALSE)
        result = prereq.writeToCell(spreadsheet, service, 'Actual_Points', 'H1')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        g.log.info('Copy Over points scored')
        result = prereq.writeToCell(spreadsheet, service, '=VLOOKUP(B2,{FanDuel!$AN$2:$AN$1000,FanDuel!$AR$2:$AR$1000},2,FALSE)', 'H2')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId0, 8, 9)

        result = prereq.writeToCell(spreadsheet, service, 'FanDuel_Salary', 'I1')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

                                                        #'=IF(D2="DST", VLOOKUP(B2,{FanDuel!$E$2:$E$1000,FanDuel!$H$2:$H$1000},2,FALSE), VLOOKUP(B2,{FanDuel!$D$2:$D$1000,FanDuel!$H$2:$H$1000},2,FALSE))', 'I2')
        g.log.info('Copy over Salary')
        result = prereq.writeToCell(spreadsheet, service, '=VLOOKUP(B2,{FanDuel!$AN$2:$AN$1000,FanDuel!$AU$2:$AU$1000},2,FALSE)', 'I2')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId0, 8, 9)

        # Rename to Actual_Points bc this is what my code looks for
        result = prereq.writeToCell(spreadsheet, service, 'Actual_Points', "H1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        #prereq.rmCol(spreadsheet, service, sheetId1, 1, 2)

    @pytest.mark.sht_pretest
    def test_sheet_pre_test(self, shtCreatePreReq, print_logging):
        """
        This test is meant to test the fixture sht_create_pretest
        Which is meant to be a common way to create the base of all
        of our google sheets and start to correct naming convention.
        :param self:
        :param deftestdata:
        :param print_logging:
        :return:
        """

        g.log.info('Instantiate the spreadsheet object')
        spreadsheet = shtCreatePreReq
        g.log.info(spreadsheet)

    @pytest.mark.create_15_16_gsheet
    def test_import_historic_data(self, shtCreatePreReq, deftestdata, print_logging):
            """
            Creates google sheet for 2015 to 2016 season,
            :return:
            """
            g.log.info('Instantiate the spreadsheet object')
            spreadsheet, service, sheetId0, sheetId1 = shtCreatePreReq
            g.log.info(spreadsheet)

            # TODO: wrap this code below in a function.
            time.sleep(60)
            # a_website = 'https://docs.google.com/spreadsheets/d/%s' % spreadsheet
            #
            # # Open url in a new window of the default browser, if possible
            # webbrowser.open_new(a_website)
            # # username = deftestdata['username']
            # # password = deftestdata['password']
            # # full_path_filename = deftestdata['full_path_filename']
            # #            spreadsheetID = deftestdata['full_path_filename']
            #
            # time.sleep(55)
            # # Click on FanDuel tab
            # pyautogui.moveTo(1586, 192)
            # pyautogui.click()
            #
            # time.sleep(20)
            #
            # pyautogui.moveTo(366, 1173)
            # # time.sleep(30)
            # pyautogui.click()
            # time.sleep(10)
            # pyautogui.moveTo(295, 307)
            # pyautogui.click()
            # time.sleep(2)
            #
            # pyautogui.moveTo(417, 213)
            # pyautogui.click()
            # time.sleep(2)
            # pyautogui.moveTo(474, 297)
            # pyautogui.click()
            # time.sleep(2)
            # # pyautogui.moveTo(1271, 691)
            # pyautogui.click()
            # time.sleep(5)
            # pyautogui.press('down')
            # time.sleep(5)
            #
            # pyautogui.press('enter')
            #
            # time.sleep(5)
            #
            # pyautogui.press('enter')
            # # Click start in add on
            # # pyautogui.moveTo(1664, 394)
            # # pyautogui.click()
            # time.sleep(30)
            #
            # # start of right to the source
            # pyautogui.moveTo(934, 845)
            # pyautogui.click()
            # time.sleep(20)
            # pyautogui.moveTo(1029, 847)
            # pyautogui.click()

            #g.log.info('Instantiate SheetsConnector object')
            #FLEX = SheetsConnector()

            g.log.info('Instantiate Prereqs')
            prereq = PreReqs()

            prereq.addCol(spreadsheet, service, sheetId1, 11, 12)

            result = prereq.writeToCell(spreadsheet, service, '=CONCATENATE(K2, H2, I2, " ", J2)', "FanDuel!L2")
            g.log.info('Concatenating split player names')
            g.log.info('{0} cell(s) updated.'.format(result.get('updatedCells')))

            prereq.copyFormula(spreadsheet, service, sheetId1, 11, 12)

            # time.sleep(200)
            #
            # prereq.addCol(spreadsheet, service, sheetId1, 7, 8)
            # #
            # result = prereq.writeToCell(spreadsheet, service, '=CONCATENATE(G2, D2, E2, " ", F2)', "FanDuel!H2")
            # #
            # g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            # # #
            # prereq.copyFormula(spreadsheet, service, sheetId1, 7, 8)

            # time.sleep(200)
            #######################################
            # Code to map team cities to team name
            #######################################

            # prereq.addCol(spreadsheet, service, sheetId1, 10, 11)
            #
            # result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(J2, "Denver Defense", "Broncos")',
            #                             "FanDuel!K2")
            #
            # g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            # prereq.copyFormula(spreadsheet, service, sheetId1, 10, 11)

            # prereq.addCol(spreadsheet, service, sheetId1, 11, 12)
            #
            # result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(K2, "Cleveland Defense", "Browns")',
            #                             "FanDuel!L2")
            #
            # g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            # #
            # prereq.copyFormula(spreadsheet, service, sheetId1, 11, 12)

            prereq.addCol(spreadsheet, service, sheetId1, 12, 13)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(L2, "Arizona Defense", "Cardinals")',
                                        "FanDuel!M2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 12, 13)

            prereq.addCol(spreadsheet, service, sheetId1, 13, 14)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(M2, "New York J Defense", "Jets")',
                                        "FanDuel!N2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 13, 14)

            prereq.addCol(spreadsheet, service, sheetId1, 14, 15)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(N2, "Tampa Bay Defense", "Buccaneers")',
                                        "FanDuel!O2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 14, 15)

            prereq.addCol(spreadsheet, service, sheetId1, 15, 16)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(O2, "Dallas Defense", "Cowboys")',
                                        "FanDuel!P2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 15, 16)

            prereq.addCol(spreadsheet, service, sheetId1, 16, 17)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(P2, "New England Defense", "Patriots")',
                                        "FanDuel!Q2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 16, 17)

            prereq.addCol(spreadsheet, service, sheetId1, 17, 18)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(Q2, "Cincinnati Defense", "Bengals")',
                                        "FanDuel!R2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 17, 18)

            prereq.addCol(spreadsheet, service, sheetId1, 18, 19)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(R2, "Kansas City Defense", "Chiefs")',
                                        "FanDuel!S2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 18, 19)

            prereq.addCol(spreadsheet, service, sheetId1, 19, 20)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(S2, "Philadelphia", "Eagles")',
                                        "FanDuel!T2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 19, 20)

            prereq.addCol(spreadsheet, service, sheetId1, 20, 21)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(T2, "Pittsburgh", "Steelers")',
                                        "FanDuel!U2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 20, 21)

            prereq.addCol(spreadsheet, service, sheetId1, 21, 22)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(U2, "Minnesota Defense", "Vikings")',
                                        "FanDuel!V2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 21, 22)

            prereq.addCol(spreadsheet, service, sheetId1, 22, 23)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(V2, "New Orleans Defense", "Saints")',
                                        "FanDuel!W2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 22, 23)

            prereq.addCol(spreadsheet, service, sheetId1, 23, 24)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(W2, "Green Bay Defense", "Packers")',
                                        "FanDuel!X2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 23, 24)

            prereq.addCol(spreadsheet, service, sheetId1, 24, 25)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(X2, "Houston Defense", "Texans")',
                                        "FanDuel!Y2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 24, 25)

            prereq.addCol(spreadsheet, service, sheetId1, 25, 26)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(Y2, "Atlanta Defense", "Falcons")',
                                        "FanDuel!Z2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 25, 26)

            prereq.addCol(spreadsheet, service, sheetId1, 26, 27)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(Z2, "Washington Defense", "Redskins")',
                                        "FanDuel!AA2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 26, 27)

            time.sleep(100)

            prereq.addCol(spreadsheet, service, sheetId1, 27, 28)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AA2, "Carolina Defense", "Panthers")',
                                        "FanDuel!AB2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 27, 28)

            prereq.addCol(spreadsheet, service, sheetId1, 28, 29)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AB2, "Seattle Defense", "Seahawks")',
                                        "FanDuel!AC2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 28, 29)

            prereq.addCol(spreadsheet, service, sheetId1, 29, 30)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AC2, "LA Rams", "Rams")', "FanDuel!AD2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 29, 30)

            prereq.addCol(spreadsheet, service, sheetId1, 30, 31)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AD2, "San Diego Defense", "Chargers")',
                                        "FanDuel!AE2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 30, 31)

            prereq.addCol(spreadsheet, service, sheetId1, 31, 32)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AE2, "Indianapolis Defense", "Colts")',
                                        "FanDuel!AF2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 31, 32)

            prereq.addCol(spreadsheet, service, sheetId1, 32, 33)
            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AF2, "Oakland Defense", "Raiders")',
                                        "FanDuel!AG2")
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            prereq.copyFormula(spreadsheet, service, sheetId1, 32, 33)

            prereq.addCol(spreadsheet, service, sheetId1, 33, 34)
            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AG2, "Jacksonville Defense", "Jaguars")',
                                        "FanDuel!AH2")
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            prereq.copyFormula(spreadsheet, service, sheetId1, 33, 34)

            prereq.addCol(spreadsheet, service, sheetId1, 34, 35)
            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AH2, "Detroit", "Lions")', "FanDuel!AI2")
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            prereq.copyFormula(spreadsheet, service, sheetId1, 34, 35)

            prereq.addCol(spreadsheet, service, sheetId1, 35, 36)
            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AI2, "Detroit Defense", "Lions")',
                                        "FanDuel!AJ2")
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            prereq.copyFormula(spreadsheet, service, sheetId1, 35, 36)

            prereq.addCol(spreadsheet, service, sheetId1, 36, 37)
            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AJ2, "Buffalo Defense", "Bills")',
                                        "FanDuel!AK2")
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            prereq.copyFormula(spreadsheet, service, sheetId1, 36, 37)

            prereq.addCol(spreadsheet, service, sheetId1, 37, 38)
            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AK2, "New York G Defense", "Giants")',
                                        "FanDuel!AL2")
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            prereq.copyFormula(spreadsheet, service, sheetId1, 37, 38)

            prereq.addCol(spreadsheet, service, sheetId1, 38, 39)
            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AL2, "Tennessee Defense", "Titans")',
                                        "FanDuel!AM2")
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            prereq.copyFormula(spreadsheet, service, sheetId1, 38, 39)

            prereq.addCol(spreadsheet, service, sheetId1, 39, 40)
            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AM2, "Chicago Defense", "Bears")',
                                        "FanDuel!AN2")
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            prereq.copyFormula(spreadsheet, service, sheetId1, 39, 40)

            prereq.addCol(spreadsheet, service, sheetId1, 40, 41)
            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AN2, "Miami Defense", "Dolphins")',
                                        "FanDuel!AO2")
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            prereq.copyFormula(spreadsheet, service, sheetId1, 40, 41)

            prereq.addCol(spreadsheet, service, sheetId1, 41, 42)
            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AO2, "Baltimore Defense", "Ravens")',
                                        "FanDuel!AP2")
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            prereq.copyFormula(spreadsheet, service, sheetId1, 41, 42)

            prereq.addCol(spreadsheet, service, sheetId1, 42, 43)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AP2, "San Francisco Defense", "49ers")',
                                        "FanDuel!AQ2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

            prereq.copyFormula(spreadsheet, service, sheetId1, 42, 43)

            prereq.addCol(spreadsheet, service, sheetId1, 43, 44)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AQ2, "Denver Defense", "Broncos")',
                                        "FanDuel!AR2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

            prereq.copyFormula(spreadsheet, service, sheetId1, 43, 44)

            prereq.addCol(spreadsheet, service, sheetId1, 44, 45)

            result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AR2, "Cleveland Defense", "Browns")',
                                        "FanDuel!AS2")

            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            prereq.copyFormula(spreadsheet, service, sheetId1, 44, 45)

            result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!AS1")

            #############################################################################

            result = prereq.writeToCell(spreadsheet, service, 'Actual_Points', 'H1')
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

            g.log.info('Copy Over points scored')
            result = prereq.writeToCell(spreadsheet, service,
                                        '=VLOOKUP(B2,{FanDuel!$AS$2:$AS$1000,FanDuel!$AT$2:$AT$1000},2,FALSE)', 'H2')
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

            prereq.copyFormula(spreadsheet, service, sheetId0, 7, 8)

            result = prereq.writeToCell(spreadsheet, service, 'FanDuel_Salary', 'I1')
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

            # '=IF(D2="DST", VLOOKUP(B2,{FanDuel!$E$2:$E$1000,FanDuel!$H$2:$H$1000},2,FALSE), VLOOKUP(B2,{FanDuel!$D$2:$D$1000,FanDuel!$H$2:$H$1000},2,FALSE))', 'I2')
            g.log.info('Copy over Salary')
            result = prereq.writeToCell(spreadsheet, service,
                                        '=VLOOKUP(B2,{FanDuel!$AS$2:$AS$1000,FanDuel!$AW$2:$AW$1000},2,FALSE)', 'I2')
            g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

            prereq.copyFormula(spreadsheet, service, sheetId0, 8, 9)

            # Rename to Actual_Points bc this is what my code looks for
            # result = prereq.writeToCell(spreadsheet, service, 'Actual_Points', "H1")
            # g.log.info('{0} cells updated.'.format(result.get('updatedCells')))


            # result = prereq.writeToCell(spreadsheet, service, 'FanDuel_Salary', 'I1')
            # g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            # # '=IF(D2="DST", VLOOKUP(B2,{FanDuel!$E$2:$E$1000,FanDuel!$H$2:$H$1000},2,FALSE), VLOOKUP(B2,{FanDuel!$D$2:$D$1000,FanDuel!$H$2:$H$1000},2,FALSE))', 'I2')
            # result = prereq.writeToCell(spreadsheet, service,
            #                             '=VLOOKUP(B2,{FanDuel!$AQ$2:$AQ$1000,FanDuel!$AU$2:$AU$1000},2,FALSE)', 'I2')
            # g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            # prereq.copyFormula(spreadsheet, service, sheetId0, 8, 9)
            #
            # # Rename to Actual_Points bc this is what my code looks for
            # result = prereq.writeToCell(spreadsheet, service, 'Actual_Points', "H1")
            # g.log.info('{0} cells updated.'.format(result.get('updatedCells')))
            #
            # # prereq.rmCol(spreadsheet, service, sheetId1, 1, 2)
