rm platinum.csv
rm gold.csv
rm silver.csv
rm bronze.csv
rm *tourny*


pfstd="1.5"
gfstd="1.6"
sfstd="1.4"
bfstd="1.3"
tfstd="1.5"

twrstd="2.2"

change="0.1"

while [ ! -f platinum.csv ] && [ $pfstd != 0 ]
do
  pytest -x -s -v -l --testdata="{'spreadsheetId': '1iVejGgLoQbW8XrxfGmVxKJBqAAbnhZthnmiunXyrg8E', 'rangeName': 'A1:L1447', 'QB_std': 1.8, 'RB_std': 1.6, 'WR_std': 2.2, 'TE_std': 1.1, 'DST_std': 2.1, 'FLX_std': $pfstd, 'QB_std2': 2.0, 'RB_std2': 1.7, 'WR_std2': 2.0, 'TE_std2': 0.9, 'DST_std2': 2.7, 'FLX_std2': 1.6, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'platinum.csv', 'collect_second_csv': 'gold_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry
  pfstd=$(echo "$pfstd - $change" | bc)
  echo $pfstd
done
  cat platinum.csv

while [ ! -f gold.csv ] && [ $gfstd != 0 ]
do
  pytest -x -s -v -l --testdata="{'spreadsheetId': '1iVejGgLoQbW8XrxfGmVxKJBqAAbnhZthnmiunXyrg8E', 'rangeName': 'A1:L1447', 'QB_std': 2.0, 'RB_std': 1.7, 'WR_std': 2.0, 'TE_std': 0.9, 'DST_std': 2.7, 'FLX_std': $gfstd,  'QB_std2': 1.1, 'RB_std2': 1.5, 'WR_std2': 1.9, 'TE_std2': 1.0, 'DST_std2': 1.0, 'FLX_std2': 1.4, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'gold.csv', 'collect_second_csv': 'silver_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry
  gfstd=$(echo "$gfstd - $change" | bc)
  echo $gfstd
done
  cat gold.csv


while [ ! -f silver.csv ] && [ $sfstd != 0 ]
do
  pytest -x -s -v -l --testdata="{'spreadsheetId': '1iVejGgLoQbW8XrxfGmVxKJBqAAbnhZthnmiunXyrg8E', 'rangeName': 'A1:L1447', 'QB_std': 2.0, 'RB_std': 1.5, 'WR_std': 1.9, 'TE_std': 1.0, 'DST_std': 1.0, 'FLX_std': $sfstd, 'QB_std2': 1.7, 'RB_std2': 1.3, 'WR_std2': 2.3, 'TE_std2': 0.7, 'DST_std2': 2.0, 'FLX_std2': 1.3, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'silver.csv', 'collect_second_csv': 'bronze_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry
  sfstd=$(echo "$sfstd - $change" | bc)
  echo $sfstd
done
  cat silver.csv

while [ ! -f bronze.csv ] && [ $bfstd != 0 ]
do
  pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '1iVejGgLoQbW8XrxfGmVxKJBqAAbnhZthnmiunXyrg8E', 'rangeName': 'A1:L1447', 'QB_std': 1.7, 'RB_std': 1.3, 'WR_std': 2.3, 'TE_std': 0.7, 'DST_std': 2.0, 'FLX_std':  $bfstd, 'QB_std2': 1.8, 'RB_std2': 1.6, 'WR_std2': 2.2, 'TE_std2': 1.1, 'DST_std2': 2.1, 'FLX_std2': 1.5, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'bronze.csv', 'collect_second_csv': 'platinum_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry
  bfstd=$(echo "$bfstd - $change" | bc)
  echo $bfstd
done
  cat bronze.csv

while [ ! -f platinum_tourny.csv ] && [ $tfstd != 0 ]
do
  pytest -x -s -v -l --testdata="{'spreadsheetId': '1iVejGgLoQbW8XrxfGmVxKJBqAAbnhZthnmiunXyrg8E', 'rangeName': 'A1:L1447', 'QB_std': 1.8, 'RB_std': 1.6, 'WR_std': $twrstd, 'TE_std': 1.1, 'DST_std': 2.1, 'FLX_std': $tfstd, 'QB_std2': 2.0, 'RB_std2': 1.7, 'WR_std2': 2.0, 'TE_std2': 0.9, 'DST_std2': 2.7, 'FLX_std2': 1.6, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'platinum_tourny.csv', 'collect_second_csv': 'gold_backup_tourny.csv', 'count': '69', 'pairing': True, 'slate': 'SUN-MON'}" -m fd_entry
  tfstd=$(echo "$tfstd - $change" | bc)
  twrstd=$(echo "$twrstd - $change" | bc)
  echo $tfstd
  echo $twrstd
done
  cat platinum_tourny.csv

# # gold.csv
# pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '$1', 'rangeName': 'A1:L1447', 'QB_std': 2.0, 'RB_std': 1.7, 'WR_std': 2.0, 'TE_std': 0.9, 'DST_std': 2.7, 'FLX_std': 1.6,  'QB_std2': 1.1, 'RB_std2': 1.5, 'WR_std2': 1.9, 'TE_std2': 1.0, 'DST_std2': 1.0, 'FLX_std2': 1.4, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'gold.csv', 'collect_second_csv': 'silver_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry
# # silver.csv
# pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '$1', 'rangeName': 'A1:L1447', 'QB_std': 1.1, 'RB_std': 1.5, 'WR_std': 1.9, 'TE_std': 1.0, 'DST_std': 1.0, 'FLX_std': 1.4, 'QB_std2': 1.7, 'RB_std2': 1.3, 'WR_std2': 2.3, 'TE_std2': 0.7, 'DST_std2': 2.0, 'FLX_std2': 1.3, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'silver.csv', 'collect_second_csv': 'bronze_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry
# # bronze.csv
# pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '$1', 'rangeName': 'A1:L1447', 'QB_std': 1.7, 'RB_std': 1.3, 'WR_std': 2.3, 'TE_std': 0.7, 'DST_std': 2.0, 'FLX_std': 1.3, 'QB_std2': 1.8, 'RB_std2': 1.6, 'WR_std2': 2.2, 'TE_std2': 1.1, 'DST_std2': 2.1, 'FLX_std2': 1.5, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'bronze.csv', 'collect_second_csv': 'platinum_backup.csv', 'count': '69', 'pairing': False, 'slate': 'SUN-MON'}" -m fd_entry
# # tourny.csv
# pytest -x --pdb -s -v -l --testdata="{'spreadsheetId': '$1', 'rangeName': 'A1:L1447', 'QB_std': 1.8, 'RB_std': 1.6, 'WR_std': 2.2, 'TE_std': 1.1, 'DST_std': 2.1, 'FLX_std': 1.5, 'QB_std2': 2.0, 'RB_std2': 1.7, 'WR_std2': 2.0, 'TE_std2': 0.9, 'DST_std2': 2.7, 'FLX_std2': 1.6, 'min_sal': 58000, 'master_csv': 'future.csv', 'master_csv2': 'future.csv', 'collect_master_csv': 'platinum_tourny.csv', 'collect_second_csv': 'gold_backup_tourny.csv', 'count': '69', 'pairing': True, 'slate': 'SUN-MON'}" -m fd_entry
