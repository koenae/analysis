import sqlite3

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re

outDir = "./plots/"


def color_map(country, reject=False):
    if country == "denmark":
        return

    db = "./db/{}/crawl-data-dark-patterns.sqlite".format(country)
    conn = sqlite3.connect(db)

    if not reject:
        query = "select * from dark_patterns where allow_height < 100 and allow_height != 0 and allow_text != '' and " \
                "length(allow_text) < 30 "
    else:
        query = "select * from dark_patterns where reject_text != '' and length(reject_text) < 30 and reject_text != " \
                "'OK' "

    df = pd.read_sql_query(
        query,
        conn
    )

    r_values = []
    g_values = []
    b_values = []

    if not reject:
        rgb_values = df.allow_rgb
    else:
        rgb_values = df.reject_rgb

    for i, rgb in enumerate(rgb_values):
        if rgb is None or rgb == "rgba(0, 0, 0, 0)":
            r_values.append(0)
            g_values.append(0)
            b_values.append(0)
            continue
        search_rgb = re.search(r'rgb\((\d+),\s*(\d+),\s*(\d+)', rgb)
        if search_rgb is not None:
            r, g, b = map(int, search_rgb.groups())
        else:
            search_rgba = re.search(r'rgba\((\d+),\s*(\d+),\s*(\d+),\s*(\d+)', rgb)
            r, g, b, a = map(int, search_rgba.groups())
        r_values.append(r)
        g_values.append(g)
        b_values.append(b)

    colors = ["#FF0000", "#00FF00", "#0000FF"]
    rgb_palette = sns.set_palette(sns.color_palette(colors))

    if len(r_values) == 0 and len(g_values) == 0 and len(b_values) == 0:
        return

    sns.histplot(data={"Red": r_values, "Green": g_values, "Blue": b_values}, palette=rgb_palette, fill=False,
                 multiple="stack")
    plt.ylim(0, 150 if not reject else 70)
    plt.savefig(outDir + "/{}/{}_colormap".format(country, "allow" if not reject else "reject"))
    plt.clf()


color_map("poland", True)
