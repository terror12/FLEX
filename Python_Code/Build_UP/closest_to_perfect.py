from __future__ import print_function
import httplib2
import os
import pandas as pd
import numba
import random
import numpy as np
# import profile
# import sys
from tqdm import tqdm
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import time
from D1x_Phase2 import Set1
from D1x_Phase2 import Set2
from D1x_Phase2 import Set3
from D1x_Phase2 import Set4
from D1x_Phase2 import Set5
from D1x_Phase2 import Set6
from D1x_Phase2 import Set7
from D1x_Phase2 import Set8

from Phase3 import Phase3Set1
from Phase3 import Phase3Set2
from Phase3 import Phase3Set3
from Phase3 import Phase3Set4
from Phase3 import Phase3Set5
from Phase3 import Phase3Set6
from Phase3 import Phase3Set7

from Phase4 import Phase4Set1
from Phase4 import Phase4Set2
from Phase4 import Phase4Set3
from Phase4 import Phase4Set4
from Phase4 import Phase4Set5
from Phase4 import Phase4Set6

from Phase5 import Phase5Set1
from Phase5 import Phase5Set2
from Phase5 import Phase5Set3
from Phase5 import Phase5Set4
from Phase5 import Phase5Set5

from Phase6 import Phase6Set1
from Phase6 import Phase6Set2
from Phase6 import Phase6Set3
from Phase6 import Phase6Set4

from Phase7 import Phase7Set1
from Phase7 import Phase7Set2
from Phase7 import Phase7Set3

from Phase8 import Phase8Set1
from Phase8 import Phase8Set2

#from D2x_Phase2 import D2xSet1
#from D2x_Phase2 import D2xSet2
#from D2x_Phase2 import D2xSet3
#from D2x_Phase2 import D2xSet4
#from D2x_Phase2 import D2xSet5
#from D2x_Phase2 import D2xSet6
#from D2x_Phase2 import D2xSet7
#from D2x_Phase2 import D2xSet8

from D3x import D3xSet1
from D3x import D3xSet2
from D3x import D3xSet3
from D3x import D3xSet4
from D3x import D3xSet5
from D3x import D3xSet6
from D3x import D3xSet7
from D3x import D3xSet8
from D3x import D3xSet9
from D3x import set_position_nums


# from line_profiler import LineProfiler
# import line_profiler
# import atexit


####
## IMPORTANT!!!
####
# You may have to uncomment this the first time you run a new google sheet and remove the -i file.py from
# Run --> Edit Configurations --> Interpreter Options
# try:
#    import argparse
#    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
# except ImportError:
#    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def check():
    pass

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


# Function that will take credentials from googlesheets and break up the sheet into dataframes RB,RB,WR,TE,K,DST.
def posDframe(spreadsheetId, rangeName):
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """

    credentials = get_credentials()
 #   print(credentials)
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    # 2015_week1
    #spreadsheetId = spreadsheetId #'1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4'
    #rangeName = rangeName #'A1:L537'
    # 2015_week2
    #spreadsheetId = '1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE'
    #rangeName = 'A1:L545'
    # 2015_week3
    #    spreadsheetId = '15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo'
    #    rangeName = 'A1:L534'
    # 2015_week4
    # spreadsheetId = '1zQrAsg8IUWNn-N-cWpi63xpyqMRvYJjvPoVL5CXhj74'
    # rangeName = 'A1:L491'
    # 2015_week5
    #    spreadsheetId = '1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L491'
    #    rangeName = 'A1:L491'
    # 2015_week6
    #    spreadsheetId = '1DCMUJigFCXhv6PTqQg0A60FncrUONHW3Y0ebJyYNg1o', 'A1:L474'
    #    rangeName = 'A1:L474'
    # 2015_week7
    #    spreadsheetId = '1HQkkgp12J8R9Sa7Te_qZKAJpoZf6dLdynPXYrlpqwcg', 'A1:L476'
    #    rangeName = 'A1:L476'
    # 2015_week8
    #    spreadsheetId = '11xsMM28Edz-TDN6zbmospqDHz_ACNj45-bRQk844Sjw', 'A1:L474'
    #    rangeName = 'A1:L474'
    # 2015_week9
    #    spreadsheetId = '1bblln58znQA8E0aUDEjCUZqYrvXjL5kd3zqOXxRMuhw', 'A1:L431'
    #    rangeName = 'A1:L431'
    # 2015_week10
    #    spreadsheetId = '1FaBKYPN8FXtzJg7bo1IvCzNDK2Rm96BjBubDfPYS2CU', 'A1:L486'
    #    rangeName = 'A1:L486'
    # 2015_week11
    #    spreadsheetId = '1SjXKGmrz9PkTHw4IKodWjfozYoSeaLo8P7BjxxuKDs4', 'A1:L472'
    #    rangeName = 'A1:L472'
    # 2015_week12
    #    spreadsheetId = '1R03RkTBQzAqEbkczLz5YWyVqdbdGdW3R_qGi5pPiUOY', 'A1:L525'
    #    rangeName = 'A1:L525'
    # 2015_week13
    #    spreadsheetId = '1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L522'
    #    rangeName = 'A1:L522'
    # 2015_week14
    #    spreadsheetId = '1U04TTYMKa4L5gToFGI5kIyWWTwg0eaYqPihEVDZTPi4', 'A1:L528'
    #    rangeName = 'A1:L528'
    # 2015_week15
    #    spreadsheetId = '166Aky6qfxab8EOOROGmuNYv2L9gRDdOGRTgWw-zD3ug', 'A1:L522'
    #    rangeName = 'A1:L522'
    # 2015_week16
    #    spreadsheetId = '1wJs8S0eSFWCV7Y26yHUFkoEl8dUUqUpUP6OIkwxd3xs', 'A1:L514'
    #    rangeName = 'A1:L514'
    # 2015_week17
    #    spreadsheetId = '1r4dA1J6GtkzJMXIjhX24hbVViQAoyCGHB0uBaO64JaQ', 'A1:L508'
    #    rangeName = 'A1:L508'

    # 2016_week1
    #   spreadsheetId = '1BwJaBTGZ4UzsUoOgpgstCTQ7h0Go_D35GjwIo6Zip-Y', 'A1:L537'
    #   rangeName = 'A1:L537'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    # Turns Googlesheet data into DataFrame and seperates just the values
    adam = pd.DataFrame(result['values'])

    return adam

#def posDframe2():
#    credentials = get_credentials()
#    http = credentials.authorize(httplib2.Http())
#    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
#                    'version=v4')
#    service = discovery.build('sheets', 'v4', http=http,
#                              discoveryServiceUrl=discoveryUrl)
#
#    # 2015_week2
#    spreadsheetId = '1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE'
#    rangeName = 'A1:L545'
#    result = service.spreadsheets().values().get(
#        spreadsheetId=spreadsheetId, range=rangeName).execute()
#    values = result.get('values', [])
#
#    # Turns Googlesheet data into DataFrame and seperates just the values
#    adam = pd.DataFrame(result['values'])
#
#    return adam
#
#def posDframe3():
#    """Shows basic usage of the Sheets API.
#
#    Creates a Sheets API service object and prints the names and majors of
#    students in a sample spreadsheet:
#    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
#    """
#
#    credentials = get_credentials()
#    http = credentials.authorize(httplib2.Http())
#    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
#                    'version=v4')
#    service = discovery.build('sheets', 'v4', http=http,
#                              discoveryServiceUrl=discoveryUrl)
#
#    # 2015_week3
#    spreadsheetId = '15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo'
#    rangeName = 'A1:L534'
#    result = service.spreadsheets().values().get(
#        spreadsheetId=spreadsheetId, range=rangeName).execute()
#    values = result.get('values', [])
#
#    # Turns Googlesheet data into DataFrame and seperates just the values
#    adam = pd.DataFrame(result['values'])
#
#    return adam
#
#def posDframe4():
#    """Shows basic usage of the Sheets API.
#
#    Creates a Sheets API service object and prints the names and majors of
#    students in a sample spreadsheet:
#    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
#    """
#
#    credentials = get_credentials()
#    http = credentials.authorize(httplib2.Http())
#    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
#                    'version=v4')
#    service = discovery.build('sheets', 'v4', http=http,
#                              discoveryServiceUrl=discoveryUrl)
#
#    # 2015_week4
#    spreadsheetId = '1zQrAsg8IUWNn-N-cWpi63xpyqMRvYJjvPoVL5CXhj74'
#    rangeName = 'A1:L491'
#    result = service.spreadsheets().values().get(
#        spreadsheetId=spreadsheetId, range=rangeName).execute()
#    values = result.get('values', [])
#
#    # Turns Googlesheet data into DataFrame and seperates just the values
#    adam = pd.DataFrame(result['values'])
#
#    return adam
#
#def posDframe5():
#    """Shows basic usage of the Sheets API.
#
#    Creates a Sheets API service object and prints the names and majors of
#    students in a sample spreadsheet:
#    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
#    """
#
#    credentials = get_credentials()
#    http = credentials.authorize(httplib2.Http())
#    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
#                    'version=v4')
#    service = discovery.build('sheets', 'v4', http=http,
#                              discoveryServiceUrl=discoveryUrl)
#
#    # 2015_week5
#    spreadsheetId = '1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE'
#    rangeName = 'A1:L491'
#    result = service.spreadsheets().values().get(
#        spreadsheetId=spreadsheetId, range=rangeName).execute()
#    values = result.get('values', [])
#
#    # Turns Googlesheet data into DataFrame and seperates just the values
#    adam = pd.DataFrame(result['values'])
#
#    return adam

def Data_clean(spreadsheetId, rangeName):
    adam = posDframe(spreadsheetId, rangeName)
