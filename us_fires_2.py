# Imports
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Load file and convert
infile = open("US_fires_9_14.json", "r")
outfile = open("US_fires_9_14_readable", "w")

fires = json.load(infile)
json.dump(fires, outfile, indent=4)

brights = []
lons = []
lats = []

# List of fires
for fire in fires:
    if int(fire["brightness"]) > 450:
        lon = fire["longitude"]
        lat = fire["latitude"]
        bright = int(fire["brightness"])

        lons.append(lon)
        lats.append(lat)
        brights.append(bright)

print(lats[:10])

# Plot the map
fire_data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [bright / 30 for bright in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="US Fires - 9/14/2020 through 9/20/2020")
fig1 = {"data": fire_data, "layout": my_layout}
offline.plot(fig1, filename="US_fires_9_1_readable.html")