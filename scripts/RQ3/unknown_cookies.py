import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import json
import numpy as np


def top_10_unknown_cookies(country):
    df = pd.read_json('./cookiepedia_purposes/output_{}.json'.format(country))
    unknown_cookies = []
    for cookie_list in df.cookies.values:
        for cookie in cookie_list:
            if cookie['purpose'] == 'Unknown':
                unknown_cookies.append(cookie['name'])
    print('-------------- {} --------------'.format(country))
    print('Unknown cookies length: ', len(unknown_cookies))
    grouped_unknown_cookies = sorted(Counter(unknown_cookies).items(), key=lambda item: item[1], reverse=True)

    with open('./cookiepedia_purposes/unknown_{}.json'.format(country), 'w') as fp:
        json.dump(grouped_unknown_cookies, fp)

    df2 = pd.DataFrame(grouped_unknown_cookies[:10], columns=['cookie_name', 'cookie_count'])
    df2.sort_values('cookie_count', inplace=True)
    y_pos = np.arange(len(df2.cookie_name))
    x_pos = np.arange(max(df2.cookie_count), step=5)
    plt.barh(y_pos, df2.cookie_count, align='center')
    plt.yticks(y_pos, df2.cookie_name)
    plt.xticks(x_pos)
    plt.xlabel('Count')
    plt.tight_layout()
    plt.savefig('./plots/{}/unknown_cookies'.format(country))


top_10_unknown_cookies("belgium")
