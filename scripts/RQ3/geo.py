import json

import numpy as np
import pandas as pd
import plotly.express as px

from scripts.utils import get_amount_of_cookies

data = [['France', np.mean(get_amount_of_cookies('france').values)],
        ['Belgium', np.mean(get_amount_of_cookies('belgium').values)],
        ['Netherlands', np.mean(get_amount_of_cookies('the_netherlands').values)],
        ['Bulgaria', np.mean(get_amount_of_cookies('bulgaria').values)],
        ['Croatia', np.mean(get_amount_of_cookies('croatia').values)],
        ['Austria', np.mean(get_amount_of_cookies('austria').values)],
        ['Cyprus', np.mean(get_amount_of_cookies('cyprus').values)],
        ['Czech Republic', np.mean(get_amount_of_cookies('czech_republic').values)],
        ['Denmark', np.mean(get_amount_of_cookies('denmark').values)],
        ['Estonia', np.mean(get_amount_of_cookies('estonia').values)],
        ['Finland', np.mean(get_amount_of_cookies('finland').values)],
        ['Germany', np.mean(get_amount_of_cookies('germany').values)],
        ['Greece', np.mean(get_amount_of_cookies('greece').values)],
        ['Hungary', np.mean(get_amount_of_cookies('hungary').values)],
        ['Ireland', np.mean(get_amount_of_cookies('ireland').values)],
        ['Italy', np.mean(get_amount_of_cookies('italy').values)],
        ['Latvia', np.mean(get_amount_of_cookies('latvia').values)],
        ['Lithuania', np.mean(get_amount_of_cookies('lithuania').values)],
        ['Luxembourg', np.mean(get_amount_of_cookies('luxembourg').values)],
        ['Malta', np.mean(get_amount_of_cookies('malta').values)],
        ['Norway', np.mean(get_amount_of_cookies('norway').values)],
        ['Poland', np.mean(get_amount_of_cookies('poland').values)],
        ['Portugal', np.mean(get_amount_of_cookies('portugal').values)],
        ['Romania', np.mean(get_amount_of_cookies('romania').values)],
        ['Slovakia', np.mean(get_amount_of_cookies('slovakia').values)],
        ['Slovenia', np.mean(get_amount_of_cookies('slovenia').values)],
        ['Spain', np.mean(get_amount_of_cookies('spain').values)],
        ['Sweden', np.mean(get_amount_of_cookies('sweden').values)],
        ['Switzerland', np.mean(get_amount_of_cookies('switzerland').values)],
        ['United Kingdom', np.mean(get_amount_of_cookies('united_kingdom').values)]]

df = pd.DataFrame(data, columns=['Country', 'Number of cookies mean'])

with open('./geo/custom.geo.json') as response:
    countries = json.load(response)

fig = px.choropleth(df, geojson=countries, color="Number of cookies mean",
                    locations="Country", featureidkey="properties.admin",
                    projection="mercator", color_continuous_scale="Reds"
                    )
fig.update_geos(fitbounds="locations", scope="europe", visible=False, showcountries=True, resolution=110,
                countrycolor="Black")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
# fig.write_image("./plots/general/map.png", width=450, height=250)
