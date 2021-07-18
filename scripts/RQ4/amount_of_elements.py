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

    print(country_view_name + ": consent {} - reject {}".format(int(consent.total), int(reject.total)))

    return [int(consent.total), int(reject.total), country_view_name]


austria = count_elements('austria', 'Austria')
belgium = count_elements('belgium', 'Belgium')
bulgaria = count_elements('bulgaria', 'Bulgaria')
croatia = count_elements('croatia', 'Croatia')
cyprus = count_elements('cyprus', 'Cyprus')
czech_republic = count_elements('czech_republic', 'Czech Republic')
estonia = count_elements('estonia', 'Estonia')
finland = count_elements('finland', 'Finland')
france = count_elements('france', 'France')
germany = count_elements('germany', 'Germany')
greece = count_elements('greece', 'Greece')
hungary = count_elements('hungary', 'Hungary')
ireland = count_elements('ireland', 'Ireland')
italy = count_elements('italy', 'Italy')
latvia = count_elements('latvia', 'Latvia')
lithuania = count_elements('lithuania', 'Lithuania')
luxembourg = count_elements('luxembourg', 'Luxembourg')
malta = count_elements('malta', 'Malta')
norway = count_elements('norway', 'Norway')
poland = count_elements('poland', 'Poland')
portugal = count_elements('portugal', 'Portugal')
romania = count_elements('romania', 'Romania')
slovakia = count_elements('slovakia', 'Slovakia')
slovenia = count_elements('slovenia', 'Slovenia')
spain = count_elements('spain', 'Spain')
sweden = count_elements('sweden', 'Sweden')
switzerland = count_elements('switzerland', 'Switzerland')
netherlands = count_elements('the_netherlands', 'Netherlands')
united_kingdom = count_elements('united_kingdom', 'United Kingdom')

data = [austria, belgium, bulgaria, croatia, cyprus, czech_republic, estonia, finland,
        france, germany, greece, hungary, ireland, italy, latvia, lithuania, luxembourg, malta, norway, poland,
        portugal, romania, slovakia, slovenia, spain, sweden, switzerland, netherlands, united_kingdom]

sorted_data = sorted(data, key=lambda row: sum([row[0], row[1]]))

# Extract the country names
index = []
total = 0
consentTotal = 0
rejectTotal = 0
for element in sorted_data:
    total += (element[0] + element[1])
    consentTotal += element[0]
    rejectTotal += element[1]
    index.append(element[2])

print('mean: ', total / 29)
print('consent mean: ', consentTotal / 29)
print('reject mean: ', rejectTotal / 29)

# Delete the country names as we do not want to pass it as a column
view_data = np.delete(np.array(sorted_data, dtype='object'), 2, 1)

df3 = pd.DataFrame(view_data, columns=['consent', 'reject'])
df3.columns = ['Consent', 'Reject']

df3.index = index

ax = df3.plot.barh(stacked=False, color=['green', 'red'])
ax.figure.set_size_inches(10, 6)
plt.xlabel('Number of HTML elements')
plt.savefig("./plots/general/amount_of_elements")
plt.clf()
