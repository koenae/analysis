import matplotlib.pyplot as plt
from mlxtend.plotting import ecdf

from scripts.utils import get_amount_of_cookies

outDir = "./plots/"


def number_of_cookies_ecdf(country):
    plt.figure(figsize=(9, 5))
    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])
    plt.xlim(0, 150)
    total = get_amount_of_cookies(country)
    filter_total = [i for i in total if i >= 2]
    print(len(filter_total))
    _, threshold, count = ecdf(x=total, x_label='number of cookies', percentile=0.13)

    print("Threshold for {}: {}".format(country, threshold))
    print("Count for {}: {}".format(country, count))

    plt.savefig(outDir + "/{}/ecdf_new".format(country))
    plt.clf()
