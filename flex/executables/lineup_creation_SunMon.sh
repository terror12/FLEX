rm platinum.csv
rm gold.csv
rm silver.csv
rm bronze.csv
rm *tourny*

while [ ! -f platinum.csv ]
do
  # platinum.csv
  pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '$1', 'rangeName': 'A1:L1447', 'QB_std': 1.8, 'RB_std': 1.6, 'WR_std': 2.2, 'TE_std': 1.1, 'DST_std': 2.1, 'FLX_std': 1.5, 'QB_std2': 2.0, 'RB_std2': 1.7, 'WR_std2': 2.0, 'TE_std2': 0.9, 'DST_std2': 2.7, 'FLX_std2': 1.6, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'platinum_tourny.csv', 'collect_second_csv': 'gold_backup_tourny.csv', 'count': '69', 'pairing': True, 'slate': 'SUN-MON'}" -m fd_entry
  pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': $1, 'rangeName': 'A1:L1447', 'QB_std': 1.1, 'RB_std': 1.5, 'WR_std': 1.9, 'TE_std': 1.0, 'DST_std': 1.0, 'FLX_std': 1.4, 'QB_std2': 1.7, 'RB_std2': 1.3, 'WR_std2': 2.3, 'TE_std2': 0.7, 'DST_std2': 2.0, 'FLX_std2': 1.3, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'silver.csv', 'collect_second_csv': 'bronze_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry
done
cat platinum.csv

# # gold.csv
# pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '$1', 'rangeName': 'A1:L1447', 'QB_std': 2.0, 'RB_std': 1.7, 'WR_std': 2.0, 'TE_std': 0.9, 'DST_std': 2.7, 'FLX_std': 1.6,  'QB_std2': 1.1, 'RB_std2': 1.5, 'WR_std2': 1.9, 'TE_std2': 1.0, 'DST_std2': 1.0, 'FLX_std2': 1.4, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'gold.csv', 'collect_second_csv': 'silver_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry
# # silver.csv
# pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '$1', 'rangeName': 'A1:L1447', 'QB_std': 1.1, 'RB_std': 1.5, 'WR_std': 1.9, 'TE_std': 1.0, 'DST_std': 1.0, 'FLX_std': 1.4, 'QB_std2': 1.7, 'RB_std2': 1.3, 'WR_std2': 2.3, 'TE_std2': 0.7, 'DST_std2': 2.0, 'FLX_std2': 1.3, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'silver.csv', 'collect_second_csv': 'bronze_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry
# # bronze.csv
# pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '$1', 'rangeName': 'A1:L1447', 'QB_std': 1.7, 'RB_std': 1.3, 'WR_std': 2.3, 'TE_std': 0.7, 'DST_std': 2.0, 'FLX_std': 1.3, 'QB_std2': 1.8, 'RB_std2': 1.6, 'WR_std2': 2.2, 'TE_std2': 1.1, 'DST_std2': 2.1, 'FLX_std2': 1.5, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'bronze.csv', 'collect_second_csv': 'platinum_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry
# # tourny.csv
# pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '$1', 'rangeName': 'A1:L1447', 'QB_std': 1.8, 'RB_std': 1.6, 'WR_std': 2.2, 'TE_std': 1.1, 'DST_std': 2.1, 'FLX_std': 1.5, 'QB_std2': 2.0, 'RB_std2': 1.7, 'WR_std2': 2.0, 'TE_std2': 0.9, 'DST_std2': 2.7, 'FLX_std2': 1.6, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'platinum_tourny.csv', 'collect_second_csv': 'gold_backup_tourny.csv', 'count': '69', 'pairing': True, 'slate': 'SUN-MON'}" -m fd_entry
