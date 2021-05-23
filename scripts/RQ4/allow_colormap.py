import sqlite3

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re


def allow_color_map(country):
    db = "./db/{}/crawl-data-dp.sqlite".format(country)
    conn = sqlite3.connect(db)

    df = pd.read_sql_query(
        "select * from dark_patterns where allow_height < 100 and allow_height != 0 and allow_text != '' and length("
        "allow_text) < 30",
        conn
    )

    r_values = []
    g_values = []
    b_values = []

    for i, rgb in enumerate(df.allow_rgb):
        if rgb is None or rgb == "rgba(0, 0, 0, 0)":
            r_values.append(0)
            g_values.append(0)
            b_values.append(0)
            continue
        r, g, b = map(int, re.search(
            r'rgb\((\d+),\s*(\d+),\s*(\d+)', rgb).groups())
        r_values.append(r)
        g_values.append(g)
        b_values.append(b)

    colors = ["#FF0000", "#00FF00", "#0000FF"]
    rgb_palette = sns.set_palette(sns.color_palette(colors))

    sns.histplot(data={"Red": r_values, "Green": g_values, "Blue": b_values}, palette=rgb_palette, fill=False, multiple="stack")
    plt.ylim(0, 30)
    plt.show()


allow_color_map("the_netherlands")
