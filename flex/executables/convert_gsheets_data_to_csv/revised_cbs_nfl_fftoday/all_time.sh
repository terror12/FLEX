#!/bin/bash
# This script is meant to take the Google sheets that we created using the Revised approach.
# Which ofcourse is using just three platforms to collect the data (CBS, NFL, FFToday)
# 1. the first pytest will create a file called revised_<postion>.csv for each postion.
# 2. Every pytest after that will append the data the data into the already created file.
# 3. This will leave us with a .csv for each position containing only the important values we
#    need to analyze the STDs accordingly.
# 4. We can then take the STDs and graph the actual results of the past 5 years to draw conclusions.
#
# TODO: **Big Item** Find a way to update this sheet everytime a new sheet is created. Then have this sheet auto run all sheets to collect the
# TODO: most up to date data and use that to make the decisions.
#

# TODO: Replace all of these spreadsheet ids with the revised google sheet ids just for 2018 & 2019 all others are good
#2019
# pytest -s -v -l --testdata="{'spreadsheetId': '1aOz0lsfyQBuMcwvFBTrVxg9XjP9jdSCFUrFOeD6wU7E', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1Xl9j6RKmwGs2YIGTCk27mrG1CyhSejWxot7_FllEhaI', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1tOHNw70CGQ5Xy7vKyXWug78xFl4rCx7wk56A5vKgByw', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1UWNBOrmsRIdGZVkK_NZj4weQCWKliOuTgbnl9FycPHY', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '18ZS1C2wxla61aiNYeVGH3_aZEEwMVJNmomvOz345DXU', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1g9BhcYcYR_YmzQ-uhvWZ843uLfZWIkVL3TfegZO6blA', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1mUyihdTMuutiY9sWdCjROvhOn5orRHIHPOmuy1Y6AJs', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1_zXGA8U4p77r5OrYxvxNMoMiUgyjl_eJSnZAX3P9-wI', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1a9QlQnU2d2_0onGibxr1iKriVq3MXDf9QZMX1rI2Z-w', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1pruJurVEsl4fqTwFNM-kcDTUuzHXt4TyzvP2qGNzvuA', 'rangeName': 'A1:L1447'}" -m csv_all_data

#2018
pytest -s -v -l --testdata="{'spreadsheetId': '1mXpMa-WNZCTf-E9w7T413fmWIORTV73wZ-PrEI0_mPg', 'rangeName': 'A1:L1447'}" -m csv_all_data
TODO: update the rest of 2018 spreadsheet ids
# pytest -s -v -l --testdata="{'spreadsheetId': '145FTWwBc1Buf6qyLXV8sbaka4j9y0N2gN4R6D4tZDMk', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1C_NEMW7ZpQWZUV1gefvChaPyE7rD2WtDQRI0idmP6V4', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1bbrtNbTEW5fITJNEmGFuE2iUEZ5iiTpf8pI9urbspoA', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1I1WRYSYLH0RPbfiMtbx0ku3aXXHi4IrKKLDaD5tepMg', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '19T8CG0xnO1WedoSpSxosflZKlCk2lRe8OschbvkcE7I', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1sBI55bo-xZccZlUN9K-6BErY16MS6BzWjstgCQaa2JA', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '19ljuqeLkifFMRMPuacm6AZ4pPtOFh1qWVCf5msw2ZYA', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '10d8uP2vBPde8bLm04EN8Vv277XiKBvYH38yQCibtD5Y', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1OmAO0Zy1OkT5A4RcAQgv6Td7EJeuSvu3AMQoVcL4fWw', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '15bgANJ3cYrQxOt3chXljIMjaNf7w4R42Zj78IM3Nj2s', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1KiraUhg126GWnxYt5YNTlPUdDFE3E5QPNkyB_nTdMrk', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1H1twpgSK6iMkRQu0sRRMbdd5trCpEJrX74xh1g2ZEOU', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1m-KkWRrpHej_tOmow38VJUduLNNCcjWhynhK1zQ17gI', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '13-QsTCPMLzss_XzThAHYUeQkHtLKgwmfNnx85-boWBk', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1peJIl29TH7QfwQasO_kEcFb4sb9u9B9ndIWXVGQWr7Q', 'rangeName': 'A1:L1447'}" -m csv_all_data
# pytest -s -v -l --testdata="{'spreadsheetId': '1DYYQoXfcHriyvSX-qS5-U3W62tSswFcVYWcUS-H5BGw', 'rangeName': 'A1:L1447'}" -m csv_all_data