#    print(adam)
    # Set column labels to equal values in the 1st row
    adam.columns = adam.iloc[0]
    adam = adam[1:]

    # remove columns that I do not need
    adam = adam[['player', 'team', 'position', 'Actual_Points', 'FanDuel_Salary', 'Platform_AVG', 'STD']]

    # Removes all free agents
    adam = adam[adam.team != "FA"]
    # print(len(adam))

    # Create dataframe of just QBS
    QB = adam.loc[adam['position'] == 'QB']

    # Create dataframe of just QBS
    RB = adam.loc[adam['position'] == 'RB']

    # Create dataframe of just QBS
    WR = adam.loc[adam['position'] == 'WR']

    # Create dataframe of just QBS
    TE = adam.loc[adam['position'] == 'TE']

    # Create dataframe of just QBS
    K = adam.loc[adam['position'] == 'K']

    # Create dataframe of just QBS
    DST = adam.loc[adam['position'] == 'DST']

    #    print('QBs')
    #    print(len(QB))
    #    print('RBs')
    #    print(len(WR))
    #    print('WRs')
    #    print(len(RB))
    #    print('TEs')
    #    print(len(TE))
    #    print('Ks')
    #    print(len(K))
    #    print('DSTs')
    #    print(len(DST))

    return (QB, RB, WR, TE, K, DST)

    # create lineup of just the top position of each player


def removeNA(spreadsheetId, rangeName):
    QB, RB, WR, TE, K, DST = Data_clean(spreadsheetId, rangeName)
#    print(QB)
    QB = QB[QB.STD.str.contains("#N/A") == False]
    RB = RB[RB.STD.str.contains("#N/A") == False]
    WR = WR[WR.STD.str.contains("#N/A") == False]
    TE = TE[TE.STD.str.contains("#N/A") == False]
    K = K[K.STD.str.contains("#N/A") == False]
    DST = DST[DST.STD.str.contains("#N/A") == False]

    QB = QB[QB.Actual_Points.str.contains("#N/A") == False]
    RB = RB[RB.Actual_Points.str.contains("#N/A") == False]
    WR = WR[WR.Actual_Points.str.contains("#N/A") == False]
    TE = TE[TE.Actual_Points.str.contains("#N/A") == False]
    K = K[K.Actual_Points.str.contains("#N/A") == False]
    DST = DST[DST.Actual_Points.str.contains("#N/A") == False]

    #print(QB)
    #   print(len(QB))
    #   print('RBs')
    #   print(len(WR))
    #   print('WRs')
    #   print(len(RB))
    #   print('TEs')
    #   print(len(TE))
    #   print('Ks')
    #   print(len(K))
    #   print('DSTs')
    #   print(len(DST))

    return (QB, RB, WR, TE, K, DST)


def Roster_cut(spreadsheetId, rangeName):
    QB, RB, WR, TE, K, DST = removeNA(spreadsheetId, rangeName)

    QB = QB.sort_values('Platform_AVG', ascending=False).drop_duplicates('team').sort_index()

    TE = TE.sort_values(by=['Platform_AVG'], ascending=False)

    RB = RB[RB.Platform_AVG != '0']
    WR = WR[WR.Platform_AVG != '0']
    TE = TE[TE.Platform_AVG != '0']

    return (QB, RB, WR, TE, K, DST)


def removeLowProjections(spreadsheetId, rangeName):
    QB, RB, WR, TE, K, DST = Roster_cut(spreadsheetId, rangeName)
#    print(QB)
    QB['Platform_AVG'] = pd.to_numeric(QB['Platform_AVG'])
    RB['Platform_AVG'] = pd.to_numeric(RB['Platform_AVG'])
    WR['Platform_AVG'] = pd.to_numeric(WR['Platform_AVG'])
    TE['Platform_AVG'] = pd.to_numeric(TE['Platform_AVG'])
    K['Platform_AVG'] = pd.to_numeric(K['Platform_AVG'])
    DST['Platform_AVG'] = pd.to_numeric(DST['Platform_AVG'])

    QB['STD'] = pd.to_numeric(QB['STD'])
    RB['STD'] = pd.to_numeric(RB['STD'])
    WR['STD'] = pd.to_numeric(WR['STD'])
    TE['STD'] = pd.to_numeric(TE['STD'])
    K['STD'] = pd.to_numeric(K['STD'])
    DST['STD'] = pd.to_numeric(DST['STD'])

    # Add user input code!
    # To say type a players name from this list to add them to the large pool
    # logic will proly be just add 1.0 to the Platform_AVG of the players the user types in

    RB = RB[~(RB['Platform_AVG'] <= 1.0)]

    WR = WR[~(WR['Platform_AVG'] <= 1.0)]

    TE = TE[~(TE['Platform_AVG'] <= 1.0)]
#########################
#    print(QB)
#    print(WR)
#    print(TE)

    QB = QB[~(QB['STD'] >= 10.0)]
    RB = RB[~(RB['STD'] >= 10.0)]
    WR = WR[~(WR['STD'] >= 10.0)]
    TE = TE[~(TE['STD'] >= 10.0)]
    K = K[~(K['STD'] >= 10.0)]
    DST = DST[~(DST['STD'] >= 10.0)]
#    print(QB)
#    print(WR)
#    print(TE)
    # print('QBs')
    # print(len(QB))
    # print('RBs')
    # print(len(WR))
    # print('WRs')
    # print(len(RB))
    # print('TEs')
    # print(len(TE))
    # print('Ks')
    # print(len(K))
    # print('DSTs')
    # print(len(DST))

    return (QB, RB, WR, TE, K, DST)


def hitpositionLimits(spreadsheetId, rangeName):
    QB, RB, WR, TE, K, DST = removeLowProjections(spreadsheetId, rangeName)
    ##    QB = QB[['player', 'Actual_Points', 'FanDuel_Salary','Platform_AVG']]
 #   print(QB)
    if len(QB) > 35:
        QB = QB.sort_values(by=['Platform_AVG'], ascending=False)
        diff = (len(QB) - 35)
        QB = QB[:-diff]

    if len(DST) > 32:
        DST = DST.sort_values(by=['Platform_AVG'], ascending=False)
        diff = (len(DST) - 32)
        DST = DST[:-diff]

    if len(RB) > 150:
        RB = RB.sort_values(by=['Platform_AVG'], ascending=False)
        diff = (len(RB) - 150)
        RB = RB[:-diff]

    if len(WR) > 150:
        WR = WR.sort_values(by=['Platform_AVG'], ascending=False)
        diff = (len(WR) - 150)
        WR = WR[:-diff]

    if len(TE) > 90:
        TE = TE.sort_values(by=['Platform_AVG'], ascending=False)
        diff = (len(TE) - 90)
        TE = TE[:-diff]
    #    print('Hit Posisiton Limits')
    #    print('QBs')
    #    print(len(QB))
    #    print('RBs')
    #    print(len(WR))
    #    print('WRs')
    #    print(len(RB))
    #    print('TEs')
    #    print(len(TE))
    #    print('Ks')
#    print(QB)
#    print(WR)

    QB = QB.sort_values(by=['Actual_Points'], ascending=True)
#    print(QB)
    RB = RB.sort_values(by=['STD'], ascending=True)
    WR = WR.sort_values(by=['STD'], ascending=True)
    TE = TE.sort_values(by=['STD'], ascending=True)
    DST = DST.sort_values(by=['STD'], ascending=True)
#    print(QB)
    return (QB, RB, WR, TE, K, DST)


def useNeededCols(spreadsheetId, rangeName):
    QB, RB, WR, TE, K, DST = hitpositionLimits(spreadsheetId, rangeName)
#    print(QB)
    QB = QB[['player', 'team', 'Actual_Points', 'FanDuel_Salary', 'STD']]
    RB = RB[['player', 'team', 'Actual_Points', 'FanDuel_Salary', 'STD']]
    WR = WR[['player', 'team', 'Actual_Points', 'FanDuel_Salary', 'STD']]
    TE = TE[['player', 'team', 'Actual_Points', 'FanDuel_Salary', 'STD']]
    K = K[['player', 'team', 'Actual_Points', 'FanDuel_Salary', 'STD']]
    DST = DST[['player', 'team', 'Actual_Points', 'FanDuel_Salary', 'STD']]

    QB['Actual_Points'] = QB['Actual_Points'].astype('float')
    RB['Actual_Points'] = RB['Actual_Points'].astype('float')
    WR['Actual_Points'] = WR['Actual_Points'].astype('float')
    TE['Actual_Points'] = TE['Actual_Points'].astype('float')
    K['Actual_Points'] = K['Actual_Points'].astype('float')
    DST['Actual_Points'] = DST['Actual_Points'].astype('float')

#    QB['FanDuel_Salary'] = QB['FanDuel_Salary'].astype('float')
#    RB['FanDuel_Salary'] = RB['FanDuel_Salary'].astype('float')
#    WR['FanDuel_Salary'] = WR['FanDuel_Salary'].astype('float')
#    TE['FanDuel_Salary'] = TE['FanDuel_Salary'].astype('float')
#    K['FanDuel_Salary'] = K['FanDuel_Salary'].astype('float')
#    DST['FanDuel_Salary'] = DST['FanDuel_Salary'].astype('float')

    return (QB, RB, WR, TE, K, DST)

def order_for_perfect(spreadsheetId, rangeName):

    QB, RB, WR, TE, K, DST = useNeededCols(spreadsheetId, rangeName)

    QB = QB.values.tolist()
    RB = RB.values.tolist()
    WR = WR.values.tolist()
    TE = TE.values.tolist()
    K = K.values.tolist()
    DST = DST.values.tolist()

    QB.sort(key=lambda x: x[1], reverse=True)
    RB.sort(key=lambda x: x[1], reverse=True)
    WR.sort(key=lambda x: x[1], reverse=True)
    TE.sort(key=lambda x: x[1], reverse=True)
    K.sort(key=lambda x: x[1], reverse=True)
    DST.sort(key=lambda x: x[1], reverse=True)

    return (QB, RB, WR, TE, K, DST)

