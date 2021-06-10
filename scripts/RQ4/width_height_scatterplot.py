import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

db = "./db/{}/crawl-data-dark-patterns.sqlite".format("the_netherlands")
conn = sqlite3.connect(db)

query_consent = "select * from dark_patterns where allow_height < 100 and allow_height != 0 and allow_text != '' and " \
                "length(allow_text) < 30 "

query_reject = "select * from dark_patterns where reject_text != '' and length(reject_text) < 30 and reject_text != " \
               "'OK' "

df_consent = pd.read_sql_query(
    query_consent,
    conn
)

df_reject = pd.read_sql_query(
    query_reject,
    conn
)

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(df_consent.allow_width, df_consent.allow_height, s=10, c='b', marker="s", label='Consent')
ax1.scatter(df_reject.reject_width, df_reject.reject_height, s=10, c='r', marker="o", label='Reject')
plt.legend(loc='upper right')
plt.show()
