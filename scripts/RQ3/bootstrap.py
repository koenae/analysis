import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mlxtend.evaluate import bootstrap

from scripts.utils import get_amount_of_cookies

outDir = "./plots/"


def bootstrap_sampling_amount_of_cookies_means(country):
    print("------------- {} --------------".format(country))
    aoc = get_amount_of_cookies(country)

    original_mean = np.mean(aoc.values)
    print("original mean: ", original_mean)

    original_standard_deviation = np.std(aoc.values)
    print("standard deviation: ", original_standard_deviation)

    sample_means = []
    n = len(aoc)
    resampling_means(sample_means, aoc.values, n)

    std_dev_of_sample_means = np.std(sample_means)
    print("std_dev_of_sample_means: ", std_dev_of_sample_means)

    standard_error = original_standard_deviation / np.sqrt(n)
    print("standard_error: ", standard_error)

    mean_of_sample_means = np.mean(sample_means)

    lb = lower_bound(mean_of_sample_means, standard_error)
    ub = upper_bound(mean_of_sample_means, standard_error)

    plot_distribution(country, original_mean, sample_means, lb, ub)


def plot_distribution(country, mean_of_sample_means, sample_means, lb, ub):
    fig_dims = (10, 6)
    fig, ax = plt.subplots(figsize=fig_dims)
    sns.kdeplot(sample_means, shade=True, ax=ax)
    plt.xticks([7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12])
    plt.xlim(7, 12)
    plt.axvline(x=mean_of_sample_means, linestyle='--', linewidth=2.5,
                label="sample mean of number of cookies", c='black')
    plt.axvline(x=lb, linestyle='--', linewidth=2.5, label="lower bound 95% CI", c='g')
    plt.axvline(x=ub, linestyle='--', linewidth=2.5, label="upper bound 95% CI", c='purple')
    plt.xlabel("sample mean number of cookies", labelpad=14)
    plt.ylabel("frequency of occurence", labelpad=14)
    plt.legend()
    plt.savefig(outDir + "/{}/bootstrap_sampling_amount_of_cookies_means".format(country))
    plt.clf()


def resampling_means(sample_means, values, size):
    for sample in range(0, 1000):
        sample_values = np.random.choice(a=values, size=size)
        sample_mean = np.mean(sample_values)
        sample_means.append(sample_mean)


def lower_bound(mean_of_sample_means, standard_error):
    lb = mean_of_sample_means - 1.96 * standard_error
    print("lower bound: ", lb)
    return lb


def upper_bound(mean_of_sample_means, standard_error):
    ub = mean_of_sample_means + 1.96 * standard_error
    print("lower bound: ", ub)
    return ub


def bootstrap_alternative(aoc):
    original, std_err, ci_bounds = bootstrap(aoc.values, num_rounds=1000, func=np.mean, ci=0.95)
    print('Mean: %.2f, SE: +/- %.2f, CI95: [%.2f, %.2f]' % (original,
                                                            std_err,
                                                            ci_bounds[0],
                                                            ci_bounds[1]))
