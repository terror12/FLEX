# from altair import *
# from math import *
import pandas as pd
# import os
import altair as alt


file = "/home/ascerra/FLEX_dev/scenario/flex/wk_1_revised_QB.csv"
data = pd.read_csv(file)

data.head()

chart = alt.Chart(data).mark_bar().encode(x=X('Actual_Points', bin=Bin(maxbins=20)), y='sdPts', )  # noqa F821
