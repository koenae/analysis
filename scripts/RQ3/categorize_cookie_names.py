import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import json


def save_unknown_cookies(file_name, country):
    df = pd.read_json(file_name)
    unknown_cookies = []
    for cookie_list in df.cookies.values:
        for cookie in cookie_list:
            if cookie['purpose'] == 'Unknown':
                unknown_cookies.append(cookie['name'])
    print('-------------- {} --------------'.format(country))
    print(len(unknown_cookies))
    grouped_unknown_cookies = sorted(Counter(unknown_cookies).items(), key=lambda item: item[1], reverse=True)
    print(grouped_unknown_cookies)
    with open('./cookiepedia_purposes/unknown_{}.json'.format(country), 'w') as fp:
        json.dump(grouped_unknown_cookies, fp)


# save_unknown_cookies("./cookiepedia_purposes/the_netherlands.json", "the_netherlands")


def count_cookie_purposes(file_name):
    df = pd.read_json(file_name)
    target_and_ad = df.target_and_ad.values.sum()
    necessary = df.necessary.values.sum()
    unknown = df.unknown.values.sum()

    return [target_and_ad, necessary, unknown]


belgium = count_cookie_purposes("./cookiepedia_purposes/output_be.json")
france = count_cookie_purposes("./cookiepedia_purposes/output_fr.json")
netherlands = count_cookie_purposes("./cookiepedia_purposes/the_netherlands.json")

data = [belgium, france, netherlands]

df3 = pd.DataFrame(data, columns=['target_and_ad', 'necessary', 'unknown'])
df3.columns = ['Target/Ad', 'Necessary', 'Unknown']
df3.index = ['Belgium', 'France', 'Netherlands']
ax = df3.plot.barh(stacked=True)
ax.figure.set_size_inches(10, 6)
plt.xlabel('Number of cookies')
plt.savefig("./plots/general/cookie_purposes")
plt.clf()