def helper_df_cleanup(spreadsheetId, rangeName):
    QB, RB, RB2, WR, WR2, WR3, TE, K, DST = display_closest(spreadsheetId, rangeName)

    QB['FanDuel_Salary'] = [s.replace(']],', '') for s in QB['FanDuel_Salary']]
    QB['FanDuel_Salary'] = [s.replace('\'', '') for s in QB['FanDuel_Salary']]
    QB['FanDuel_Salary'] = [s.replace(']', '') for s in QB['FanDuel_Salary']]
    QB['FanDuel_Salary'] = [s.replace(',', '') for s in QB['FanDuel_Salary']]
    QB['FanDuel_Salary'] = [float(i) for i in QB['FanDuel_Salary']]

    RB['FanDuel_Salary'] = [s.replace(']],', '') for s in RB['FanDuel_Salary']]
    RB['FanDuel_Salary'] = [s.replace('\'', '') for s in RB['FanDuel_Salary']]
    RB['FanDuel_Salary'] = [s.replace(']', '') for s in RB['FanDuel_Salary']]
    RB['FanDuel_Salary'] = [s.replace(',', '') for s in RB['FanDuel_Salary']]
    RB['FanDuel_Salary'] = [float(i) for i in RB['FanDuel_Salary']]

    RB2['FanDuel_Salary'] = [s.replace(']],', '') for s in RB2['FanDuel_Salary']]
    RB2['FanDuel_Salary'] = [s.replace('\'', '') for s in RB2['FanDuel_Salary']]
    RB2['FanDuel_Salary'] = [s.replace(']', '') for s in RB2['FanDuel_Salary']]
    RB2['FanDuel_Salary'] = [s.replace(',', '') for s in RB2['FanDuel_Salary']]
    RB2['FanDuel_Salary'] = [float(i) for i in RB2['FanDuel_Salary']]

    WR['FanDuel_Salary'] = [s.replace(']],', '') for s in WR['FanDuel_Salary']]
    WR['FanDuel_Salary'] = [s.replace('\'', '') for s in WR['FanDuel_Salary']]
    WR['FanDuel_Salary'] = [s.replace(']', '') for s in WR['FanDuel_Salary']]
    WR['FanDuel_Salary'] = [s.replace(',', '') for s in WR['FanDuel_Salary']]
    WR['FanDuel_Salary'] = [float(i) for i in WR['FanDuel_Salary']]

    WR2['FanDuel_Salary'] = [s.replace(']],', '') for s in WR2['FanDuel_Salary']]
    WR2['FanDuel_Salary'] = [s.replace('\'', '') for s in WR2['FanDuel_Salary']]
    WR2['FanDuel_Salary'] = [s.replace(']', '') for s in WR2['FanDuel_Salary']]
    WR2['FanDuel_Salary'] = [s.replace(',', '') for s in WR2['FanDuel_Salary']]
    WR2['FanDuel_Salary'] = [float(i) for i in WR2['FanDuel_Salary']]

    WR3['FanDuel_Salary'] = [s.replace(']],', '') for s in WR3['FanDuel_Salary']]
    WR3['FanDuel_Salary'] = [s.replace('\'', '') for s in WR3['FanDuel_Salary']]
    WR3['FanDuel_Salary'] = [s.replace(']', '') for s in WR3['FanDuel_Salary']]
    WR3['FanDuel_Salary'] = [s.replace(',', '') for s in WR3['FanDuel_Salary']]
    WR3['FanDuel_Salary'] = [float(i) for i in WR3['FanDuel_Salary']]

    TE['FanDuel_Salary'] = [s.replace(']],', '') for s in TE['FanDuel_Salary']]
    TE['FanDuel_Salary'] = [s.replace('\'', '') for s in TE['FanDuel_Salary']]
    TE['FanDuel_Salary'] = [s.replace(']', '') for s in TE['FanDuel_Salary']]
    TE['FanDuel_Salary'] = [s.replace(',', '') for s in TE['FanDuel_Salary']]
    TE['FanDuel_Salary'] = [float(i) for i in TE['FanDuel_Salary']]

    K['FanDuel_Salary'] = [s.replace(']],', '') for s in K['FanDuel_Salary']]
    K['FanDuel_Salary'] = [s.replace('\'', '') for s in K['FanDuel_Salary']]
    K['FanDuel_Salary'] = [s.replace(']', '') for s in K['FanDuel_Salary']]
    K['FanDuel_Salary'] = [s.replace(',', '') for s in K['FanDuel_Salary']]
    K['FanDuel_Salary'] = [float(i) for i in K['FanDuel_Salary']]

    DST['FanDuel_Salary'] = [s.replace(']],', '') for s in DST['FanDuel_Salary']]
    DST['FanDuel_Salary'] = [s.replace('\'', '') for s in DST['FanDuel_Salary']]
    DST['FanDuel_Salary'] = [s.replace(']', '') for s in DST['FanDuel_Salary']]
    DST['FanDuel_Salary'] = [s.replace(',', '') for s in DST['FanDuel_Salary']]
    DST['FanDuel_Salary'] = [float(i) for i in DST['FanDuel_Salary']]

    return(QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def display_closest(spreadsheetId, rangeName):

    #    global QB
#    global RB
#    global RB2
#    global WR
#    global WR2
#    global WR3
#    global TE
#    global K
#    global DST
#    global count
#    count = int(raw_input("> "))

    QB, RB, WR, TE, K, DST = useNeededCols(spreadsheetId, rangeName)

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
#    print(QBclosest)
    QBposition = (QBSTD.index(QBclosest))
#    print(QBposition)

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
#    print(RBclosest)
    RB1position = (RBSTD.index(RBclosest))
#    print(RB1position)

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
#    print(RB2closest)
    RB2position = (RB2STD.index(RB2closest))
#    print(RB2position)

    WRSTD = WR['STD']
    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
#    print(WRclosest)
    WR1position = (WRSTD.index(WRclosest))
#    print(WR1position)

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']
    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
#    print(WR2closest)
    WR2position = (WR2STD.index(WR2closest))
#    print(WR2position)

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
#    print(WR3closest)
    WR3position = (WR3STD.index(WR3closest))
#    print(WR3position)

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
#    print(TEclosest)
    TEposition = (TESTD.index(TEclosest))
#    print(TEposition)

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
#    print(Kclosest)
    Kposition = (KSTD.index(Kclosest))
#    print(Kposition)

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
 #      print(DSTclosest)
    DSTposition = (DSTSTD.index(DSTclosest))
#
#    return (QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

#    QB, RB, RB2, WR, WR2, WR3, TE, K, DST = helper_df_cleanup(spreadsheetId, rangeName)
 #       print(DSTposition)
#    else:
#        DSTSTD = DST['STD']
#        DSTSTD = DSTSTD.values.tolist()
#
#        DST_avg_std = 2.651650429611765
#        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
#        print(DSTclosest)
#        print('_______________+++++++++++++++++++__________________')
#        DSTposition = (DSTSTD.index(DSTclosest))
#        print(DSTposition)
#    else:
#        DSTSTD = DSTretry['STD']
#        # print(DST)
#        DSTSTD = DSTSTD.values.tolist()
#        #        print(DST)
#        DST_avg_std = 2.651650429611765
#        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
#        print(DSTclosest)
#        DSTposition = (DSTSTD.index(DSTclosest))
#        print(DSTposition)

 #   return (QBposition, RB1position, RB2position, WR1position, WR2position, WR3position, TEposition, Kposition, DSTposition, QBclosest, RBclosest, RB2closest, WRclosest, WR2closest, WR3closest, TEclosest, Kclosest, DSTclosest)

#def superline(spreadsheetId, rangeName):
#    QBposition, RB1position, RB2position, WR1position, WR2position, WR3position, TEposition, Kposition, DSTposition, QBclosest, RBclosest, RB2closest, WRclosest, WR2closest, WR3closest, TEclosest, Kclosest, DSTclosest  = display_closest(spreadsheetId, rangeName)
 #   print('superline===========================')
 #   print(DST)

#    print(QB)
    QB['FanDuel_Salary'] = [s.replace(']],', '') for s in QB['FanDuel_Salary']]
    QB['FanDuel_Salary'] = [s.replace('\'', '') for s in QB['FanDuel_Salary']]
    QB['FanDuel_Salary'] = [s.replace(']', '') for s in QB['FanDuel_Salary']]
    QB['FanDuel_Salary'] = [s.replace(',', '') for s in QB['FanDuel_Salary']]
    QB['FanDuel_Salary'] = [float(i) for i in QB['FanDuel_Salary']]

    RB['FanDuel_Salary'] = [s.replace(']],', '') for s in RB['FanDuel_Salary']]
    RB['FanDuel_Salary'] = [s.replace('\'', '') for s in RB['FanDuel_Salary']]
    RB['FanDuel_Salary'] = [s.replace(']', '') for s in RB['FanDuel_Salary']]
    RB['FanDuel_Salary'] = [s.replace(',', '') for s in RB['FanDuel_Salary']]
    RB['FanDuel_Salary'] = [float(i) for i in RB['FanDuel_Salary']]

    RB2['FanDuel_Salary'] = [s.replace(']],', '') for s in RB2['FanDuel_Salary']]
    RB2['FanDuel_Salary'] = [s.replace('\'', '') for s in RB2['FanDuel_Salary']]
    RB2['FanDuel_Salary'] = [s.replace(']', '') for s in RB2['FanDuel_Salary']]
    RB2['FanDuel_Salary'] = [s.replace(',', '') for s in RB2['FanDuel_Salary']]
    RB2['FanDuel_Salary'] = [float(i) for i in RB2['FanDuel_Salary']]

    WR['FanDuel_Salary'] = [s.replace(']],', '') for s in WR['FanDuel_Salary']]
    WR['FanDuel_Salary'] = [s.replace('\'', '') for s in WR['FanDuel_Salary']]
    WR['FanDuel_Salary'] = [s.replace(']', '') for s in WR['FanDuel_Salary']]
    WR['FanDuel_Salary'] = [s.replace(',', '') for s in WR['FanDuel_Salary']]
    WR['FanDuel_Salary'] = [float(i) for i in WR['FanDuel_Salary']]

    WR2['FanDuel_Salary'] = [s.replace(']],', '') for s in WR2['FanDuel_Salary']]
    WR2['FanDuel_Salary'] = [s.replace('\'', '') for s in WR2['FanDuel_Salary']]
    WR2['FanDuel_Salary'] = [s.replace(']', '') for s in WR2['FanDuel_Salary']]
    WR2['FanDuel_Salary'] = [s.replace(',', '') for s in WR2['FanDuel_Salary']]
    WR2['FanDuel_Salary'] = [float(i) for i in WR2['FanDuel_Salary']]

    WR3['FanDuel_Salary'] = [s.replace(']],', '') for s in WR3['FanDuel_Salary']]
    WR3['FanDuel_Salary'] = [s.replace('\'', '') for s in WR3['FanDuel_Salary']]
    WR3['FanDuel_Salary'] = [s.replace(']', '') for s in WR3['FanDuel_Salary']]
    WR3['FanDuel_Salary'] = [s.replace(',', '') for s in WR3['FanDuel_Salary']]
    WR3['FanDuel_Salary'] = [float(i) for i in WR3['FanDuel_Salary']]

    TE['FanDuel_Salary'] = [s.replace(']],', '') for s in TE['FanDuel_Salary']]
    TE['FanDuel_Salary'] = [s.replace('\'', '') for s in TE['FanDuel_Salary']]
    TE['FanDuel_Salary'] = [s.replace(']', '') for s in TE['FanDuel_Salary']]
    TE['FanDuel_Salary'] = [s.replace(',', '') for s in TE['FanDuel_Salary']]
    TE['FanDuel_Salary'] = [float(i) for i in TE['FanDuel_Salary']]

    K['FanDuel_Salary'] = [s.replace(']],', '') for s in K['FanDuel_Salary']]
    K['FanDuel_Salary'] = [s.replace('\'', '') for s in K['FanDuel_Salary']]
    K['FanDuel_Salary'] = [s.replace(']', '') for s in K['FanDuel_Salary']]
    K['FanDuel_Salary'] = [s.replace(',', '') for s in K['FanDuel_Salary']]
    K['FanDuel_Salary'] = [float(i) for i in K['FanDuel_Salary']]

    DST['FanDuel_Salary'] = [s.replace(']],', '') for s in DST['FanDuel_Salary']]
    DST['FanDuel_Salary'] = [s.replace('\'', '') for s in DST['FanDuel_Salary']]
    DST['FanDuel_Salary'] = [s.replace(']', '') for s in DST['FanDuel_Salary']]
    DST['FanDuel_Salary'] = [s.replace(',', '') for s in DST['FanDuel_Salary']]
    DST['FanDuel_Salary'] = [float(i) for i in DST['FanDuel_Salary']]

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])
  #  print(DSTposition)
 #   print(first)
 #   print(first[0][1])
    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

 #   return first, QBposition, RB1position, RB2position, WR1position, WR2position, WR3position, TEposition, Kposition, DSTposition, QBclosest, RBclosest, RB2closest, WRclosest, WR2closest, WR3closest, TEclosest, Kclosest, DSTclosest

