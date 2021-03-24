import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def rounded_mean_value(value) -> int:
    return round(np.mean(value))


outDir = "/Users/koen/Documents/Research/"

df = pd.read_json("output_fr_js_disabled.json")

labels = ['Functionality', 'Necessary', 'Performance', 'Target/Ad', 'Unknown']
values = [rounded_mean_value(df.functionality), rounded_mean_value(df.necessary), rounded_mean_value(df.performance), rounded_mean_value(df.target_and_ad), rounded_mean_value(df.unknown)]

plt.bar(labels, values, align="center")
plt.title("France top 500 - means of cookie purposes before consent - JS disabled")
plt.tight_layout()
plt.savefig(outDir + "france_top_500_cookies_purposes_js_disabled")
plt.clf()
