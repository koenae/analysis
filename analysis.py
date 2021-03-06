import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outDir = "/Users/koen/Documents/Research/"

# Belgium
openwpm_db_top500_be = "/Users/koen/Documents/Research/crawl-data.top500-be.sqlite"
conn = sqlite3.connect(openwpm_db_top500_be)

# Belgium top 500 - cookies set
df1 = pd.read_sql_query(
    "select s.visit_id as url, count(distinct j.name) as amount_of_cookies from site_visits s join javascript_cookies "
    "j on s.visit_id = j.visit_id "
    " where j.record_type == 'added-or-changed'"
    " group by s.site_url"
    " order by count(distinct j.name) desc ", conn)

_, ax = plt.subplots()
ax.scatter(df1.url, df1.amount_of_cookies)
ax.set_xlabel('Visit id from crawl')
ax.set_ylabel("Number of cookies")
ax.set_title("Belgium top 500 - cookies set")

plt.savefig(outDir + "belgium_top_500_cookies")
plt.clf()

# Belgium top 500 - CMP usage
df2 = pd.read_sql_query(
    "select cmp_name, count(cmp_id) as count_cmp from ping_cmp group by cmp_id order by count(cmp_id)", conn
)

y_pos = np.arange(len(df2.cmp_name))
x_pos = np.arange(max(df2.count_cmp), step=5)
plt.barh(y_pos, df2.count_cmp, align="center")
plt.yticks(y_pos, df2.cmp_name)
plt.xticks(x_pos)
plt.xlabel("Count")
plt.title("Belgium top 500 - CMP usage")
plt.tight_layout()

plt.savefig(outDir + "belgium_top_500_cmp")
plt.clf()
conn.close()

# Netherlands top 500 - cookies set
openwpm_db_top500_nl = "/Users/koen/Documents/Research/crawl-data.top500-nl.sqlite"
conn = sqlite3.connect(openwpm_db_top500_nl)

df1 = pd.read_sql_query(
    "select s.visit_id as url, count(distinct j.name) as amount_of_cookies from site_visits s join javascript_cookies "
    "j on s.visit_id = j.visit_id "
    " where j.record_type == 'added-or-changed'"
    " group by s.site_url"
    " order by count(distinct j.name) desc ", conn)

fig, ax = plt.subplots()
ax.scatter(df1.url, df1.amount_of_cookies)
ax.set_xlabel('Visit id from crawl')
ax.set_ylabel("Number of cookies")
ax.set_title("Netherlands top 500 - cookies set")

plt.savefig(outDir + "netherlands_top_500_cookies")
plt.clf()

# Netherlands top 500 - CMP usage
df2 = pd.read_sql_query(
    "select cmp_name, count(cmp_id) as count_cmp from ping_cmp group by cmp_id order by count(cmp_id)", conn
)

y_pos = np.arange(len(df2.cmp_name))
x_pos = np.arange(max(df2.count_cmp), step=5)
plt.barh(y_pos, df2.count_cmp, align="center")
plt.yticks(y_pos, df2.cmp_name)
plt.xticks(x_pos)
plt.xlabel("Count")
plt.title("Netherlands top 500 - CMP usage")
plt.tight_layout()

plt.savefig(outDir + "netherlands_top_500_cmp")
plt.clf()
conn.close()
