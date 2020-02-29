#!/bin/bash
# This script is meant to take the Google sheets that we created using the Revised approach.
# Which ofcourse is using just three platforms to collect the data (CBS, NFL, FFToday)
# 1. the first pytest will create a file called revised_<postion>.csv for each postion.
# 2. Every pytest after that will append the data the data into the already created file.
# 3. This will leave us with a .csv for each position containing only the important values we
#    need to analyze the STDs accordingly.
# 4. We can then take the STDs and graph the actual results of wk1 over the past 5 years to draw conclusions.



# Set vars from gsheet_id.config file
# Needs to be executed from the "flex" directory
source executables/convert_gsheets_data_to_csv/revised_cbs_nfl_fftoday/gsheet_id.config

pytest -s -v -l --testdata="{'spreadsheetId': '$wk1_2015', 'rangeName': 'A1:L1447', 'round': 5}" -m csv_all_data

# TODO: Replace all of these spreadsheet ids with the revised google sheet ids
#2019
pytest -s -v -l --testdata="{'spreadsheetId': '$wk1_2019',
                              'rangeName': 'A1:L1447',
                              'round': 5,
                              'QBfile': 'wk_1_revised_QB.csv',
                              'RBfile': 'wk_1_revised_RB.csv',
                              'WRfile': 'wk_1_revised_WR.csv',
                              'TEfile': 'wk_1_revised_TE.csv',
                              'DSTfile': 'wk_1_revised_DST.csv',
                              'FLXfile': 'wk_1_revised_FLX.csv'}" -m csv_all_data

#2018
pytest -s -v -l --testdata="{'spreadsheetId': '$wk1_2018',
                              'rangeName': 'A1:L1447',
                              'round': 5,
                              'QBfile': 'wk_1_revised_QB.csv',
                              'RBfile': 'wk_1_revised_RB.csv',
                              'WRfile': 'wk_1_revised_WR.csv',
                              'TEfile': 'wk_1_revised_TE.csv',
                              'DSTfile': 'wk_1_revised_DST.csv',
                              'FLXfile': 'wk_1_revised_FLX.csv'}" -m csv_all_data

#2017
pytest -s -v -l --testdata="{'spreadsheetId': '$wk1_2017',
                              'rangeName': 'A1:L1447',
                              'round': 5,
                              'QBfile': 'wk_1_revised_QB.csv',
                              'RBfile': 'wk_1_revised_RB.csv',
                              'WRfile': 'wk_1_revised_WR.csv',
                              'TEfile': 'wk_1_revised_TE.csv',
                              'DSTfile': 'wk_1_revised_DST.csv',
                              'FLXfile': 'wk_1_revised_FLX.csv'}" -m csv_all_data

#2016
pytest -s -v -l --testdata="{'spreadsheetId': '$wk1_2016',
                              'rangeName': 'A1:L1447',
                              'round': 5,
                              'QBfile': 'wk_1_revised_QB.csv',
                              'RBfile': 'wk_1_revised_RB.csv',
                              'WRfile': 'wk_1_revised_WR.csv',
                              'TEfile': 'wk_1_revised_TE.csv',
                              'DSTfile': 'wk_1_revised_DST.csv',
                              'FLXfile': 'wk_1_revised_FLX.csv'}" -m csv_all_data

#2015
pytest -s -v -l --testdata="{'spreadsheetId': '$wk1_2015',
                              'rangeName': 'A1:L1447',
                              'round': 5,
                              'QBfile': 'wk_1_revised_QB.csv',
                              'RBfile': 'wk_1_revised_RB.csv',
                              'WRfile': 'wk_1_revised_WR.csv',
                              'TEfile': 'wk_1_revised_TE.csv',
                              'DSTfile': 'wk_1_revised_DST.csv',
                              'FLXfile': 'wk_1_revised_FLX.csv'}" -m csv_all_data