#2017
pytest -s -v -l --testdata="{'spreadsheetId': '1Ax0pYiPbPj-UtbBdZkwqfbrWWIEqxsstBHOGG5D0R68', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1d1tz2DSQ3yZEiFO-s4w6g1YON_NiN38m-NpO9XHV0nc', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1zkOufQB0gR8_hk6hLTV7clcE_Qu1HbXk5YtJODSYG8w', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1K2rdhPeMlspmsrCtzgWtss6oHWFEDlEzh_2vVXK34vk', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1YyMCVVjpfEz_HXaTrfJIdeXjSmYhqYTux1BzqAh4Wso', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1BS4l5g5sKgqVUPmaqmEeV0csK5IkJG3mDyl42J7NOHE', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1FX8IznjCL5fHHUWNTnTOPyx-ojeCClVa3ZO96HHZt5w', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '18-Iq0vkmnvbaRUThbbS8fDWm7a6gl5FnPX7GiWzWe0I', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1znuIaZ6EX5ahWYys-CRWJmkq_Q_qgdvayt4bE_e8jC0', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1dUt_7HxFijMDrApY4HqS1IjJa9j4t6HLVW7QGlbYBJY', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1o1YgU0YRSiuiH_CMCv00VUvE5lN1cTCbYgQ8qHI2Las', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '15KZ0k38MrcOZlG7VyjXRW3XjlEmtjBlmLVGGZ4OvpdQ', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1I3kQ24LMGKpaflkLLZaMDIc38EMeauaIk-3dFqRLAOg', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1AUS5MiwX4yCgS1wkXBEslDiJ4SZy93nYoxKYbNC7p4U', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1nt7xUbd_gzlafCcQcOK7YIjDO4LmgFEWs4HbYz2v4Q8', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1GkmoZTAhOTJ60uMCUoqBDWC9mwJ8bSbrVO3-csH2HOw', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1uOkfFB7vS5hpx2B2cb8uSl5tTRTNGh9CVHMgRAuR-DA', 'rangeName': 'A1:L1447'}" -m csv_all_data

#2016
pytest -s -v -l --testdata="{'spreadsheetId': '18qnMqE1QX8sTLxLSUw6AVulhBqE5v_3sDn1BRipRJ80', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '15ct4Hfn235xforQAB5GJh4EmfB1kCop6cLYbtmhJLOA', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '19fXX9z03z3tCGkh0TAIAfeKy47NsfUjkRvGbQcBZtbM', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1ubVojcFz19wbvWFpW40x0lRNW45uQNqPaxmA9S4v6ZU', 'rangeName': 'A1:L1447'}" -m csv_all_data
# TODO: need to fix Revised 2016 Week5 STD
pytest -s -v -l --testdata="{'spreadsheetId': '1sreIkvzmnB8TJJg690vkNflXXUGuR7hRIwx_6UGx9a8', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1C4e4DuVAV0Df94--UeIAOzp-6UXQrjr6ptnYlZFZ3Fw', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1Tk2HXBS-Ad4nKyBkNL5jp8LhSV0JuJ8TPeds9pcoZQ0', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1IdgzfmIhYKvygz0qNsOkchCabloAHgMX3BunB2A6reI', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1UpDZpiyzRW7pjc6YEe2i8N6wkeAO61qZocHOAzdqmwI', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1aidHjvsbXiXWALhn9VxC5o54D9ZfBA3KbB8JTtPy7-M', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1YLZpLo8Vo99VdcFymk5z0G2A6gD76zOL6syxtn8VRUU', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1FdfpHXacpUWkcNHIQpSZCEc1FNrGyDErMJNGZqLeLoQ', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1KTVy5LDvjJXGcZHivWgPtROe1po-LwmO5NyBmmyNfAQ', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1GKYzPg0X6vT_LGvWHjBDYz3hyxNZN8L0wu2KzyXO15w', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1UpDZpiyzRW7pjc6YEe2i8N6wkeAO61qZocHOAzdqmwI', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1SWcgq6wBLPkpOz-1-sHkO0_fQM1W0QlwqfVJXW7YFzY', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1WG0c_nKSFTqVUOOpb-X1Jmv_MOs_E4_Iu6S_vBexSaA', 'rangeName': 'A1:L1447'}" -m csv_all_data

#2015
pytest -s -v -l --testdata="{'spreadsheetId': '1iM99sD2ylm3Ny3Pksoz3lFcp1jgUucY9KW-BsYfBTjs', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1DoQc3yC3YY9i2OP-hFtjVU_SsmdJzU-cpc9DOvuFZ5s', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1_UXVmTwveJnU35YtjOFZPExGNQGcZ0YGRHfJkqmuAQ0', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1H6kohzf8O5hd5sJVpGLMPf71UU1z3j6cnaeJN1qk_OQ', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1i1DmgmJOoikIhQ4YdXg_cuMKSvEe1Av-RsbIdSHFnyo', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1EOLMZ3nTE_Q_V7bfqZvbS4Udw_d5s0QAQ8k9KIivPVU', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1FuQlkEb09cBXoTKRmCkKu89hkSOxTz4NA79zyr41j4o', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1fI9V56aVMVM9uY1Jggvt-pv2CoqZHFeM0W__Oy78p4E', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1GYdPvKvH_gmbi_GKIglBkLlpomNUULTgEK43RJ1W_qo', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1plp3eDm6wE_m9JqZqmHO2pADf4XirKgAbB2efRkrEO4', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1Wi0Oo6QelmPvdiaefoiSLeTARzloH__yM694iHHBwYo', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1gkmRkkGwNmmerWb-tAci5ah26oI9mjc5AwqGq_e-wFs', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1LH9lQGHgONiDb-IrJK7TY8EqAVvHskPHeB655O53ghU', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1hOZUeCn8BjbUhapsZNU5fhVt6DnpJbrAFEwDjIBd7e8', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1d0BcSQJ-5QHtKmVzhheKt1KBAAcxGPKco5yJ0AOXAw4', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1SWcgq6wBLPkpOz-1-sHkO0_fQM1W0QlwqfVJXW7YFzY', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1WG0c_nKSFTqVUOOpb-X1Jmv_MOs_E4_Iu6S_vBexSaA', 'rangeName': 'A1:L1447'}" -m csv_all_data
