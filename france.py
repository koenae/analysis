import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

outDir = "/Users/koen/Documents/Research/"

# France
# fr = "/Users/koen/Documents/Research/france/crawl-data.top500-fr-ping-cmp.sqlite"
# conn = sqlite3.connect(fr)
#
# # France top 500 - CMP usage
# df2 = pd.read_sql_query(
#     "select cmp_name, count(cmp_id) as count_cmp from ping_cmp group by cmp_id order by count(cmp_id)", conn
# )
#
# y_pos = np.arange(len(df2.cmp_name))
# x_pos = np.arange(max(df2.count_cmp), step=5)
# plt.barh(y_pos, df2.count_cmp, align="center")
# plt.yticks(y_pos, df2.cmp_name)
# plt.xticks(x_pos)
# plt.xlabel("Count")
# plt.title("France top 500 - CMP usage")
# plt.tight_layout()
#
# plt.savefig(outDir + "france_top_500_cmp")
# plt.clf()
# conn.close()

# France
fr = "/Users/koen/Documents/Research/france/crawl-data.top500-fr-dialog.sqlite"
conn = sqlite3.connect(fr)

# France top 500 - cookie dialog detection
df1 = pd.read_sql_query(
    "select count(*) as count_frames from cookie_dialog as c join site_visits as s on c.visit_id = s.visit_id where "
    "c.element_type = "
    "'frame'", conn
)

df2 = pd.read_sql_query(
    "select count(*) as count_classes from cookie_dialog as c join site_visits as s on c.visit_id = s.visit_id where "
    "c.element_type = "
    "'class'", conn
)

df3 = pd.read_sql_query(
    "select count(*) as count_ids from cookie_dialog as c join site_visits as s on c.visit_id = s.visit_id where "
    "c.element_type = "
    "'id'", conn
)

df4 = pd.read_sql_query(
    "select count(*) as count_unknown from cookie_dialog as c join site_visits as s on c.visit_id = s.visit_id where "
    "c.element_type != "
    "'class' and c.element_type != 'id' and c.element_type != 'frame'", conn
)

labels = ['HTML frame', 'CSS class', 'CSS id', 'No dialog found']
sizes = [df1.count_frames[0], df2.count_classes[0], df3.count_ids[0], df4.count_unknown[0]]
colors = ['silver', 'grey', 'dimgrey', 'red']
print(sizes)
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
ax.set_title('France top 500 - cookie dialog detection')
plt.tight_layout()

plt.savefig(outDir + "france_top_500_dialog")
plt.clf()
conn.close()
