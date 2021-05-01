import matplotlib.pyplot as plt
from mlxtend.plotting import ecdf

from scripts.utils import get_amount_of_cookies

outDir = "./plots/"


def number_of_cookies_ecdf(country):
    plt.figure(figsize=(9, 5))
    plt.xticks([0, 20, 40, 60, 80, 100, 120, 140, 160])
    plt.xlim(0, 160)
    _, threshold, count = ecdf(x=get_amount_of_cookies(country), x_label='number of cookies', percentile=0.8)

    print("Threshold for {}: {}".format(country, threshold))
    print("Count for {}: {}".format(country, count))

    plt.savefig(outDir + "/{}/ecdf".format(country))
    plt.clf()
