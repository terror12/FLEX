#!/bin/bash
# This script is meant to take the Google sheets that we created using the Revised approach.
# Which ofcourse is using just three platforms to collect the data (CBS, NFL, FFToday)
# 1. the first pytest will create a file called revised_<postion>.csv for each postion.
# 2. Every pytest after that will append the data the data into the already created file.
# 3. This will leave us with a .csv for each position containing only the important values we
#    need to analyze the STDs accordingly.
# 4. We can then take the STDs and graph the actual results of the past 5 years to draw conclusions.


# TODO: Replace all of these spreadsheet ids with the revised google sheet ids
#2019
pytest -s -v -l --testdata="{'spreadsheetId': '1aOz0lsfyQBuMcwvFBTrVxg9XjP9jdSCFUrFOeD6wU7E', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1Xl9j6RKmwGs2YIGTCk27mrG1CyhSejWxot7_FllEhaI', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1tOHNw70CGQ5Xy7vKyXWug78xFl4rCx7wk56A5vKgByw', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1UWNBOrmsRIdGZVkK_NZj4weQCWKliOuTgbnl9FycPHY', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '18ZS1C2wxla61aiNYeVGH3_aZEEwMVJNmomvOz345DXU', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1g9BhcYcYR_YmzQ-uhvWZ843uLfZWIkVL3TfegZO6blA', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1mUyihdTMuutiY9sWdCjROvhOn5orRHIHPOmuy1Y6AJs', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1_zXGA8U4p77r5OrYxvxNMoMiUgyjl_eJSnZAX3P9-wI', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1a9QlQnU2d2_0onGibxr1iKriVq3MXDf9QZMX1rI2Z-w', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1pruJurVEsl4fqTwFNM-kcDTUuzHXt4TyzvP2qGNzvuA', 'rangeName': 'A1:L1447'}" -m csv_all_data

#2018
pytest -s -v -l --testdata="{'spreadsheetId': '1h6Utm5FyaNAqB4sorzrv2eySe5U9nnzfb-LewcKVkt4', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '145FTWwBc1Buf6qyLXV8sbaka4j9y0N2gN4R6D4tZDMk', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1C_NEMW7ZpQWZUV1gefvChaPyE7rD2WtDQRI0idmP6V4', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1bbrtNbTEW5fITJNEmGFuE2iUEZ5iiTpf8pI9urbspoA', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1I1WRYSYLH0RPbfiMtbx0ku3aXXHi4IrKKLDaD5tepMg', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '19T8CG0xnO1WedoSpSxosflZKlCk2lRe8OschbvkcE7I', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1sBI55bo-xZccZlUN9K-6BErY16MS6BzWjstgCQaa2JA', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '19ljuqeLkifFMRMPuacm6AZ4pPtOFh1qWVCf5msw2ZYA', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '10d8uP2vBPde8bLm04EN8Vv277XiKBvYH38yQCibtD5Y', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1OmAO0Zy1OkT5A4RcAQgv6Td7EJeuSvu3AMQoVcL4fWw', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '15bgANJ3cYrQxOt3chXljIMjaNf7w4R42Zj78IM3Nj2s', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1KiraUhg126GWnxYt5YNTlPUdDFE3E5QPNkyB_nTdMrk', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1H1twpgSK6iMkRQu0sRRMbdd5trCpEJrX74xh1g2ZEOU', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1m-KkWRrpHej_tOmow38VJUduLNNCcjWhynhK1zQ17gI', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '13-QsTCPMLzss_XzThAHYUeQkHtLKgwmfNnx85-boWBk', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1peJIl29TH7QfwQasO_kEcFb4sb9u9B9ndIWXVGQWr7Q', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1DYYQoXfcHriyvSX-qS5-U3W62tSswFcVYWcUS-H5BGw', 'rangeName': 'A1:L1447'}" -m csv_all_data

