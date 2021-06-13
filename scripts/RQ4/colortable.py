import plotly.graph_objects as go
import sqlite3
import pandas as pd

outDir = "./plots/"


def color_table(country):
    if country == "denmark":
        return

    db = "./db/{}/crawl-data-dark-patterns.sqlite".format(country)
    conn = sqlite3.connect(db)

    query_reject = "select * from dark_patterns where reject_text != '' and length(reject_text) < 30 and reject_text " \
                   "!= " \
                   "'OK' "

    df_reject = pd.read_sql_query(
        query_reject,
        conn
    )

    consent = []
    reject = []
    width_difference = []
    height_difference = []
    id = []

    for index, item in df_reject.iterrows():
        if item.allow_exists == 1 and (
                item.allow_rgb != 'rgba(0, 0, 0, 0)' and item.allow_rgb != 'rgb(0, 0, 0)' and item.allow_rgb != 'rgb(255, 255, 255)' and item.reject_rgb != 'rgba(0, 0, 0, 0)' and item.reject_rgb != 'rgb(0, 0, 0)' and item.reject_rgb != 'rgb(255, 255, 255)' and item.allow_rgb != item.reject_rgb):
            id.append(item.visit_id)
            consent.append(item.allow_rgb)
            reject.append(item.reject_rgb)
            width_difference.append(int(item.allow_width) - int(item.reject_width))
            height_difference.append(int(item.allow_height) - int(item.reject_height))

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['<b>ID</b>', '<b>Consent</b>', '<b>Reject</b>', '<b>Width difference</b>',
                    '<b>Height difference</b>'],
            line_color='white', fill_color='white',
            align='center', font=dict(color='black', size=12)
        ),
        cells=dict(
            values=[id, consent, reject, width_difference, height_difference],
            line_color=['rgb(255,255,255)', consent, reject, 'rgb(255,255,255)', 'rgb(255,255,255)'],
            fill_color=['rgb(255,255,255)', consent, reject, 'rgb(255,255,255)', 'rgb(255,255,255)'],
            align='center', font=dict(color='black', size=11)
        ))
    ])
    fig.update_layout(title_text=country)

    fig.show()
