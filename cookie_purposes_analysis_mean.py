import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def rounded_mean_value(value) -> int:
    return round(np.mean(value))


df = pd.read_json("output.json")

labels = ['Necessary', 'Target/Ad', 'Unknown']
values = [rounded_mean_value(df.necessary), rounded_mean_value(df.target_and_ad), rounded_mean_value(df.unknown)]

plt.bar(labels, values, align="center")
plt.title("Belgium top 500 - means of cookie purposes before consent")
plt.tight_layout()
plt.show()