#def MoneyTIME(spreadsheetId, rangeName):
#    first, QBposition, RB1position, RB2position, WR1position, WR2position, WR3position, TEposition, Kposition, DSTposition, QBclosest, RBclosest, RB2closest, WRclosest, WR2closest, WR3closest, TEclosest, Kclosest, DSTclosest = superline(spreadsheetId, rangeName)
#    global DSTSCERRA
 #   print('moneytime')
 #   print(first)
  #  print(DST)
    if first[-1] > 64000 and first[-1] < 65000 and first[0][1] == first[3][1] and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:
     #   print(first)
        print('_________________________________________________')
        print('STARTER KUSH')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        print(first)

        set_position_nums('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
## GOLDEN Drop each position seperatley by just 1
#        D1x('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#
#
## Phase2!!!!!!!!!!
## Golden drop WR3 and TE by 1
#        print('START------------------------set1-------------------------')
#        Set1('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
## GOLDEN drop TE and WR2 by 1
#        print('START------------------------set2-------------------------')
#        Set2('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
## GOLDEN drop WR2 and K by 1
#        print('START------------------------set3-------------------------')
#        Set3('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
## GOLDEN drop K and RB2 by 1
#        print('START------------------------set4-------------------------')
#        Set4('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
## GOLDEN drop RB2 and DST by 1
#        print('START------------------------set5-------------------------')
#        Set5('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
## GOLDEN drop DST and RB by 1
#        print('START------------------------set6-------------------------')
#        Set6('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
## GOLDEN drop RB and WR by 1
#        print('START------------------------set7-------------------------')
#        Set7('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
## GOLDEN drop WR and QB by 1
#        print('START------------------------set8-------------------------')
#        Set8('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#
#
## Golden drop WR3 and TE by 1
#        print('START------------------------Phase3set1-------------------------')
#        Phase3Set1('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
## GOLDEN drop TE and WR2 by 1
#        print('START------------------------Phase3set2-------------------------')
#        Phase3Set2('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
## GOLDEN drop WR2 and K by 1
#        print('START------------------------Phase3set3-------------------------')
#        Phase3Set3('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
## GOLDEN drop K and RB2 by 1
#        print('START------------------------Phase3set4-------------------------')
#        Phase3Set4('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
## GOLDEN drop RB2 and DST by 1
#        print('START------------------------Phase3set5-------------------------')
#        Phase3Set5('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
## GOLDEN drop DST and RB by 1
#        print('START------------------------Phase3set6-------------------------')
#        Phase3Set6('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
## GOLDEN drop RB and WR by 1
#        print('START------------------------Phase3set7-------------------------')
#        Phase3Set7('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
##______________________________________________________________________
#
#        print('START------------------------Phase4set1-------------------------')
#        Phase4Set1('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
#
#        print('START------------------------Phase4set2-------------------------')
#        Phase4Set2('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#
#        print('START------------------------Phase4set3-------------------------')
#        Phase4Set3('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#
#        print('START------------------------Phase4set4-------------------------')
#        Phase4Set4('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
#
#        print('START------------------------Phase4set5-------------------------')
#        Phase4Set5('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#
#        print('START------------------------Phase4set6-------------------------')
#        Phase4Set6('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#
#     # ______________________________________________________________________
#
#        print('START------------------------Phase5set1-------------------------')
#        Phase5Set1('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes','no')
#
#        print('START------------------------Phase5set2-------------------------')
#        Phase5Set2('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#
#        print('START------------------------Phase5set3-------------------------')
#        Phase5Set3('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#
#        print('START------------------------Phase5set4-------------------------')
#        Phase5Set4('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
#
#        print('START------------------------Phase5set5-------------------------')
#        Phase5Set5('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#
#     # ______________________________________________________________________
#
#        print('START------------------------Phase6set1-------------------------')
#        Phase6Set1('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
#
#        print('START------------------------Phase6set2-------------------------')
#        Phase6Set2('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#
#        print('START------------------------Phase6set3-------------------------')
#        Phase6Set3('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#
#        print('START------------------------Phase6set4-------------------------')
#        Phase6Set4('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
#
#     # ______________________________________________________________________
#        print('START------------------------Phase7set1-------------------------')
#        Phase7Set1('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
#
#        print('START------------------------Phase7set2-------------------------')
#        Phase7Set2('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#
#        print('START------------------------Phase7set3-------------------------')
#        Phase7Set3('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#        print('START------------------------Phase8set1-------------------------')
#        Phase8Set1('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no')
#
#        print('START------------------------Phase8set2-------------------------')
#        Phase8Set2('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes')
#    #### GOLDEN!!!!!!!!!!!!!!!!
#
## Drop each position individually by 2
#        print('START------------------------D2X-------------------------')
#        D2x('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

# Removes each position individually starting from removing just 1 player to removing 31 players.
        for i in range(32):
            #print(i)
            # when i = 1 it is doing the same thing as D1x, then D2x, D3x, D4x... D32x
            # All Phases just remove by 1
            Dnum = i
            print('START------------------------D3xSet1-------------------------')
            D3xSet1('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no', Dnum)
            print('START------------------------D3xSet2-------------------------')
            D3xSet2('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes', Dnum)
            print('START------------------------D3xSet3-------------------------')
            #Bug in WR2 it removes 3 on first go when it should only remove 1. RFE it!
            D3xSet3('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes', Dnum)
            print('START------------------------D3xSet4-------------------------')
            D3xSet4('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no', Dnum)
            print('START------------------------D3xSet5-------------------------')
            D3xSet5('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes', Dnum)
            print('START------------------------D3xSet6-------------------------')
            D3xSet6('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes', Dnum)
            print('START------------------------D3xSet7-------------------------')
            D3xSet7('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'yes', 'no', Dnum)
            print('START------------------------D3xSet8-------------------------')
            D3xSet8('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes', Dnum)
            print('START------------------------D3xSet8-------------------------')
            D3xSet9('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST, 'no', 'yes', Dnum)

#    return (QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
   #     first = superline(spreadsheetId, rangeName)
#        print(first)
#        print(DST)

# def display_closest2(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
#
#     QBSTD = QB['STD']
#
#     QBSTD = QBSTD.values.tolist()
#     QB_avg_std = 1.7697010980470589
#     QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
#     QBposition = (QBSTD.index(QBclosest))
#
#     RBSTD = RB['STD']
#     RBSTD = RBSTD.values.tolist()
#     RB1_avg_std = 3.8891219586694112
#     RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
#     RB1position = (RBSTD.index(RBclosest))
#
#     RB2 = RB[RB.STD != RBclosest]
#
#     RB2STD = RB2['STD']
#     RB2STD = RB2STD.values.tolist()
#     RB2_avg_std = 3.957562269411765
#     RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
#     RB2position = (RB2STD.index(RB2closest))
#
#     WRSTD = WR['STD']
#
#     WRSTD = WRSTD.values.tolist()
#
#     WR1_avg_std = 5.0732831823529425
#     WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
#     WR1position = (WRSTD.index(WRclosest))
#
#     WR2 = WR[WR.STD != WRclosest]
#     WR2STD = WR2['STD']
#
#     WR2STD = WR2STD.values.tolist()
#
#     WR2_avg_std = 5.996161518058823
#     WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
#     WR2position = (WR2STD.index(WR2closest))
#
#     WR3 = WR2[WR2.STD != WR2closest]
#     WR3STD = WR3['STD']
#     WR3STD = WR3STD.values.tolist()
#
#     WR3_avg_std = 5.283595456647058
#     WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
#     WR3position = (WR3STD.index(WR3closest))
#
#     TESTD = TE['STD']
#     TESTD = TESTD.values.tolist()
#
#     TE_avg_std = 4.302276825235293
#     TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
#     TEposition = (TESTD.index(TEclosest))
#
#     KSTD = K['STD']
#     KSTD = KSTD.values.tolist()
#
#     K_avg_std = 5.071295935117646
#     Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
#     Kposition = (KSTD.index(Kclosest))
#
#     DSTSTD = DST['STD']
#     DSTSTD = DSTSTD.values.tolist()
#     DST_avg_std = 2.651650429611765
#     DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
#     DSTposition = (DSTSTD.index(DSTclosest))
#
#     QBpos = QB.values.tolist()
#     RBpos = RB.values.tolist()
#     RB2pos = RB2.values.tolist()
#     WRpos = WR.values.tolist()
#     WR2pos = WR2.values.tolist()
#     WR3pos = WR3.values.tolist()
#     TEpos = TE.values.tolist()
#     Kpos = K.values.tolist()
#     DSTpos = DST.values.tolist()
#
#     first = []
#
#     first.append(QBpos[QBposition])
#     first.append(RBpos[RB1position])
#     first.append(RB2pos[RB2position])
#     first.append(WRpos[WR1position])
#     first.append(WR2pos[WR2position])
#     first.append(WR3pos[WR3position])
#     first.append(TEpos[TEposition])
#     first.append(Kpos[Kposition])
#     first.append(DSTpos[DSTposition])
#
#     totalPoints = sum([first[0][1], first[1][1], first[2][1], first[3][1], first[4][1], first[5][1], first[6][1], first[7][1], first[8][1]])
#
#     totalSalary = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])
#
#     first.append(totalPoints)
#     first.append(totalSalary)
#
#     if (first[-1] > 61400 and first[-1] < 65000):
#         print('SUCCESS your winning lineup is', first)
#     else:
#
#         QB = QB[QB.STD != QBclosest]
#         RB = RB[RB.STD != RBclosest]
#         RB2 = RB2[RB2.STD != RB2closest]
#         DST = DST[DST.STD != DSTclosest]
#         TE = TE[TE.STD != TEclosest]
#         K = K[K.STD != Kclosest]
#         WR = WR[WR.STD != WRclosest]
#         WR2 = WR2[WR2.STD != WR2closest]
#         WR3 = WR3[WR3.STD != WR3closest]
#         display_closest2('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#
#   #      print(first)

def WR3PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']
    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:
        print('_________________________________________________')
        print('WR3PLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        # Figure out how to remove by name instead of by WR3closest
        # Phase? (1,2,3,4,5,6,7,8,9)
        # Set? (D1x, D2x, D3x, D4x, ...., D32x)
# Reorder STD likenups by closest to the AVG STD!!!
#        print(WR)
        WR3 = WR3[WR3.STD != WR3closest]
#        print(WR3.head(50))
        print('WR3PLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']
        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

        totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        print(len(WR))
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        #TEPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
# could do variation of position, least variiation on top most on bottom

def TEPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
 #   WR = display_closest(spreadsheetId, rangeName)

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:
        print('_________________________________________________')
        print('TEPLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
    #    print(WR3.head(50))
        TE = TE[TE.STD != TEclosest]
    #    print(WR3.head(50))
        print('TEPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
     #   print(first)


        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)

        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        #WR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def WR2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

      #  print(first)
        print('_________________________________________________')
        print('WR2PLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        WR2 = WR2[WR2.STD != WR2closest]
        print('WR2PLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        #KPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def KPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

     #   print(first)
        print('_________________________________________________')
        print('KPLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        K = K[K.STD != Kclosest]
        print('KPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
       # RB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def RB2PLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:
        print('_________________________________________________')
        print('RB2PLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        RB2 = RB2[RB2.STD != RB2closest]
        print('RB2PLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
       # DSTPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def DSTPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        #QB = QB[QB.STD != QBclosest]
        #RB = RB[RB.STD != RBclosest]
        #RB2 = RB2[RB2.STD != RB2closest]
        #DST = DST[DST.STD != DSTclosest]
      #  TE = TE[TE.STD != TEclosest]
        #K = K[K.STD != Kclosest]
        #WR = WR[WR.STD != WRclosest]
        #WR2 = WR2[WR2.STD != WR2closest]
        #WR3 = WR3[WR3.STD != WR3closest]
        print('_________________________________________________')
        print('DSTPLEX PRINT OUT BEFORE')
        print('WR')
        print(len(WR))
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB')
        print(len(RB))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        #WR2 = WR2[WR2.STD != WR2closest]
        print('QB')
        print(len(QB))
        DST = DST[DST.STD != DSTclosest]
        print('DSTPLEX PRINT OUT AFTER')
        print('WR')
        print(len(WR))
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB')
        print(len(RB))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
     #   RBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def RBPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if first[-1] > 50000 and first[-1] < 65000 and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        #QB = QB[QB.STD != QBclosest]
        #RB = RB[RB.STD != RBclosest]
        #RB2 = RB2[RB2.STD != RB2closest]
        #DST = DST[DST.STD != DSTclosest]
      #  TE = TE[TE.STD != TEclosest]
        #K = K[K.STD != Kclosest]
        #WR = WR[WR.STD != WRclosest]
        #WR2 = WR2[WR2.STD != WR2closest]
        #WR3 = WR3[WR3.STD != WR3closest]
        print('_________________________________________________')
        print('RBPLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        #WR2 = WR2[WR2.STD != WR2closest]
        RB = RB[RB.STD != RBclosest]
        print('RBPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
       # WRPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def WRPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if first[-1] > 50000 and first[-1] < 65000 and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        print('_________________________________________________')
        print('WRPLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        #WR2 = WR2[WR2.STD != WR2closest]
        WR = WR[WR.STD != WRclosest]
        print('WRPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
      #  QBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def QBPLEX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if first[-1] > 50000 and first[-1] < 65000 and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        print('_________________________________________________')
        print('QBPLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        QB = QB[QB.STD != QBclosest]
        print('QBPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)

               # WR3PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)


def WR3PLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']
    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:
        print('_________________________________________________')
        print('WR3PLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        # Figure out how to remove by name instead of by WR3closest
        # Phase? (1,2,3,4,5,6,7,8,9)
        # Set? (D1x, D2x, D3x, D4x, ...., D32x)
# Reorder STD likenups by closest to the AVG STD!!!
#        print(WR)
        WR3 = WR3[WR3.STD != WR3closest]
        WR = WR[WR.STD != WR3closest]
#        print(WR3.head(50))
        print('WR3PLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']
        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

        totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        print(len(WR))
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(WR3) >= 109:
            WR3PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)



#    print(QB)
#    return QB, RB, RB2, WR, WR2, WR3, TE, K, DST
#        TEPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
# could do variation of position, least variiation on top most on bottom

def TEPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
 #   WR = display_closest(spreadsheetId, rangeName)

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:
        print('_________________________________________________')
        print('TEPLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
    #    print(WR3.head(50))
        TE = TE[TE.STD != TEclosest]
    #    print(WR3.head(50))
        print('TEPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
     #   print(first)


        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)

        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(TE) >= 58:
            TEPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
        #        WR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def WR2PLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

      #  print(first)
        print('_________________________________________________')
        print('WR2PLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        WR2 = WR2[WR2.STD != WR2closest]
        WR = WR[WR.STD != WR2closest]
        print('WR2PLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(WR2) >= 110:
            WR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
 #       KPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def KPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

     #   print(first)
        print('_________________________________________________')
        print('KPLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        K = K[K.STD != Kclosest]
        print('KPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(K) >= 30:
            KPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
     #       RB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def RB2PLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:
        print('_________________________________________________')
        print('RB2PLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        RB2 = RB2[RB2.STD != RB2closest]
        RB = RB[RB.STD != RB2closest]
        print('RB2PLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(RB2) >= 82:
            RB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#        DSTPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def DSTPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        #QB = QB[QB.STD != QBclosest]
        #RB = RB[RB.STD != RBclosest]
        #RB2 = RB2[RB2.STD != RB2closest]
        #DST = DST[DST.STD != DSTclosest]
      #  TE = TE[TE.STD != TEclosest]
        #K = K[K.STD != Kclosest]
        #WR = WR[WR.STD != WRclosest]
        #WR2 = WR2[WR2.STD != WR2closest]
        #WR3 = WR3[WR3.STD != WR3closest]
        print('_________________________________________________')
        print('DSTPLEX PRINT OUT BEFORE')
        print('WR')
        print(len(WR))
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB')
        print(len(RB))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        #WR2 = WR2[WR2.STD != WR2closest]
        print('QB')
        print(len(QB))
        DST = DST[DST.STD != DSTclosest]
        print('DSTPLEX PRINT OUT AFTER')
        print('WR')
        print(len(WR))
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB')
        print(len(RB))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(DST) >= 30:
            DSTPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
 #       RBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def RBPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if first[-1] > 50000 and first[-1] < 65000 and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        #QB = QB[QB.STD != QBclosest]
        #RB = RB[RB.STD != RBclosest]
        #RB2 = RB2[RB2.STD != RB2closest]
        #DST = DST[DST.STD != DSTclosest]
      #  TE = TE[TE.STD != TEclosest]
        #K = K[K.STD != Kclosest]
        #WR = WR[WR.STD != WRclosest]
        #WR2 = WR2[WR2.STD != WR2closest]
        #WR3 = WR3[WR3.STD != WR3closest]
        print('_________________________________________________')
        print('RBPLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        #WR2 = WR2[WR2.STD != WR2closest]
        RB = RB[RB.STD != RBclosest]
        print('RBPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(RB) >= 83:
            RBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
 #       WRPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def WRPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if first[-1] > 50000 and first[-1] < 65000 and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        print('_________________________________________________')
        print('WRPLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        #WR2 = WR2[WR2.STD != WR2closest]
        WR = WR[WR.STD != WRclosest]
        print('WRPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(WR) >= 111:
            WRPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#        QBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def QBPLEXX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    QBSTD = QB['STD']

    QBSTD = QBSTD.values.tolist()
    QB_avg_std = 1.7697010980470589
    QBclosest = min(QBSTD, key=lambda x:abs(x-QB_avg_std))
    QBposition = (QBSTD.index(QBclosest))

    RBSTD = RB['STD']
    RBSTD = RBSTD.values.tolist()
    RB1_avg_std = 3.8891219586694112
    RBclosest = min(RBSTD, key=lambda x:abs(x-RB1_avg_std))
    RB1position = (RBSTD.index(RBclosest))

    RB2 = RB[RB.STD != RBclosest]

    RB2STD = RB2['STD']
    RB2STD = RB2STD.values.tolist()
    RB2_avg_std = 3.957562269411765
    RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
    RB2position = (RB2STD.index(RB2closest))

    WRSTD = WR['STD']

    WRSTD = WRSTD.values.tolist()

    WR1_avg_std = 5.0732831823529425
    WRclosest = min(WRSTD, key=lambda x:abs(x-WR1_avg_std))
    WR1position = (WRSTD.index(WRclosest))

    WR2 = WR[WR.STD != WRclosest]
    WR2STD = WR2['STD']

    WR2STD = WR2STD.values.tolist()

    WR2_avg_std = 5.996161518058823
    WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
    WR2position = (WR2STD.index(WR2closest))

    WR3 = WR2[WR2.STD != WR2closest]
    WR3STD = WR3['STD']
    WR3STD = WR3STD.values.tolist()

    WR3_avg_std = 5.283595456647058
    WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
    WR3position = (WR3STD.index(WR3closest))

    TESTD = TE['STD']
    TESTD = TESTD.values.tolist()

    TE_avg_std = 4.302276825235293
    TEclosest = min(TESTD, key=lambda x:abs(x-TE_avg_std))
    TEposition = (TESTD.index(TEclosest))

    KSTD = K['STD']
    KSTD = KSTD.values.tolist()

    K_avg_std = 5.071295935117646
    Kclosest = min(KSTD, key=lambda x:abs(x-K_avg_std))
    Kposition = (KSTD.index(Kclosest))

    DSTSTD = DST['STD']
    DSTSTD = DSTSTD.values.tolist()
    DST_avg_std = 2.651650429611765
    DSTclosest = min(DSTSTD, key=lambda x:abs(x-DST_avg_std))
    DSTposition = (DSTSTD.index(DSTclosest))

    QBpos = QB.values.tolist()
    RBpos = RB.values.tolist()
    RB2pos = RB2.values.tolist()
    WRpos = WR.values.tolist()
    WR2pos = WR2.values.tolist()
    WR3pos = WR3.values.tolist()
    TEpos = TE.values.tolist()
    Kpos = K.values.tolist()
    DSTpos = DST.values.tolist()

    first = []

    first.append(QBpos[QBposition])
    first.append(RBpos[RB1position])
    first.append(RB2pos[RB2position])
    first.append(WRpos[WR1position])
    first.append(WR2pos[WR2position])
    first.append(WR3pos[WR3position])
    first.append(TEpos[TEposition])
    first.append(Kpos[Kposition])
    first.append(DSTpos[DSTposition])

    totalPoints = sum([first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2], first[8][2]])

    totalSalary = sum([first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3], first[8][3]])

    first.append(totalPoints)
    first.append(totalSalary)

    if first[-1] > 50000 and first[-1] < 65000 and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
        print('SUCCESS your winning lineup is', first)
    else:

        print('_________________________________________________')
        print('QBPLEX PRINT OUT BEFORE')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))
        QB = QB[QB.STD != QBclosest]
        print('QBPLEX PRINT OUT AFTER')
        print('WR3')
        print(len(WR3))
        print('TE')
        print(len(TE))
        print('WR2')
        print(len(WR2))
        print('K')
        print(len(K))
        print('RB2')
        print(len(RB2))
        print('DST')
        print(len(DST))
        print('RB1')
        print(len(RB))
        print('WR1')
        print(len(WR))
        print('QB')
        print(len(QB))

        QBSTD = QB['STD']

        QBSTD = QBSTD.values.tolist()
        QB_avg_std = 1.7697010980470589
        QBclosest = min(QBSTD, key=lambda x: abs(x - QB_avg_std))
        QBposition = (QBSTD.index(QBclosest))

        RBSTD = RB['STD']
        RBSTD = RBSTD.values.tolist()
        RB1_avg_std = 3.8891219586694112
        RBclosest = min(RBSTD, key=lambda x: abs(x - RB1_avg_std))
        RB1position = (RBSTD.index(RBclosest))

        RB2 = RB[RB.STD != RBclosest]

        RB2STD = RB2['STD']
        RB2STD = RB2STD.values.tolist()
        RB2_avg_std = 3.957562269411765
        RB2closest = min(RB2STD, key=lambda x: abs(x - RB2_avg_std))
        RB2position = (RB2STD.index(RB2closest))

        WRSTD = WR['STD']

        WRSTD = WRSTD.values.tolist()

        WR1_avg_std = 5.0732831823529425
        WRclosest = min(WRSTD, key=lambda x: abs(x - WR1_avg_std))
        WR1position = (WRSTD.index(WRclosest))

        WR2 = WR[WR.STD != WRclosest]
        WR2STD = WR2['STD']

        WR2STD = WR2STD.values.tolist()

        WR2_avg_std = 5.996161518058823
        WR2closest = min(WR2STD, key=lambda x: abs(x - WR2_avg_std))
        WR2position = (WR2STD.index(WR2closest))

        WR3 = WR2[WR2.STD != WR2closest]
        WR3STD = WR3['STD']
        WR3STD = WR3STD.values.tolist()

        WR3_avg_std = 5.283595456647058
        WR3closest = min(WR3STD, key=lambda x: abs(x - WR3_avg_std))
        WR3position = (WR3STD.index(WR3closest))

        TESTD = TE['STD']
        TESTD = TESTD.values.tolist()

        TE_avg_std = 4.302276825235293
        TEclosest = min(TESTD, key=lambda x: abs(x - TE_avg_std))
        TEposition = (TESTD.index(TEclosest))

        KSTD = K['STD']
        KSTD = KSTD.values.tolist()

        K_avg_std = 5.071295935117646
        Kclosest = min(KSTD, key=lambda x: abs(x - K_avg_std))
        Kposition = (KSTD.index(Kclosest))

        DSTSTD = DST['STD']
        DSTSTD = DSTSTD.values.tolist()
        DST_avg_std = 2.651650429611765
        DSTclosest = min(DSTSTD, key=lambda x: abs(x - DST_avg_std))
        DSTposition = (DSTSTD.index(DSTclosest))

        QBpos = QB.values.tolist()
        RBpos = RB.values.tolist()
        RB2pos = RB2.values.tolist()
        WRpos = WR.values.tolist()
        WR2pos = WR2.values.tolist()
        WR3pos = WR3.values.tolist()
        TEpos = TE.values.tolist()
        Kpos = K.values.tolist()
        DSTpos = DST.values.tolist()

        first = []

        first.append(QBpos[QBposition])
        first.append(RBpos[RB1position])
        first.append(RB2pos[RB2position])
        first.append(WRpos[WR1position])
        first.append(WR2pos[WR2position])
        first.append(WR3pos[WR3position])
        first.append(TEpos[TEposition])
        first.append(Kpos[Kposition])
        first.append(DSTpos[DSTposition])

        totalPoints = sum(
            [first[0][2], first[1][2], first[2][2], first[3][2], first[4][2], first[5][2], first[6][2], first[7][2],
             first[8][2]])

        totalSalary = sum(
            [first[0][3], first[1][3], first[2][3], first[3][3], first[4][3], first[5][3], first[6][3], first[7][3],
             first[8][3]])

        first.append(totalPoints)
        first.append(totalSalary)
        print(first)
        if (first[-1] > 50000 and first[-1] < 65000) and first[0][1] == first[3][1] : #and first[7][1] == first[8][1]:
            print('SUCCESS your winning lineup is', first)
        elif len(QB) >= 30:
            QBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
               # WR3PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#        else:
#            WR3PLEXX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537',  QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def Phase1(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    WR3PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)


def Phase1x(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    WR3PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    WR3PLEXcontd('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')

def Phase2(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    TEPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def Phase3(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    WR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def Phase4(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    KPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def Phase5(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    RB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def Phase6(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    DSTPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def Phase7(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    RBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def Phase8(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    WRPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def Phase9(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    QBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def PhaseX(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):

    WR3PLEXX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)


## Possible Phase list
# K
# WR3
# TE
# DST
# QB
# WR2
# RB2
# WR1
# RB1

def D1x(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    Phase1('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    Phase2('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    Phase3('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    Phase4('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    Phase5('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    Phase6('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    Phase7('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    Phase8('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    Phase9('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)

def D2x(spreadsheetId, rangeName, QB, RB, RB2, WR, WR2, WR3, TE, K, DST):
    WR3PLEXX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    TEPLEXX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    WR2PLEXX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    KPLEXX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    RB2PLEXX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    DSTPLEXX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    RBPLEXX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    WRPLEXX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
    QBPLEXX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#    for i in range(2):
#        TEPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#    for i in range(2):
#        WR2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#    for i in range(2):
#        KPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#    for i in range(2):
#        RB2PLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#    for i in range(2):
#        DSTPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#    for i in range(2):
#        RBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#    for i in range(2):
#        WRPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)
#    for i in range(2):
#        QBPLEX('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537', QB, RB, RB2, WR, WR2, WR3, TE, K, DST)


if __name__ == '__main__':
    # 2015 week1
    posDframe('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
    Data_clean('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
    removeNA('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
    Roster_cut('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
    removeLowProjections('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
    hitpositionLimits('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
    useNeededCols('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
    order_for_perfect('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
    display_closest('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')

 #   play_function('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
 #    superline('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
 #   MoneyTIME('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
    # createAllLineups('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
    # std_finder('1VZLj2gegd6RwDmE3UYprClaGsMe91TDrNw8fsC5ZbD4', 'A1:L537')
     # 2015 week2
    #posDframe('1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE', 'A1:L545')
    #Data_clean('1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE', 'A1:L545')
    #removeNA('1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE', 'A1:L545')
    #Roster_cut('1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE', 'A1:L545')
    #removeLowProjections('1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE', 'A1:L545')
    #hitpositionLimits('1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE', 'A1:L545')
    #useNeededCols('1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE', 'A1:L545')
    #order_for_perfect('1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE', 'A1:L545')
    #display_closest('1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE', 'A1:L545')
    #    createAllLineups('1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE', 'A1:L545')
    #    std_finder('1JRz3BLEoglYVR0tx7ysu7UuS2GCOe15-ZAIzKsos3PE', 'A1:L545')
    # 2015 week3
    #posDframe('15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo', 'A1:L534')
    #Data_clean('15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo', 'A1:L534')
    #removeNA('15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo', 'A1:L534')
    #Roster_cut('15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo', 'A1:L534')
    #removeLowProjections('15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo', 'A1:L534')
    #hitpositionLimits('15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo', 'A1:L534')
    #useNeededCols('15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo', 'A1:L534')
    #order_for_perfect('15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo', 'A1:L534')
    #display_closest('15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo', 'A1:L534')
    #    createAllLineups('15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo', 'A1:L534')
    #    std_finder('15_Tw4iqUFclgA9FbdQN2C_ITwSvVdDzdFfwXnZVK1uo', 'A1:L534')
    #    # 2015 week4
    #    posDframe('1zQrAsg8IUWNn-N-cWpi63xpyqMRvYJjvPoVL5CXhj74', 'A1:L491')
    #    Data_clean('1zQrAsg8IUWNn-N-cWpi63xpyqMRvYJjvPoVL5CXhj74', 'A1:L491')
    #    removeNA('1zQrAsg8IUWNn-N-cWpi63xpyqMRvYJjvPoVL5CXhj74', 'A1:L491')
    #    Roster_cut('1zQrAsg8IUWNn-N-cWpi63xpyqMRvYJjvPoVL5CXhj74', 'A1:L491')
    #    removeLowProjections('1zQrAsg8IUWNn-N-cWpi63xpyqMRvYJjvPoVL5CXhj74', 'A1:L491')
    #    hitpositionLimits('1zQrAsg8IUWNn-N-cWpi63xpyqMRvYJjvPoVL5CXhj74', 'A1:L491')
    #    useNeededCols('1zQrAsg8IUWNn-N-cWpi63xpyqMRvYJjvPoVL5CXhj74', 'A1:L491')
    #    order_for_perfect('1zQrAsg8IUWNn-N-cWpi63xpyqMRvYJjvPoVL5CXhj74', 'A1:L491')
    #    createAllLineups('1zQrAsg8IUWNn-N-cWpi63xpyqMRvYJjvPoVL5CXhj74', 'A1:L491')
    #    std_finder('1zQrAsg8IUWNn-N-cWpi63xpyqMRvYJjvPoVL5CXhj74', 'A1:L491')
    #    # 2015 week5
    #    posDframe('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L491')
    #    Data_clean('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L491')
    #    removeNA('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L491')
    #    Roster_cut('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L491')
    #    removeLowProjections('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L491')
    #    hitpositionLimits('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L491')
    #    useNeededCols('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L491')
    #    order_for_perfect('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L491')
    #    createAllLineups('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L491')
    #    std_finder('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L491')
    #    # 2015 week6
    #    posDframe('1DCMUJigFCXhv6PTqQg0A60FncrUONHW3Y0ebJyYNg1o', 'A1:L474')
    #    Data_clean('1DCMUJigFCXhv6PTqQg0A60FncrUONHW3Y0ebJyYNg1o', 'A1:L474')
    #    removeNA('1DCMUJigFCXhv6PTqQg0A60FncrUONHW3Y0ebJyYNg1o', 'A1:L474')
    #    Roster_cut('1DCMUJigFCXhv6PTqQg0A60FncrUONHW3Y0ebJyYNg1o', 'A1:L474')
    #    removeLowProjections('1DCMUJigFCXhv6PTqQg0A60FncrUONHW3Y0ebJyYNg1o', 'A1:L474')
    #    hitpositionLimits('1DCMUJigFCXhv6PTqQg0A60FncrUONHW3Y0ebJyYNg1o', 'A1:L474')
    #    useNeededCols('1DCMUJigFCXhv6PTqQg0A60FncrUONHW3Y0ebJyYNg1o', 'A1:L474')
    #    order_for_perfect('1DCMUJigFCXhv6PTqQg0A60FncrUONHW3Y0ebJyYNg1o', 'A1:L474')
    #    createAllLineups('1DCMUJigFCXhv6PTqQg0A60FncrUONHW3Y0ebJyYNg1o', 'A1:L474')
    #    std_finder('1DCMUJigFCXhv6PTqQg0A60FncrUONHW3Y0ebJyYNg1o', 'A1:L491')
    #    # 2015 week7
    #    posDframe('1HQkkgp12J8R9Sa7Te_qZKAJpoZf6dLdynPXYrlpqwcg', 'A1:L476')
    #    Data_clean('1HQkkgp12J8R9Sa7Te_qZKAJpoZf6dLdynPXYrlpqwcg', 'A1:L476')
    #    removeNA('1HQkkgp12J8R9Sa7Te_qZKAJpoZf6dLdynPXYrlpqwcg', 'A1:L476')
    #    Roster_cut('1HQkkgp12J8R9Sa7Te_qZKAJpoZf6dLdynPXYrlpqwcg', 'A1:L476')
    #    removeLowProjections('1HQkkgp12J8R9Sa7Te_qZKAJpoZf6dLdynPXYrlpqwcg', 'A1:L476')
    #    hitpositionLimits('1HQkkgp12J8R9Sa7Te_qZKAJpoZf6dLdynPXYrlpqwcg', 'A1:L476')
    #    useNeededCols('1HQkkgp12J8R9Sa7Te_qZKAJpoZf6dLdynPXYrlpqwcg', 'A1:L476')
    #    order_for_perfect('1HQkkgp12J8R9Sa7Te_qZKAJpoZf6dLdynPXYrlpqwcg', 'A1:L476')
    #    createAllLineups('1HQkkgp12J8R9Sa7Te_qZKAJpoZf6dLdynPXYrlpqwcg', 'A1:L476')
    #    std_finder('1HQkkgp12J8R9Sa7Te_qZKAJpoZf6dLdynPXYrlpqwcg', 'A1:L476')
    #    # 2015 week8
    #    posDframe('11xsMM28Edz-TDN6zbmospqDHz_ACNj45-bRQk844Sjw', 'A1:L474')
    #    Data_clean('11xsMM28Edz-TDN6zbmospqDHz_ACNj45-bRQk844Sjw', 'A1:L474')
    #    removeNA('11xsMM28Edz-TDN6zbmospqDHz_ACNj45-bRQk844Sjw', 'A1:L474')
    #    Roster_cut('11xsMM28Edz-TDN6zbmospqDHz_ACNj45-bRQk844Sjw', 'A1:L474')
    #    removeLowProjections('11xsMM28Edz-TDN6zbmospqDHz_ACNj45-bRQk844Sjw', 'A1:L474')
    #    hitpositionLimits('11xsMM28Edz-TDN6zbmospqDHz_ACNj45-bRQk844Sjw', 'A1:L474')
    #    useNeededCols('11xsMM28Edz-TDN6zbmospqDHz_ACNj45-bRQk844Sjw', 'A1:L474')
    #    order_for_perfect('11xsMM28Edz-TDN6zbmospqDHz_ACNj45-bRQk844Sjw', 'A1:L474')
    #    createAllLineups('11xsMM28Edz-TDN6zbmospqDHz_ACNj45-bRQk844Sjw', 'A1:L474')
    #    std_finder('11xsMM28Edz-TDN6zbmospqDHz_ACNj45-bRQk844Sjw', 'A1:L474')
    #    # 2015 week9
    #    posDframe('1bblln58znQA8E0aUDEjCUZqYrvXjL5kd3zqOXxRMuhw', 'A1:L431')
    #    Data_clean('1bblln58znQA8E0aUDEjCUZqYrvXjL5kd3zqOXxRMuhw', 'A1:L431')
    #    removeNA('1bblln58znQA8E0aUDEjCUZqYrvXjL5kd3zqOXxRMuhw', 'A1:L431')
    #    Roster_cut('1bblln58znQA8E0aUDEjCUZqYrvXjL5kd3zqOXxRMuhw', 'A1:L431')
    #    removeLowProjections('1bblln58znQA8E0aUDEjCUZqYrvXjL5kd3zqOXxRMuhw', 'A1:L431')
    #    hitpositionLimits('1bblln58znQA8E0aUDEjCUZqYrvXjL5kd3zqOXxRMuhw', 'A1:L431')
    #    useNeededCols('1bblln58znQA8E0aUDEjCUZqYrvXjL5kd3zqOXxRMuhw', 'A1:L431')
    #    order_for_perfect('1bblln58znQA8E0aUDEjCUZqYrvXjL5kd3zqOXxRMuhw', 'A1:L431')
    #    createAllLineups('1bblln58znQA8E0aUDEjCUZqYrvXjL5kd3zqOXxRMuhw', 'A1:L431')
    #    std_finder('1bblln58znQA8E0aUDEjCUZqYrvXjL5kd3zqOXxRMuhw', 'A1:L431')
    #    # 2015 week10
    #    posDframe('1FaBKYPN8FXtzJg7bo1IvCzNDK2Rm96BjBubDfPYS2CU', 'A1:L486')
    #    Data_clean('1FaBKYPN8FXtzJg7bo1IvCzNDK2Rm96BjBubDfPYS2CU', 'A1:L486')
    #    removeNA('1FaBKYPN8FXtzJg7bo1IvCzNDK2Rm96BjBubDfPYS2CU', 'A1:L486')
    #    Roster_cut('1FaBKYPN8FXtzJg7bo1IvCzNDK2Rm96BjBubDfPYS2CU', 'A1:L486')
    #    removeLowProjections('1FaBKYPN8FXtzJg7bo1IvCzNDK2Rm96BjBubDfPYS2CU', 'A1:L486')
    #    hitpositionLimits('1FaBKYPN8FXtzJg7bo1IvCzNDK2Rm96BjBubDfPYS2CU', 'A1:L486')
    #    useNeededCols('1FaBKYPN8FXtzJg7bo1IvCzNDK2Rm96BjBubDfPYS2CU', 'A1:L486')
    #    order_for_perfect('1FaBKYPN8FXtzJg7bo1IvCzNDK2Rm96BjBubDfPYS2CU', 'A1:L486')
    #    createAllLineups('1FaBKYPN8FXtzJg7bo1IvCzNDK2Rm96BjBubDfPYS2CU', 'A1:L486')
    #    std_finder('1FaBKYPN8FXtzJg7bo1IvCzNDK2Rm96BjBubDfPYS2CU', 'A1:L486')
    #    # 2015 week11
    #    posDframe('1SjXKGmrz9PkTHw4IKodWjfozYoSeaLo8P7BjxxuKDs4', 'A1:L472')
    #    Data_clean('1SjXKGmrz9PkTHw4IKodWjfozYoSeaLo8P7BjxxuKDs4', 'A1:L472')
    #    removeNA('1SjXKGmrz9PkTHw4IKodWjfozYoSeaLo8P7BjxxuKDs4', 'A1:L472')
    #    Roster_cut('1SjXKGmrz9PkTHw4IKodWjfozYoSeaLo8P7BjxxuKDs4', 'A1:L472')
    #    removeLowProjections('1SjXKGmrz9PkTHw4IKodWjfozYoSeaLo8P7BjxxuKDs4', 'A1:L472')
    #    hitpositionLimits('1SjXKGmrz9PkTHw4IKodWjfozYoSeaLo8P7BjxxuKDs4', 'A1:L472')
    #    useNeededCols('1SjXKGmrz9PkTHw4IKodWjfozYoSeaLo8P7BjxxuKDs4', 'A1:L472')
    #    order_for_perfect('1SjXKGmrz9PkTHw4IKodWjfozYoSeaLo8P7BjxxuKDs4', 'A1:L472')
    #    createAllLineups('1SjXKGmrz9PkTHw4IKodWjfozYoSeaLo8P7BjxxuKDs4', 'A1:L472')
    #    std_finder('1SjXKGmrz9PkTHw4IKodWjfozYoSeaLo8P7BjxxuKDs4', 'A1:L472')
    #    # 2015 week12
    #    posDframe('1R03RkTBQzAqEbkczLz5YWyVqdbdGdW3R_qGi5pPiUOY', 'A1:L525')
    #    Data_clean('1R03RkTBQzAqEbkczLz5YWyVqdbdGdW3R_qGi5pPiUOY', 'A1:L525')
    #    removeNA('1R03RkTBQzAqEbkczLz5YWyVqdbdGdW3R_qGi5pPiUOY', 'A1:L525')
    #    Roster_cut('1R03RkTBQzAqEbkczLz5YWyVqdbdGdW3R_qGi5pPiUOY', 'A1:L525')
    #    removeLowProjections('1R03RkTBQzAqEbkczLz5YWyVqdbdGdW3R_qGi5pPiUOY', 'A1:L525')
    #    hitpositionLimits('1R03RkTBQzAqEbkczLz5YWyVqdbdGdW3R_qGi5pPiUOY', 'A1:L525')
    #    useNeededCols('1R03RkTBQzAqEbkczLz5YWyVqdbdGdW3R_qGi5pPiUOY', 'A1:L525')
    #    order_for_perfect('1R03RkTBQzAqEbkczLz5YWyVqdbdGdW3R_qGi5pPiUOY', 'A1:L525')
    #    createAllLineups('1R03RkTBQzAqEbkczLz5YWyVqdbdGdW3R_qGi5pPiUOY', 'A1:L525')
    #    std_finder('1R03RkTBQzAqEbkczLz5YWyVqdbdGdW3R_qGi5pPiUOY', 'A1:L525')
    #    # 2015 week13
    #    posDframe('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L522')
    #    Data_clean('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L522')
    #    removeNA('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L522')
    #    Roster_cut('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L522')
    #    removeLowProjections('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L522')
    #    hitpositionLimits('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L522')
    #    useNeededCols('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L522')
    #    order_for_perfect('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L522')
    #    createAllLineups('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L522')
    #    std_finder('1sNb4YBMq70VYWHqaUE0jHFZ8CsGt8PwQJwYSkLJMawE', 'A1:L522')
    #    # 2015 week14
    #    posDframe('1U04TTYMKa4L5gToFGI5kIyWWTwg0eaYqPihEVDZTPi4', 'A1:L528')
    #    Data_clean('1U04TTYMKa4L5gToFGI5kIyWWTwg0eaYqPihEVDZTPi4', 'A1:L528')
    #    removeNA('1U04TTYMKa4L5gToFGI5kIyWWTwg0eaYqPihEVDZTPi4', 'A1:L528')
    #    Roster_cut('1U04TTYMKa4L5gToFGI5kIyWWTwg0eaYqPihEVDZTPi4', 'A1:L528')
    #    removeLowProjections('1U04TTYMKa4L5gToFGI5kIyWWTwg0eaYqPihEVDZTPi4', 'A1:L528')
    #    hitpositionLimits('1U04TTYMKa4L5gToFGI5kIyWWTwg0eaYqPihEVDZTPi4', 'A1:L528')
    #    useNeededCols('1U04TTYMKa4L5gToFGI5kIyWWTwg0eaYqPihEVDZTPi4', 'A1:L528')
    #    order_for_perfect('1U04TTYMKa4L5gToFGI5kIyWWTwg0eaYqPihEVDZTPi4', 'A1:L528')
    #    createAllLineups('1U04TTYMKa4L5gToFGI5kIyWWTwg0eaYqPihEVDZTPi4', 'A1:L528')
    #    std_finder('1U04TTYMKa4L5gToFGI5kIyWWTwg0eaYqPihEVDZTPi4', 'A1:L528')
    #    # 2015 week15
    #    posDframe('166Aky6qfxab8EOOROGmuNYv2L9gRDdOGRTgWw-zD3ug', 'A1:L522')
    #    Data_clean('166Aky6qfxab8EOOROGmuNYv2L9gRDdOGRTgWw-zD3ug', 'A1:L522')
    #    removeNA('166Aky6qfxab8EOOROGmuNYv2L9gRDdOGRTgWw-zD3ug', 'A1:L522')
    #    Roster_cut('166Aky6qfxab8EOOROGmuNYv2L9gRDdOGRTgWw-zD3ug', 'A1:L522')
    #    removeLowProjections('166Aky6qfxab8EOOROGmuNYv2L9gRDdOGRTgWw-zD3ug', 'A1:L522')
    #    hitpositionLimits('166Aky6qfxab8EOOROGmuNYv2L9gRDdOGRTgWw-zD3ug', 'A1:L522')
    #    useNeededCols('166Aky6qfxab8EOOROGmuNYv2L9gRDdOGRTgWw-zD3ug', 'A1:L522')
    #    order_for_perfect('166Aky6qfxab8EOOROGmuNYv2L9gRDdOGRTgWw-zD3ug', 'A1:L522')
    #    createAllLineups('166Aky6qfxab8EOOROGmuNYv2L9gRDdOGRTgWw-zD3ug', 'A1:L522')
    #    std_finder('166Aky6qfxab8EOOROGmuNYv2L9gRDdOGRTgWw-zD3ug', 'A1:L522')
    #    # 2015 week16
    #    posDframe('1wJs8S0eSFWCV7Y26yHUFkoEl8dUUqUpUP6OIkwxd3xs', 'A1:L514')
    #    Data_clean('1wJs8S0eSFWCV7Y26yHUFkoEl8dUUqUpUP6OIkwxd3xs', 'A1:L514')
    #    removeNA('1wJs8S0eSFWCV7Y26yHUFkoEl8dUUqUpUP6OIkwxd3xs', 'A1:L514')
    #    Roster_cut('1wJs8S0eSFWCV7Y26yHUFkoEl8dUUqUpUP6OIkwxd3xs', 'A1:L514')
    #    removeLowProjections('1wJs8S0eSFWCV7Y26yHUFkoEl8dUUqUpUP6OIkwxd3xs', 'A1:L514')
    #    hitpositionLimits('1wJs8S0eSFWCV7Y26yHUFkoEl8dUUqUpUP6OIkwxd3xs', 'A1:L514')
    #    useNeededCols('1wJs8S0eSFWCV7Y26yHUFkoEl8dUUqUpUP6OIkwxd3xs', 'A1:L514')
    #    order_for_perfect('1wJs8S0eSFWCV7Y26yHUFkoEl8dUUqUpUP6OIkwxd3xs', 'A1:L514')
    #    createAllLineups('1wJs8S0eSFWCV7Y26yHUFkoEl8dUUqUpUP6OIkwxd3xs', 'A1:L514')
    #    std_finder('1wJs8S0eSFWCV7Y26yHUFkoEl8dUUqUpUP6OIkwxd3xs', 'A1:L514')
    #    # 2015 week17
    #    posDframe('1r4dA1J6GtkzJMXIjhX24hbVViQAoyCGHB0uBaO64JaQ', 'A1:L508')
    #    Data_clean('1r4dA1J6GtkzJMXIjhX24hbVViQAoyCGHB0uBaO64JaQ', 'A1:L508')
    #    removeNA('1r4dA1J6GtkzJMXIjhX24hbVViQAoyCGHB0uBaO64JaQ', 'A1:L508')
    #    Roster_cut('1r4dA1J6GtkzJMXIjhX24hbVViQAoyCGHB0uBaO64JaQ', 'A1:L508')
    #    removeLowProjections('1r4dA1J6GtkzJMXIjhX24hbVViQAoyCGHB0uBaO64JaQ', 'A1:L508')
    #    hitpositionLimits('1r4dA1J6GtkzJMXIjhX24hbVViQAoyCGHB0uBaO64JaQ', 'A1:L508')
    #    useNeededCols('1r4dA1J6GtkzJMXIjhX24hbVViQAoyCGHB0uBaO64JaQ', 'A1:L508')
    #    order_for_perfect('1r4dA1J6GtkzJMXIjhX24hbVViQAoyCGHB0uBaO64JaQ', 'A1:L508')
    #    createAllLineups('1r4dA1J6GtkzJMXIjhX24hbVViQAoyCGHB0uBaO64JaQ', 'A1:L508')
    #    std_finder('1r4dA1J6GtkzJMXIjhX24hbVViQAoyCGHB0uBaO64JaQ', 'A1:L508')
#    perf_std()
#    disect()


#####
# WEEK1 OUTPUT
#SUCCESS your winning lineup is [['Derek Carr', 'OAK', 3.24, 6300.0, 3.149453603], ['Tevin Coleman', 'ATL', 8.0, 6700.0, 3.814841085], ['Eddie Lacy', 'GB', 16.9, 8500.0, 2.499622471], ['Amari Cooper', 'OAK', 7.2, 7100.0, 5.032832515], ['Tavon Austin', 'STL', 14.5, 4700.0, 5.706351724], ['Greg Jennings', 'MIA', 4.4, 4900.0, 4.9444441669999994], ['Maxx Williams', 'BAL', 2.0, 4800.0, 5.7576169650000005], ['Josh Scobee', 'PIT', 8.0, 4600.0, 4.148359783], ['Steelers', 'PIT', 1.0, 4000.0, 4.348706704], 65.24000000000001, 51600.0]