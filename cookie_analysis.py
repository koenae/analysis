import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outDir = "/Users/koen/Documents/Research/"

# Belgium
openwpm_db_top500_be = "/Users/koen/Documents/Research/crawl-data.top500-be.sqlite"
conn = sqlite3.connect(openwpm_db_top500_be)

visits = pd.read_sql_query("select visit_id, site_url from site_visits", conn)

result = []
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
    result.append([row.site_url, df1.shape[0]])
print(result)
df = pd.DataFrame(result, columns=['url', 'amount_of_cookies'])

outDir = "/Users/koen/Documents/Research/"
_, ax = plt.subplots()
ax.scatter(df.url, df.amount_of_cookies)
ax.set_xlabel('Visit id from crawl')
ax.set_ylabel("Number of cookies")
ax.set_title("Belgium top 500 - cookies set")

plt.savefig(outDir + "belgium_top_500_cookies_2")
plt.clf()

