from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.sheets.prerequisite import PreReqs
from apiclient import discovery
import os.path
from os import path
import pyautogui
import pytest
import time
import webbrowser

class TestCreatePostGSheet:

    g.add_log(g.log, filename='./logs/post_Gsheets_create')


    @pytest.mark.post_gsheet
    def test_post_gsheet_create(self, deftestdata, print_logging):
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

        time.sleep(35)

        # TODO: Update for Rasberry Pi

        pyautogui.moveTo(1599, 696)
            #time.sleep(30)
        pyautogui.click()
        time.sleep(10)
        pyautogui.moveTo(1578, 241)
        pyautogui.click()
        time.sleep(2)

        pyautogui.moveTo(1700, 147)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(1741, 231)
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
        pyautogui.moveTo(2055, 571)
        pyautogui.click()
        time.sleep(20)
        pyautogui.moveTo(2149, 567)
        pyautogui.click()

        prereq.addCol(spreadsheet, service, sheetId1, 7, 8)
#
        result = prereq.writeToCell(spreadsheet, service, '=CONCATENATE(G2, D2, E2, " ", F2)', "FanDuel!H2")
#
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 7, 8)





        prereq.addCol(spreadsheet, service, sheetId1, 8, 9)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(H2, "Cleveland ", "Browns")', "FanDuel!I2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 8, 9)


        prereq.addCol(spreadsheet, service, sheetId1, 9, 10)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(I2, "Arizona ", "Cardinals")', "FanDuel!J2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 9, 10)

        prereq.addCol(spreadsheet, service, sheetId1, 10, 11)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(J2, "NewYork J", "Jets")', "FanDuel!K2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 10, 11)

        #time.sleep(200)

        prereq.addCol(spreadsheet, service, sheetId1, 11, 12)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(K2, "Tampa Bay", "Buccaneers")', "FanDuel!L2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 11, 12)

        prereq.addCol(spreadsheet, service, sheetId1, 12, 13)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(L2, "Dallas ", "Cowboys")', "FanDuel!M2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 12, 13)

        prereq.addCol(spreadsheet, service, sheetId1, 13, 14)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(M2, "New England", "Patriots")', "FanDuel!N2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 13, 14)

        prereq.addCol(spreadsheet, service, sheetId1, 14, 15)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(N2, "Cincinnati ", "Bengals")', "FanDuel!O2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 14, 15)

        prereq.addCol(spreadsheet, service, sheetId1, 15, 16)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(O2, "Kansas City", "Chiefs")', "FanDuel!P2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 15, 16)

        prereq.addCol(spreadsheet, service, sheetId1, 16, 17)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(P2, "Philadelphia ", "Eagles")', "FanDuel!Q2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 16, 17)

        prereq.addCol(spreadsheet, service, sheetId1, 17, 18)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(Q2, "Pittsburgh ", "Steelers")', "FanDuel!R2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 17, 18)

        prereq.addCol(spreadsheet, service, sheetId1, 18, 19)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(R2, "Minnesota ", "Vikings")', "FanDuel!S2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 18, 19)

        prereq.addCol(spreadsheet, service, sheetId1, 19, 20)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(S2, "New Orleans", "Saints")', "FanDuel!T2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 19, 20)

        prereq.addCol(spreadsheet, service, sheetId1, 20, 21)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(T2, "Green Bay", "Packers")', "FanDuel!U2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 20, 21)

        prereq.addCol(spreadsheet, service, sheetId1, 21, 22)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(U2, "Houston ", "Texans")', "FanDuel!V2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 21, 22)

        prereq.addCol(spreadsheet, service, sheetId1, 22, 23)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(V2, "Atlanta ", "Falcons")', "FanDuel!W2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 22, 23)

        prereq.addCol(spreadsheet, service, sheetId1, 23, 24)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(W2, "Washington ", "Redskins")', "FanDuel!X2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 23, 24)

        time.sleep(100)

        prereq.addCol(spreadsheet, service, sheetId1, 24, 25)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(X2, "Carolina ", "Panthers")', "FanDuel!Y2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 24, 25)

        prereq.addCol(spreadsheet, service, sheetId1, 25, 26)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(Y2, "Seattle ", "Seahawks")', "FanDuel!Z2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 25, 26)

        prereq.addCol(spreadsheet, service, sheetId1, 26, 27)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(Z2, "LA Rams ", "Rams")', "FanDuel!AA2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 26, 27)

        prereq.addCol(spreadsheet, service, sheetId1, 27, 28)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AA2, "LA Chargers ", "Chargers")', "FanDuel!AB2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 27, 28)

        prereq.addCol(spreadsheet, service, sheetId1, 28, 29)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AB2, "Indianapolis ", "Colts")', "FanDuel!AC2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 28, 29)

        prereq.addCol(spreadsheet, service, sheetId1, 29, 30)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AC2, "Oakland ", "Raiders")', "FanDuel!AD2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 29, 30)

        prereq.addCol(spreadsheet, service, sheetId1, 30, 31)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AD2, "Jacksonville ", "Jaguars")', "FanDuel!AE2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 30, 31)

        prereq.addCol(spreadsheet, service, sheetId1, 31, 32)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AE2, "Detroit ", "Lions")', "FanDuel!AF2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 31, 32)

        prereq.addCol(spreadsheet, service, sheetId1, 32, 33)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AF2, "Buffalo ", "Bills")', "FanDuel!AG2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 32, 33)

        prereq.addCol(spreadsheet, service, sheetId1, 33, 34)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AG2, "NewYork G", "Giants")', "FanDuel!AH2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 33, 34)

        prereq.addCol(spreadsheet, service, sheetId1, 34, 35)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AH2, "Tennessee ", "Titans")', "FanDuel!AI2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 34, 35)

        prereq.addCol(spreadsheet, service, sheetId1, 35, 36)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AI2, "Chicago ", "Bears")', "FanDuel!AJ2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 35, 36)

        prereq.addCol(spreadsheet, service, sheetId1, 36, 37)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AJ2, "Miami ", "Dolphins")', "FanDuel!AK2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 36, 37)

        prereq.addCol(spreadsheet, service, sheetId1, 37, 38)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AK2, "Baltimore ", "Ravens")', "FanDuel!AL2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 37, 38)

        prereq.addCol(spreadsheet, service, sheetId1, 38, 39)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AL2, "San Francisco", "49ers")', "FanDuel!AM2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 38, 39)

        prereq.addCol(spreadsheet, service, sheetId1, 39, 40)

        result = prereq.writeToCell(spreadsheet, service, '=REGEXREPLACE(AM2, "Denver ", "Broncos")', "FanDuel!AN2")

        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId1, 39, 40)

        result = prereq.writeToCell(spreadsheet, service, 'player', "FanDuel!AN1")

        #############################################################################

        result = prereq.writeToCell(spreadsheet, service, 'FanDuel_Salary', 'I1')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

                                                        #'=IF(D2="DST", VLOOKUP(B2,{FanDuel!$E$2:$E$1000,FanDuel!$H$2:$H$1000},2,FALSE), VLOOKUP(B2,{FanDuel!$D$2:$D$1000,FanDuel!$H$2:$H$1000},2,FALSE))', 'I2')
        result = prereq.writeToCell(spreadsheet, service, '=VLOOKUP(B2,{FanDuel!$AN$2:$AN$1000,FanDuel!$AR$2:$AR$1000},2,FALSE)', 'I2')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheet, service, sheetId0, 8, 9)

        # Rename to Actual_Points bc this is what my code looks for
        result = prereq.writeToCell(spreadsheet, service, 'Actual_Points', "H1")
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        ###################################################################################

        # Code to update using the actual points from fanduel tab.
        result = prereq.writeToCell(spreadsheetId, service, '=VLOOKUP(B2,{FanDuel!$AN$2:$AN$1000,FanDuel!$AO$2:$AO$1000},2,FALSE)', 'H2')
        g.log.info('{0} cells updated.'.format(result.get('updatedCells')))

        prereq.copyFormula(spreadsheetId, service, sheetId0, 7, 8)