#!/bin/bash

cd /home/acterror12/FLEX && source py3_venv_flex/bin/activate && cd py3_venv_flex/flex

Rscript tests/tier-0/testscrape/test_scrape_rotoguru 12 2019 post_FanDuel_Salaries_2019_week12

pytest -s -v -l --testdata="{'projections': '/home/acterror12/FLEX/FLEX/flex/ffa_proj/Projections_2019_week12', 'FanDuel_Salaries': '/home/acterror12/FLEX/FLEX/flex/FanDuel_proj/post_FanDuel_Salaries_2019_week12', 'Sheet_Name': 'Post 2019 Week12 STD'}" -m import_historic_data

pytest -s -v -l --testdata="{'spreadsheetId': '11cF3yBe78g0a9I28NXsTYpn9G44PjEy9RxWlYFZ6vpE', 'rangeName': 'A1:L1447'}" -m update_points