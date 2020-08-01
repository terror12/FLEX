After we Download Fanduel slates and ffanalytics projections we will do the following.

This will be what the Cron job will be doing week to week

1. This code will be cloned onto our Heroku server
2. a Cron job will be put in place, this job could maybe kick off ansible playbook or shell script to do the following.
3. The webscraping will download slate data and projection data.
4. The code to create a Google sheet will be executed
# Create Google Sheet (Pathing may not be correct here)
pytest -s -v -l --testdata="{'projections': 'flex/ffa_proj/Projections_2019_week4', 'FanDuel_Salaries': 'flex/FanDuel_proj/FanDuel_Salaries_2019_week4', 'Sheet_Name': '2019 Week4 STD'}" -m import_data
5. That Google sheet ID will be output and gathered to feed into the lineup generation code.
# Create platinum w/ gold backup
pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '1FcacnoanHEromRSdTrIul_8zFVOjCLJNr6fxYpXHcVo', 'rangeName': 'A1:L1447', 'QB_std': 1.8, 'RB_std': 1.6, 'WR_std': 2.2, 'TE_std': 1.1, 'DST_std': 2.1, 'FLX_std': 1.5, 'QB_std2': 2.0, 'RB_std2': 1.7, 'WR_std2': 2.0, 'TE_std2': 0.9, 'DST_std2': 2.7, 'FLX_std2': 1.6, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'platinum.csv', 'collect_second_csv': 'gold_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry

# Create gold w/ silver backup
pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '1FcacnoanHEromRSdTrIul_8zFVOjCLJNr6fxYpXHcVo', 'rangeName': 'A1:L1447', 'QB_std': 2.0, 'RB_std': 1.7, 'WR_std': 2.0, 'TE_std': 0.9, 'DST_std': 2.7, 'FLX_std': 1.6,  'QB_std2': 1.1, 'RB_std2': 1.5, 'WR_std2': 1.9, 'TE_std2': 1.0, 'DST_std2': 1.0, 'FLX_std2': 1.4, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'gold.csv', 'collect_second_csv': 'silver_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry

# Create silver w/ bronze backup
pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '1FcacnoanHEromRSdTrIul_8zFVOjCLJNr6fxYpXHcVo', 'rangeName': 'A1:L1447', 'QB_std': 1.1, 'RB_std': 1.5, 'WR_std': 1.9, 'TE_std': 1.0, 'DST_std': 1.0, 'FLX_std': 1.4, 'QB_std2': 1.7, 'RB_std2': 1.3, 'WR_std2': 2.3, 'TE_std2': 0.7, 'DST_std2': 2.0, 'FLX_std2': 1.3, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'silver.csv', 'collect_second_csv': 'bronze_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry

# Create bronze with platinum backup
pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '1FcacnoanHEromRSdTrIul_8zFVOjCLJNr6fxYpXHcVo', 'rangeName': 'A1:L1447', 'QB_std': 1.7, 'RB_std': 1.3, 'WR_std': 2.3, 'TE_std': 0.7, 'DST_std': 2.0, 'FLX_std': 1.3, 'QB_std2': 1.8, 'RB_std2': 1.6, 'WR_std2': 2.2, 'TE_std2': 1.1, 'DST_std2': 2.1, 'FLX_std2': 1.5, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'bronze.csv', 'collect_second_csv': 'platinum_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry

6. Once the lineups are created we will update the postregsql database table.
# Update ffautoduel_platinum table
pytest -s -v -l --testdata="{'user': 'ascerra', 'password':'<Redacted>', 'dbname':'flex', 'tablename':'ffautoduel_platinum', 'result': 'platinum.csv'}" -m update_db

# Update ffautoduel_gold table
pytest -s -v -l --testdata="{'user': 'ascerra', 'password':'<Redacted>', 'dbname':'flex', 'tablename':'ffautoduel_gold', 'result': 'gold.csv'}" -m update_db

7. The application will retrieve data from this table when the user clicks the button to generate data.
