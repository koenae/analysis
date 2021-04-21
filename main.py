from scripts.RQ1.cmp_usage import cmp_usage
from scripts.RQ3.bootstrap import bootstrap_sampling_amount_of_cookies_means
from scripts.RQ3.number_of_cookies_ecdf import number_of_cookies_ecdf


def run():
    countries = ['france']
    for country in countries:
        cmp_usage(country)
        number_of_cookies_ecdf(country)
        bootstrap_sampling_amount_of_cookies_means(country)


run()
