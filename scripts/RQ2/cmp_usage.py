import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def cmp_usage(country):
    db = "./db/{}/crawl-data.sqlite".format(country)
    conn = sqlite3.connect(db)

    df_init = pd.read_sql_query(
        "select cmp_name, count(cmp_id) as count_cmp from ping_cmp group by cmp_id order by count(cmp_id)", conn
    )

    df = df_init[(df_init['count_cmp'] != 0)]

    y_pos = np.arange(len(df.cmp_name))
    x_pos = np.arange(max(df.count_cmp), step=5)
    plt.barh(y_pos, df.count_cmp, align="center")
    plt.yticks(y_pos, df.cmp_name)
    plt.xticks(x_pos)
    plt.xlabel("Count")
    plt.tight_layout()

    print("{}: {}".format(country, df.cmp_name.values[-1]))

    plt.savefig("./plots/{}/cmp_usage".format(country))
    plt.clf()
    conn.close()
    return sum(df.count_cmp.values)
