import plotly.graph_objects as go
from plotly.colors import n_colors
import numpy as nps
import sqlite3
import pandas as pd

db = "./db/{}/crawl-data-dark-patterns.sqlite".format("the_netherlands")
conn = sqlite3.connect(db)

query_consent = "select * from dark_patterns where allow_height < 100 and allow_height != 0 and allow_text != '' and " \
                "length(allow_text) < 30 "

query_reject = "select * from dark_patterns where reject_text != '' and length(reject_text) < 30 and reject_text != " \
               "'OK' "

df_consent = pd.read_sql_query(
    query_consent,
    conn
)

df_reject = pd.read_sql_query(
    query_reject,
    conn
)

consent = []
reject = []
id = []

for index, item in df_reject.iterrows():
    if item.allow_exists == 1 and (item.allow_rgb != 'rgba(0, 0, 0, 0)' and item.allow_rgb != 'rgb(0, 0, 0)' and item.allow_rgb != 'rgb(255, 255, 255)' and item.reject_rgb != 'rgba(0, 0, 0, 0)' and item.reject_rgb != 'rgb(0, 0, 0)' and item.reject_rgb != 'rgb(255, 255, 255)'):
        print("allowRGB: {} - rejectRGB: {}".format(item.allow_rgb, item.reject_rgb))
        id.append(item.visit_id)
        consent.append(item.allow_rgb)
        reject.append(item.reject_rgb)

fig = go.Figure(data=[go.Table(
    header=dict(
        values=['<b>ID</b>', '<b>Consent</b>', '<b>Reject</b>'],
        line_color='white', fill_color='white',
        align='center', font=dict(color='black', size=12)
    ),
    cells=dict(
        values=[id, consent, reject],
        line_color=['rgb(255,255,255)', consent, reject],
        fill_color=['rgb(0,0,0)', consent, reject],
        align='center', font=dict(color='black', size=11)
    ))
])

fig.show()
