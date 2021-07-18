import plotly.graph_objects as go
import sqlite3
import pandas as pd

outDir = "./plots/"


def color_table(country):
    if country == "denmark":
        return

    db = "./db/{}/crawl-data-dark-patterns_with_context.sqlite".format(country)
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
    context = []
    width_difference = []
    height_difference = []
    id = []

    for index, item in df_reject.iterrows():
        if item.allow_exists == 1 and (
                item.allow_rgb != 'rgba(0, 0, 0, 0)' and item.allow_rgb != 'rgb(0, 0, 0)' and item.allow_rgb != 'rgb(255, 255, 255)' and item.reject_rgb != 'rgba(0, 0, 0, 0)' and item.reject_rgb != 'rgb(0, 0, 0)' and item.reject_rgb != 'rgb(255, 255, 255)' and item.allow_rgb != item.reject_rgb):
            id.append(item.visit_id)
            consent.append(item.allow_rgb)
            reject.append(item.reject_rgb)
            context.append(item.context_rgb)
            width_difference.append(int(item.allow_width) - int(item.reject_width))
            height_difference.append(int(item.allow_height) - int(item.reject_height))

    fig = go.Figure(data=[go.Table(
        columnwidth=[5, 5, 5, 5, 10, 10],
        header=dict(
            values=['<b>ID</b>', '<b>Background</b>', '<b>Consent</b>', '<b>Reject</b>', '<b>Consent - reject (width)</b>',
                    '<b>Consent - reject (height)</b>'],
            line_color='white', fill_color='white',
            align='center', font=dict(color='black', size=12)
        ),
        cells=dict(
            values=[id, '', '', '', width_difference, height_difference],
            line_color=['rgb(255,255,255)', 'rgb(255,255,255)', 'rgb(255,255,255)', 'rgb(255,255,255)', 'rgb(255,255,255)', 'rgb(255,255,255)'],
            fill_color=['rgb(255,255,255)', context, consent, reject, 'rgb(255,255,255)', 'rgb(255,255,255)'],
            align='right', font=dict(color='black', size=11)
        ))
    ])
    fig.update_layout(title_text=country)

    fig.show()
