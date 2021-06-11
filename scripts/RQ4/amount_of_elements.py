import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import numpy as np


def count_elements(country, country_view_name):
    db = "./db/{}/crawl-data-dark-patterns.sqlite".format(country)
    conn = sqlite3.connect(db)

    query_consent = "select count(*) as total from dark_patterns where allow_height < 100 and allow_height != 0 and " \
                    "allow_text != " \
                    "'' and " \
                    "length(allow_text) < 30 "

    query_reject = "select count(*) as total from dark_patterns where reject_text != '' and length(reject_text) < 30 " \
                   "and " \
                   "reject_text != " \
                   "'OK' "

    consent = pd.read_sql_query(
        query_consent,
        conn
    )

    reject = pd.read_sql_query(
        query_reject,
        conn
    )

    return [int(consent.total), int(reject.total), country_view_name]


belgium = count_elements("belgium", "Belgium")
the_netherlands = count_elements("the_netherlands", "The Netherlands")
france = count_elements("france", "France")
germany = count_elements("germany", "Germany")
united_kingdom = count_elements("united_kingdom", "United Kingdom")

data = [belgium, the_netherlands, france, germany, united_kingdom]

sorted_data = sorted(data, key=lambda row: sum([row[0], row[1]]))

# Extract the country names
index = []
for element in sorted_data:
    index.append(element[2])

# Delete the country names as we do not want to pass it as a column
view_data = np.delete(np.array(sorted_data, dtype='object'), 2, 1)

df3 = pd.DataFrame(view_data, columns=['consent', 'reject'])
df3.columns = ['Consent', 'Reject']

df3.index = index

ax = df3.plot.barh(stacked=True, color=['green', 'red'])
ax.figure.set_size_inches(10, 6)
plt.xlabel('Number of elements')
plt.show()
# plt.savefig("./plots/general/cookie_purposes")
# plt.clf()
