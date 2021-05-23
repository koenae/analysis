import matplotlib.pyplot as plt
import pandas as pd


def count_cookie_purposes(country):
    df = pd.read_json('./cookiepedia_purposes/output_{}.json'.format(country))
    target_and_ad = df.target_and_ad.values.sum()
    necessary = df.necessary.values.sum()
    unknown = df.unknown.values.sum()

    return [target_and_ad, necessary, unknown]


belgium = count_cookie_purposes('belgium')
france = count_cookie_purposes('france')
netherlands = count_cookie_purposes('the_netherlands')
austria = count_cookie_purposes('austria')
bulgaria = count_cookie_purposes('bulgaria')
croatia = count_cookie_purposes('croatia')
denmark = count_cookie_purposes('denmark')

data = [belgium, france, netherlands, austria, bulgaria, croatia, denmark]

df3 = pd.DataFrame(data, columns=['target_and_ad', 'necessary', 'unknown'])
df3.columns = ['Target/Ad', 'Necessary', 'Unknown']
df3.index = ['Belgium', 'France', 'Netherlands', 'Austria', 'Bulgaria', 'Croatia', 'Denmark']
ax = df3.plot.barh(stacked=True)
ax.figure.set_size_inches(10, 6)
plt.xlabel('Number of cookies')
plt.savefig("./plots/general/cookie_purposes")
plt.clf()