#2017
pytest -s -v -l --testdata="{'spreadsheetId': '1y4p3N0mys7FaRNU7sFkBhs5_WiKsErzqSYyWzbdd2uE', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1Z0JknDE54DSUQLKHs1qLapRzjvPEKfZpT17xKSJDUxM', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1VnSJmOBZqL1WVPcnBG8oUiSMnDTqGdUFP_ymnDQP428', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '19QvowYm41YE1y7QqGCsCwyp0GzrwV30jZBBdgAyXjzc', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1a83IzYdHqmN_j_kacPbJ5D10UdK13Q5LCMzmDH3UEHM', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1fK0EoRvLCYEePovWuYBRJtVr4D_MJuei8R4oW7O_3Qo', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1NyOiGdwpC2-gpdbZ2DZkII5bIWXD0zyMEcf7ItwCbtA', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1erp5q2PesAVR0bwKdzXkkFJkk5ra5AxdLwxn6pqV0FQ', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1zub5YhnGWxADslPIPgbaz-g0eR96T7d40EhUC0KfWa8', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1BlcPL02ANcrsM2ZLZ3eVbhuKii66DRmIoPvrPhFVUIw', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1GQO0jBG8zH0o_huMD6fiZy0m3rW38jyWM3VvQYCcJkk', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1PSLbz7RRvRGTTm7K5PeLaTtgeC3A19jpWXqjqL8qPms', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1EL1WfbGr1kHAn5geNs5t0D88H1rHCGVeuYyuNHMdjlk', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1d8WTRlyPIF80k63oJlkMUVZfVaamgiKTrnebiU0FpRI', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1OgbhNVo41hpN988I0ElPgR4mXDPeyO9hiaskJ2RHHRI', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1WCZdPQgy8VXwUjh_xLxb7g542vPfg75AupZy4W0S50c', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1AJACm-x4a5kNLZnJ7mNj7v2d_bfLT6epszKXNzhbuEQ', 'rangeName': 'A1:L1447'}" -m csv_all_data

#2016
pytest -s -v -l --testdata="{'spreadsheetId': '1zrLpLemIyu3sKElUAbJbI2EllHPhuS9ku-97r-nEYvQ', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1zs5VZT-blOt-4qGsIbP3IhkiDDqgDdrz9yKG4va7nhk', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1nX56WWvf_d5LsByrHEc07oEN_aiiev_xzmpDKNIdXdY', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1FSu_QBAU3Icf6eIWoAlFAG_uHYj26wILYkR3zszpxag', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1gGUaBVXjx0o-ndmawWvBhCiuh--OSQkCvTBEV3YZG4g', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1g3o5AoF5QlNhbBn_vsjirOgVybKt3K1rWFlUWzPORUo', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1syahsfFgzbO7kVpjxcCrju7MG2k1RWaytwt-rrS0hJA', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '11G3wMvKZPO7yrs5_uqreZH6WR9IJ51V53-9Ay_wkb2s', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '15owXQK3zhJwSx2hLp-Lq60FMkRA3zg7CnWvWvuxKRro', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1Vkx5ub9NIDy6vEfuH-0jb_bRLzPhz3H2fC6nfXjtXi8', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1Xw2i2ps5cmfUSgSieEjiy5ikzJKTIONAk9YRfpmER5Y', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1JSMJOZqJNIBVzMl0A2G5ASMG-yy5a2G_A2wxl8ofn7g', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1KMDEwSjOgBqOd4RlhSFRNR3ZhWRkJmDkmBT3k24aZZ4', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1Tc0c3NWqDVEK7ss7jZroS6HdEYoyE9Rzf3s44jVFcl4', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1r6gOA2FP_LzUCGjyG_3wbEZoCegb47dxHT-lO4Tkw4Y', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1ukgMOMcHov7W_IhHD3uELq5b7yTC07IfUdiN9jYkWpw', 'rangeName': 'A1:L1447'}" -m csv_all_data
pytest -s -v -l --testdata="{'spreadsheetId': '1pfE0jD6KiX4Ea1t9sdIcd9Ip2GVhQO7GHS2trw9Jk_A', 'rangeName': 'A1:L1447'}" -m csv_all_data

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
