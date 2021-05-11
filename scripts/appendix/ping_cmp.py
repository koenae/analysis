import sqlite3

import pandas as pd
from IPython.display import display


def load_data(country):
    db = "./db/{}/crawl-data.top500.sqlite".format(country)
    conn = sqlite3.connect(db)

    df = pd.read_sql_query(
        "select cmp_name, count(cmp_id) as count_cmp from ping_cmp group by cmp_id order by count(cmp_id)", conn
    )

    display(df)

    # with open('./plots/{}/appendix_ping_cmp.png'.format(country), 'w') as fp:
    #    json.dump(df.render(), fp)


load_data('the_netherlands')
