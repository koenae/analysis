import sqlite3

import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.plotting import ecdf

outDir = "./plots/"


def plot_ecdf(country):
    crawl_data = "./db/{}/crawl-data.top500.sqlite".format(country)
    conn = sqlite3.connect(crawl_data)

    visits = pd.read_sql_query("select visit_id, site_url from site_visits", conn)

    result = []
    cookie_names = {}
    for _, row in visits.iterrows():
        df1 = pd.read_sql_query(
            "select name from javascript_cookies " +
            "where visit_id = {} and record_type = 'added-or-changed'".format(row.visit_id), conn)
        df2 = pd.read_sql_query(
            "select name from javascript_cookies " +
            "where visit_id = {} and record_type = 'deleted'".format(row.visit_id), conn)
        for n in df1.name.values:
            if n in df2.name.values:
                df2.drop([df2.index[(df2["name"] == n)][0]], inplace=True)
                df1.drop([df1.index[(df1["name"] == n)][0]], inplace=True)
        cookie_names.update({row.site_url: list(df1.name.values)})
        result.append([row.visit_id, df1.shape[0]])

    df = pd.DataFrame(result, columns=['url', 'amount_of_cookies'])
    df.url = df.url.astype(str)

    df.sort_values(by=['amount_of_cookies'], inplace=True)

    plt.figure(figsize=(9, 5))
    _, threshold, count = ecdf(x=df.amount_of_cookies, x_label='number of cookies', percentile=0.8)

    print("Threshold for {}: {}".format(country, threshold))
    print("Count for {}: {}".format(country, count))

    plt.savefig(outDir + "/{}/ecdf".format(country))
    plt.clf()


plot_ecdf("the_netherlands")
plot_ecdf("belgium")
plot_ecdf("france")
