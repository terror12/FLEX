from glusto.core import Glusto as g
# from flex.lib.connect.connect_to_sheets import SheetsConnector
# from flex.lib.data_clean.fix_df import FixUpDf
# from flex.lib.data_clean.remove import Remove
# from flex.lib.generate_lineup.closest_to_num import ClosestToNum
import pytest
# import random
import pandas as pd
# import csv
# import matplotlib.pyplot as plt
# import plotly.express as px
# import plotly.graph_objects as go
# import numpy as np
import os
# from plotly.subplots import make_subplots


class TestSTDPerPosition:

    g.add_log(g.log, filename='./logs/STDPerPositionLog')

    @pytest.mark.find_avg
    def test_find_average(self, print_logging, deftestdata):
        """
        Seperate the master csv into STD categories and find the average.
        :param print_logging:
        :return: a new average csv to graph
        """
        master_csv = deftestdata['master_csv']
        df = pd.read_csv(master_csv)
        g.log.info(df.describe())

        df_by_std = df.groupby('sdPts')
        df_by_std = df_by_std['Actual_Points']
        std_mean = df_by_std.mean()

        std_mean.to_csv('Mean' + master_csv)

        # g.log.info(df_by_std.describe().head(500))

    @pytest.mark.csv_all_data
    def test_create_csv_all_data(self, deftestdata, rawDataframe, full_dataframe_prep_for_data, round=0):
        """
        This test will create a single csv of each Position using a Google sheet as input
        The result of this csv will be a file containing all relevant information needed for
        charting and analyizing specific STD's
        This only is here to help us find the best STD and do research not create lineups!
        :param rawDataframe:
        :param print_logging:
        :param full_dataframe_prep:
        :return:
        """
        # g.log.info('Instantiate Closest_to_num object')
        # Closest_to_num = ClosestToNum()

        g.log.info('Instantiate the positional dataframes')
        QB, RB, WR, TE, FLX, DST = full_dataframe_prep_for_data

        # Instantiate the file names that get assigned at the command line
        QBfile = deftestdata['QBfile']
        RBfile = deftestdata['RBfile']
        WRfile = deftestdata['WRfile']
        TEfile = deftestdata['TEfile']
        DSTfile = deftestdata['DSTfile']
        FLXfile = deftestdata['FLXfile']

        # TODO: change STD value to hundreths 22.42
        QB = QB.round(round)
        RB = RB.round(round)
        WR = WR.round(round)
        TE = TE.round(round)
        DST = DST.round(round)
        FLX = FLX.round(round)
        # g.log.info(type(QB))
        # TODO: list from highest to lowest Actual points
        # g.log.info(QB)

        # TODO: figure out how to analyze the data, we need to find which STD comes up the highest most frequently.

        with open(QBfile, 'a') as f:
            if os.stat(QBfile).st_size == 0:
                QB.to_csv(f)
            else:
                QB.to_csv(f, header=False)
        with open(RBfile, 'a') as f:
            if os.stat(RBfile).st_size == 0:
                RB.to_csv(f)
            else:
                RB.to_csv(f, header=False)
        with open(WRfile, 'a') as f:
            if os.stat(WRfile).st_size == 0:
                WR.to_csv(f)
            else:
                WR.to_csv(f, header=False)
        with open(TEfile, 'a') as f:
            if os.stat(TEfile).st_size == 0:
                TE.to_csv(f)
            else:
                TE.to_csv(f, header=False)
        with open(DSTfile, 'a') as f:
            if os.stat(DSTfile).st_size == 0:
                DST.to_csv(f)
            else:
                DST.to_csv(f, header=False)
        with open(FLXfile, 'a') as f:
            if os.stat(FLXfile).st_size == 0:
                FLX.to_csv(f)
            else:
                FLX.to_csv(f, header=False)
