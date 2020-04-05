#token = open(".mapbox_token").read() # you will need your own token

import pandas as pd
import pathlib
from collections import Counter
import json
#in_cities = pd.read_csv("E:\in.csv")
#print(us_cities)
import os
import uuid


import plotly.express as px
df= pd.read_csv('F:\dash-nlp-master\data\customer29.csv')
s=[]
for i in df['State']:
        s.append(i)
sf=dict(Counter(s))
a=list(sf.keys())
b=list(sf.values())
#print(a)
filename="data/in.json"
with open(filename) as f:
    data = json.load(f)
    for i in range(len(data)):
        data[i]["compliants"] =0
    json.dump(data, open("data.json", "w"), indent = 4)
with open(filename, 'r') as f:
    data = json.load(f)
   # print(data[1]['admin']==a[9])
    for i in range(len(data)):
       data[i]['compliants']=0
    for i in range(len(data)):
        for j in range(len(a)):
            if data[i]['admin']==a[j]:
                data[i]['compliants']=b[j]

#json.dump(data, open(f, "w"), indent = 4)
tempfile = os.path.join(os.path.dirname(filename), str(uuid.uuid4()))
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

# rename temporary file replacing old file
#os.rename(tempfile, filename)

#print(tempfile)
        
in_cities = pd.read_json("data/in.json")

            
    #in_cities[population]
#print(in_cities)

fig2 = px.scatter_mapbox(in_cities, lat="lat", lon="lng", hover_name="admin", hover_data=["compliants"],
                        color_discrete_sequence=["blue"], zoom=4, height=700)
fig2.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ])
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":1})
#fig.show()
import dash
import dash_core_components as dcc
import dash_html_components as html
import uuid
import plotly.graph_objects as go # or plotly.express as px
#fig = go.Figure()

