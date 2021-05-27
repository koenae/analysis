import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def count_cookie_purposes(country, country_view_name):
    df = pd.read_json('./cookiepedia_purposes/output_{}.json'.format(country))
    target_and_ad = df.target_and_ad.values.sum()
    performance = 0
    if 'performance' in df.columns.values:
        performance = df.performance.values.sum()
    necessary = df.necessary.values.sum()
    functionality = 0
    if 'functionality' in df.columns.values:
        functionality = df.functionality.values.sum()
    unknown = df.unknown.values.sum()

    return [target_and_ad, performance, necessary, functionality, unknown, country_view_name]


austria = count_cookie_purposes('austria', 'Austria')
bulgaria = count_cookie_purposes('bulgaria', 'Bulgaria')
croatia = count_cookie_purposes('croatia', 'Croatia')
cyprus = count_cookie_purposes('cyprus', 'Cyprus')
czech_republic = count_cookie_purposes('czech_republic', 'Czech Republic')
denmark = count_cookie_purposes('denmark', 'Denmark')
estonia = count_cookie_purposes('estonia', 'Estonia')
finland = count_cookie_purposes('finland', 'Finland')
france = count_cookie_purposes('france', 'France')
germany = count_cookie_purposes('germany', 'Germany')
greece = count_cookie_purposes('greece', 'Greece')
hungary = count_cookie_purposes('hungary', 'Hungary')
ireland = count_cookie_purposes('ireland', 'Ireland')
italy = count_cookie_purposes('italy', 'Italy')
latvia = count_cookie_purposes('latvia', 'Latvia')
lithuania = count_cookie_purposes('lithuania', 'Lithuania')
luxembourg = count_cookie_purposes('luxembourg', 'Luxembourg')
malta = count_cookie_purposes('malta', 'Malta')
norway = count_cookie_purposes('norway', 'Norway')
poland = count_cookie_purposes('poland', 'Poland')
portugal = count_cookie_purposes('portugal', 'Portugal')
romania = count_cookie_purposes('romania', 'Romania')
slovakia = count_cookie_purposes('slovakia', 'Slovakia')
slovenia = count_cookie_purposes('slovenia', 'Slovenia')
spain = count_cookie_purposes('spain', 'Spain')
sweden = count_cookie_purposes('sweden', 'Sweden')
switzerland = count_cookie_purposes('switzerland', 'Switzeland')
netherlands = count_cookie_purposes('the_netherlands', 'Netherlands')
united_kingdom = count_cookie_purposes('united_kingdom', 'United Kingdom')

data = [austria, bulgaria, croatia, cyprus, czech_republic, denmark, estonia, finland,
        france, germany, greece, hungary, ireland, italy, latvia, lithuania, luxembourg, malta, norway, poland,
        portugal, romania, slovakia, slovenia, spain, sweden, switzerland, netherlands, united_kingdom]

sorted_data = sorted(data, key=lambda row: sum([row[0], row[1], row[2], row[3], row[4]]))

# Extract the country names
index = []
for element in sorted_data:
    index.append(element[5])

# Delete the country names as we do not want to pass it as a column
view_data = np.delete(np.array(sorted_data, dtype='object'), 5, 1)

df3 = pd.DataFrame(view_data, columns=['target_and_ad', 'performance', 'necessary', 'functionality', 'unknown'])
df3.columns = ['Target/Ad', 'Performance', 'Necessary', 'Functionality', 'Unknown']

df3.index = index

ax = df3.plot.barh(stacked=True, color=['red', 'orange', 'green', 'blue', 'grey'])
ax.figure.set_size_inches(10, 6)
plt.xlabel('Number of cookies')
plt.savefig("./plots/general/cookie_purposes")
plt.clf()
