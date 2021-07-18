import sqlite3

import matplotlib.pyplot as plt
import pandas as pd


def cookie_dialog(country, js_disabled=False, ublock=False):
    if js_disabled:
        db = "./db/{}/crawl-data-cookie-dialog-no-js.sqlite".format(country)
    elif ublock:
        db = "./db/{}/crawl-data-cookie-dialog-ublock.sqlite".format(country)
    else:
        db = "./db/{}/crawl-data-cookie-dialog.sqlite".format(country)
    conn = sqlite3.connect(db)

    df1 = pd.read_sql_query(
        "select count(*) as count_frames from cookie_dialog as c join site_visits as s on c.visit_id = s.visit_id "
        "where "
        "c.element_type = "
        "'frame'", conn
    )

    df2 = pd.read_sql_query(
        "select count(*) as count_classes from cookie_dialog as c join site_visits as s on c.visit_id = s.visit_id "
        "where "
        "c.element_type = "
        "'class'", conn
    )

    df3 = pd.read_sql_query(
        "select count(*) as count_ids from cookie_dialog as c join site_visits as s on c.visit_id = s.visit_id where "
        "c.element_type = "
        "'id'", conn
    )

    df4 = pd.read_sql_query(
        "select count(*) as count_unknown from cookie_dialog as c join site_visits as s on c.visit_id = s.visit_id "
        "where "
        "c.element_type != "
        "'class' and c.element_type != 'id' and c.element_type != 'frame'", conn
    )

    labels = ['HTML frame', 'CSS class', 'CSS id', 'No dialog found']
    sizes = [df1.count_frames[0], df2.count_classes[0], df3.count_ids[0], df4.count_unknown[0]]
    colors = ['silver', 'grey', 'dimgrey', 'red']
    print(sizes)
    plt.rcParams.update({'font.size': 12})
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.tight_layout()

    if js_disabled:
        plt.savefig("./plots/{}/new_cookie_dialog_no_js".format(country))
    elif ublock:
        plt.savefig("./plots/{}/new_cookie_dialog_ublock".format(country))
    else:
        plt.savefig("./plots/{}/new_cookie_dialog".format(country))
    plt.clf()
    conn.close()
    # return df1.count_frames[0] + df2.count_classes[0] + df3.count_ids[0] + df4.count_unknown[0]
    # return ((df1.count_frames[0] + df2.count_classes[0] + df3.count_ids[0]) / (df1.count_frames[0] + df2.count_classes[0] + df3.count_ids[0] + df4.count_unknown[0])) * 100
