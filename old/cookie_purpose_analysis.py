import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_json("../cookiepedia_purposes/output_be.json")

labels = df.url
target_and_ad = df.target_and_ad.values.sum()
necessary = df.necessary.values.sum()
unknown = df.unknown.values.sum()

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, target_and_ad, width, label='Target/Ad')
rects2 = ax.bar(x + width/2, necessary, width, label='Necessary')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of cookies')
ax.set_title('Number of cookies grouped by purpose')
ax.set_xticks(x)
#ax.set_xticklabels(labels, rotation='vertical')
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()


