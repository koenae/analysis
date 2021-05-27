from scripts.RQ1.cmp_usage import cmp_usage
from scripts.RQ2.cookie_dialog import cookie_dialog
from scripts.RQ3.bootstrap import bootstrap_sampling_amount_of_cookies_means
from scripts.RQ3.number_of_cookies_ecdf import number_of_cookies_ecdf

import os


def run():
    cmp_count_total = 0
    countries = ['the_netherlands',
                 'belgium',
                 'france',
                 'germany',
                 'luxembourg',
                 'united_kingdom',
                 'spain',
                 'portugal',
                 'italy',
                 'switzerland',
                 'ireland',
                 'denmark',
                 'norway',
                 'sweden',
                 'finland',
                 'bulgaria',
                 'cyprus',
                 'estonia',
                 'greece',
                 'hungary',
                 'croatia',
                 'latvia',
                 'lithuania',
                 'malta',
                 'austria',
                 'poland',
                 'romania',
                 'slovenia',
                 'slovakia',
                 'czech_republic']
    for country in countries:
        if not os.path.exists('./plots/{}'.format(country)):
            os.makedirs('./plots/{}'.format(country))

        # RQ1
        cmp_usage(country)
        # cmp_count = cmp_usage(country)
        # print("{}: {}".format(country, cmp_count))
        # cmp_count_total += cmp_count

        # RQ2
        # cookie_dialog(country)

        # RQ3
        # number_of_cookies_ecdf(country)
        # bootstrap_sampling_amount_of_cookies_means(country)

    # print(str(cmp_count_total))
    # print(str(cmp_count_total / 30))


run()
