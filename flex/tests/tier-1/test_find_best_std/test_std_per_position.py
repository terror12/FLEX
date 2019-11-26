from glusto.core import Glusto as g
from flex.lib.connect.connect_to_sheets import SheetsConnector
from flex.lib.data_clean.fix_df import FixUpDf
from flex.lib.data_clean.remove import Remove
from flex.lib.generate_lineup.closest_to_num import ClosestToNum
import pytest
import random
import pandas as pd
import csv
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os
from plotly.subplots import make_subplots

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

        #g.log.info(df_by_std.describe().head(500))



    @pytest.mark.csv_all_data
    def test_create_csv_all_data(self, rawDataframe, print_logging, full_dataframe_prep_for_data):
        """
        This test will create a single csv of all QB data points
        :param rawDataframe:
        :param print_logging:
        :param full_dataframe_prep:
        :return:
        """
        # g.log.info('Instantiate Closest_to_num object')
        # Closest_to_num = ClosestToNum()

        g.log.info('Instantiate the positional dataframes')
        QB, RB, WR, TE, FLX, DST = full_dataframe_prep_for_data

        # TODO: change STD value to hundreths 22.42
        QB = QB.round(1)
        RB = RB.round(1)
        WR = WR.round(1)
        TE = TE.round(1)
        DST = DST.round(1)
        FLX = FLX.round(1)
        #g.log.info(type(QB))
        # TODO: list from highest to lowest Actual points
        #g.log.info(QB)

        # TODO: figure out how to analyze the data, we need to find which STD comes up the highest most frequently.


        with open('fullQB.csv', 'a') as f:
            if os.stat('fullQB.csv').st_size == 0:
                QB.to_csv(f)
            else:
                QB.to_csv(f, header=False)
        with open('fullRB.csv', 'a') as f:
            if os.stat('fullRB.csv').st_size == 0:
                RB.to_csv(f)
            else:
                RB.to_csv(f, header=False)
        with open('fullWR.csv', 'a') as f:
            if os.stat('fullWR.csv').st_size == 0:
                WR.to_csv(f)
            else:
                WR.to_csv(f, header=False)
        with open('fullTE.csv', 'a') as f:
            if os.stat('fullTE.csv').st_size == 0:
                TE.to_csv(f)
            else:
                TE.to_csv(f, header=False)
        with open('fullDST.csv', 'a') as f:
            if os.stat('fullDST.csv').st_size == 0:
                DST.to_csv(f)
            else:
                DST.to_csv(f, header=False)
        with open('fullFLX.csv', 'a') as f:
            if os.stat('fullFLX.csv').st_size == 0:
                FLX.to_csv(f)
            else:
                FLX.to_csv(f, header=False)

    @pytest.mark.graph_select_data
    def test_create_graph_select_data(self, print_logging, deftestdata):
        """
        This test will dgraph each postion all_dta_csvs
        :param rawDataframe:
        :param print_logging:
        :param full_dataframe_prep:
        :return:
        """
        # Scatter Plot for QB
        #
        master_csv = deftestdata['master_csv']
        title = deftestdata['title']
        x = deftestdata['x']
        y = deftestdata['y']
        df = pd.read_csv(master_csv)
        N = 100000
        fig = go.Figure(data=go.Scattergl(
            x=df[x],
            y=df[y],
            mode='markers',
            marker_color=df[y],
            marker=dict(
                color=np.random.randn(N),
                colorscale='jet',
                line_width=0.1
            )
        ))
        fig.update_layout(
            xaxis=dict(
                tickmode='linear',
                title=title,
                dtick=0.1
            )
        )
        fig.show()

    @pytest.mark.dub_graph
    def test_double_graph(self, print_logging, deftestdata):
        """
        This test will dgraph each postion all_dta_csvs
        :param rawDataframe:
        :param print_logging:
        :param full_dataframe_prep:
        :return:
        """

        #one_x = deftestdata['one_x']
        #two_x = deftestdata['two_x']
        #one_y = deftestdata['one_y']
        #two_y = deftestdata['two_y']
        x = deftestdata['x']
        y = deftestdata['y']
        #df = pd.read_csv(file)

        master_csv = deftestdata['master_csv']
        master_csv2 = deftestdata['master_csv2']

        title = deftestdata['title']
        # x = deftestdata['x']
        # y = deftestdata['y']
        df = pd.read_csv(master_csv)
        df2 = pd.read_csv(master_csv2)

        N = 100000

        trace1 = go.Scattergl(
            x=df[x],
            y=df[y],
            mode='markers',
            marker_color='red',
            marker=dict(
                color='red',
                symbol=1,
                line_width=0.1
            )
        )

        trace2 = go.Scattergl(
            x=df2[x],
            y=df2[y],
            mode='markers',
            marker_color='black',
            marker=dict(
                color='black',
                symbol=2,
                line_width=0.1
            )
        )


        data = [trace1, trace2]

        fig = go.Figure(data=data)
        fig.show()

    @pytest.mark.multi_graph
    def test_multi_graph(self, print_logging, deftestdata):
        """
        This test will dgraph each postion all_dta_csvs
        :param rawDataframe:
        :param print_logging:
        :param full_dataframe_prep:
        :return:
        """

        #one_x = deftestdata['one_x']
        #two_x = deftestdata['two_x']
        #one_y = deftestdata['one_y']
        #two_y = deftestdata['two_y']
        x = deftestdata['x']
        y = deftestdata['y']
        #df = pd.read_csv(file)

        master_csv = deftestdata['master_csv']
        master_csv2 = deftestdata['master_csv2']
        master_csv3 = deftestdata['master_csv3']
        master_csv4 = deftestdata['master_csv4']
        title = deftestdata['title']
        # x = deftestdata['x']
        # y = deftestdata['y']
        df = pd.read_csv(master_csv)
        df2 = pd.read_csv(master_csv2)
        df3 = pd.read_csv(master_csv3)
        df4 = pd.read_csv(master_csv4)
        N = 100000

        trace1 = go.Scattergl(
            x=df[x],
            y=df[y],
            mode='markers',
            marker_color='red',
            marker=dict(
                color='red',
                symbol=1,
                line_width=0.1
            )
        )

        trace2 = go.Scattergl(
            x=df2[x],
            y=df2[y],
            mode='markers',
            marker_color='black',
            marker=dict(
                color='black',
                symbol=2,
                line_width=0.1
            )
        )

        trace3 = go.Scattergl(
            x=df3[x],
            y=df3[y],
            mode='markers',
            marker_color='blue',
            marker=dict(
                color='blue',
                symbol=3,
                line_width=0.1
            )
        )

        trace4 = go.Scattergl(
            x=df4[x],
            y=df4[y],
            mode='markers',
            marker_color='purple',
            marker=dict(
                color='purple',
                symbol=4,
                line_width=0.1
            )
        )

        data = [trace1, trace2, trace3, trace4]

        fig = go.Figure(data=data)
        fig.show()

        # layout = go.Layout(
        #     yaxis=dict(
        #     ),
        #     legend=dict(
        #         traceorder="reversed"
        #     ),
        #     yaxis2=dict(
        #         domain=[0.33, 0.66]
        #     ),


        # fig.update_layout(
        #     xaxis=dict(
        #         tickmode='linear',
        #         title=title,
        #         dtick=0.1
        #     )
        # )

        # # Create figure with secondary y-axis
        # fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Add traces
        # fig.add_trace(
        #     go.Scatter(x=df[one_x], y=df[one_y], name="yaxis data"),
        #     secondary_y=False,
        # )
        #
        # fig.add_trace(
        #     go.Scatter(x=df2[two_x], y=df2[two_y], name="yaxis2 data"),
        #     secondary_y=True,
        # )
        #
        # # Add figure title
        # fig.update_layout(
        #     title_text="Double Y Axis Example"
        # )
        #
        # # Set x-axis title
        # fig.update_xaxes(title_text="xaxis title")
        #
        # # Set y-axes titles
        # fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
        # fig.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)
        #
        # fig.show()
        # Scatter Plot for QB
        #
        ### Set your path to the folder containing the .csv files
        # PATH = './'  # Use your path
        #
        # ### Fetch all files in path
        # fileNames = os.listdir(PATH)
        #
        # ### Filter file name list for files ending with .csv
        # fileNames = [file for file in fileNames if 'best_Lineup.csv' in file]
        #
        # ### Loop over all files
        # for file in fileNames:
        #     #master_csv = deftestdata['master_csv']
        #     title = deftestdata['title']
        #     x = deftestdata['x']
        #     y = deftestdata['y']
        #     df = pd.read_csv(file)
        #     N = 100000
        #     fig = go.Figure(data=go.Scattergl(
        #         x=df[x],
        #         y=df[y],
        #         mode='markers',
        #         marker_color=df[y],
        #         marker=dict(
        #             color=np.random.randn(N),
        #             colorscale='jet',
        #             line_width=0.1
        #         )
        #     ))
        #     fig.update_layout(
        #         xaxis=dict(
        #             tickmode='linear',
        #             title=title,
        #             dtick=0.1
        #         )
        #     )
        #     plt.plot(df)
        # fig.show()

    @pytest.mark.graph_all_data
    def test_create_graph_all_data(self, print_logging):
        """
        This test will dgraph each postion all_dta_csvs
        :param rawDataframe:
        :param print_logging:
        :param full_dataframe_prep:
        :return:
        """
        # Scatter Plot for QB
        #
        df = pd.read_csv('fullQB.csv')
        N = 100000
        fig = go.Figure(data=go.Scattergl(
            x=df['sdPts'],
            y=df['Actual_Points'],
            mode='markers',
            marker_color=df['Actual_Points'],
            marker=dict(
                color=np.random.randn(N),
                colorscale='jet',
                line_width=0.1
            )
        ))
        fig.update_layout(
            xaxis=dict(
                tickmode='linear',
                title='QB Chart',
                dtick=0.1
            )
        )
        fig.show()

        # Scatter Plot for RB
        #
        df = pd.read_csv('fullRB.csv')
        N = 100000
        fig = go.Figure(data=go.Scattergl(
            x=df['sdPts'],
            y=df['Actual_Points'],
            mode='markers',
            marker_color=df['Actual_Points'],
            marker=dict(
                color=np.random.randn(N),
                colorscale='jet',
                line_width=0.1
            )
        ))
        fig.update_layout(
            xaxis=dict(
                tickmode='linear',
                title='RB Chart',
                dtick=0.1
            )
        )
        fig.show()

        # Scatter Plot for WR
        #
        df = pd.read_csv('fullWR.csv')
        N = 100000
        fig = go.Figure(data=go.Scattergl(
            x=df['sdPts'],
            y=df['Actual_Points'],
            mode='markers',
            marker_color=df['Actual_Points'],
            marker=dict(
                color=np.random.randn(N),
                colorscale='jet',
                line_width=0.1
            )
        ))
        fig.update_layout(
            xaxis=dict(
                tickmode='linear',
                title='WR Chart',
                dtick=0.1
            )
        )
        fig.show()

        # Scatter Plot for TE
        #
        df = pd.read_csv('fullTE.csv')
        N = 100000
        fig = go.Figure(data=go.Scattergl(
            x=df['sdPts'],
            y=df['Actual_Points'],
            mode='markers',
            marker_color=df['Actual_Points'],
            marker=dict(
                color=np.random.randn(N),
                colorscale='jet',
                line_width=0.1
            )
        ))
        fig.update_layout(
            xaxis=dict(
                tickmode='linear',
                title='TE Chart',
                dtick=0.1
            )
        )
        fig.show()

        # Scatter Plot for DST
        #
        df = pd.read_csv('fullDST.csv')
        N = 100000
        fig = go.Figure(data=go.Scattergl(
            x=df['sdPts'],
            y=df['Actual_Points'],
            mode='markers',
            marker_color=df['Actual_Points'],
            marker=dict(
                color=np.random.randn(N),
                colorscale='jet',
                line_width=0.1
            )
        ))
        fig.update_layout(
            xaxis=dict(
                tickmode='linear',
                title='DST Chart',
                dtick=0.1
            )
        )
        fig.show()

        # Scatter Plot for FLX
        #
        df = pd.read_csv('fullFLX.csv')
        N = 100000
        fig = go.Figure(data=go.Scattergl(
            x=df['sdPts'],
            y=df['Actual_Points'],
            mode='markers',
            marker_color=df['Actual_Points'],
            marker=dict(
                color=np.random.randn(N),
                colorscale='jet',
                line_width=0.1
            )
        ))
        fig.update_layout(
            xaxis=dict(
                tickmode='linear',
                title='FLX Chart',
                dtick=0.1
            )
        )
        fig.show()