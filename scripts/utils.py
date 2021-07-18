import sqlite3

import pandas as pd
import json


def get_amount_of_cookies(country):
    crawl_data = "./db/{}/crawl-data.sqlite".format(country)
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
        df1.drop_duplicates(subset='name', keep='last', inplace=True)
        cookie_names.update({row.site_url: list(df1.name.values)})
        result.append([row.visit_id, df1.shape[0]])

    df = pd.DataFrame(result, columns=['url', 'amount_of_cookies'])
    df.url = df.url.astype(str)
    df.sort_values(by=['amount_of_cookies'], inplace=True)

    with open('./cookie_names/{}_new.json'.format(country), 'w') as fp:
        json.dump(cookie_names, fp)

    return df.amount_of_cookies
