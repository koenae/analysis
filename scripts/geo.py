import json

import numpy as np
import pandas as pd
import plotly.express as px

from scripts.utils import get_amount_of_cookies

data = [['France', np.mean(get_amount_of_cookies('france').values)],
        ['Belgium', np.mean(get_amount_of_cookies('belgium').values)],
        ['Netherlands', np.mean(get_amount_of_cookies('the_netherlands').values)]]

df = pd.DataFrame(data, columns=['Country', 'Number of cookies mean'])

with open('./geo/custom.geo.json') as response:
    countries = json.load(response)

fig = px.choropleth(df, geojson=countries, color="Number of cookies mean",
                    locations="Country", featureidkey="properties.admin",
                    projection="mercator", color_continuous_scale=px.colors.sequential.Viridis
                    )
fig.update_geos(fitbounds="locations", scope="europe", visible=False, showcountries=True, resolution=110,
                countrycolor="Black")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, legend=dict(orientation="h"))
fig.show()
