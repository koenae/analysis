import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.plotting import stacked_barplot


def count_cookie_purposes(file_name):
    df = pd.read_json(file_name)
    target_and_ad = df.target_and_ad.values.sum()
    necessary = df.necessary.values.sum()
    unknown = df.unknown.values.sum()

    return [target_and_ad, necessary, unknown]


belgium = count_cookie_purposes("./cookiepedia_purposes/output_be.json")
france = count_cookie_purposes("./cookiepedia_purposes/output_fr.json")

data = [belgium, france]

df3 = pd.DataFrame(data, columns=['target_and_ad', 'necessary', 'unknown'])
df3.columns = ['Target/Ad', 'Necessary', 'Unknown']
df3.index = ['Belgium', 'France']

fig = stacked_barplot(df3, rotation=45, legend_loc='best')
plt.ylabel('Number of cookies')
plt.savefig("./plots/general/cookie_purposes")
plt.clf()
