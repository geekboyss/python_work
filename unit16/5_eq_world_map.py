import plotly.express as px
import pandas as pd
import json

filename = 'data2/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eg_data = json.load(f)

# readable_file = 'data2/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eg_data, f, indent=4)

all_eq_dicts = all_eg_data['features']

mags, titles, lons, lats = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=["经度", "维度", "位置", "震级"]
)
data.head()

fig = px.scatter(
    data,
    x="经度",
    y="维度",

    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="Global Earthquakes",
    size="震级",
    size_max=10,
    color="震级",
    hover_name="位置",
)

fig.write_html("global_earthquakes.html")
fig.show()