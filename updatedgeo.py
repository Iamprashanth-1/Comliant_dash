#token = open(".mapbox_token").read() # you will need your own token

import pandas as pd
import pathlib
from collections import Counter
import json
#in_cities = pd.read_csv("E:\in.csv")
#print(us_cities)
import os
import plotly.graph_objects as go
import uuid


import plotly.express as px
df= pd.read_csv('data/customer29.csv')
s=[]
for i in df['City']:
    s.append(i)
sf=dict(Counter(s))
a=list(sf.keys())
b=list(sf.values())
#print(a)
filename="data/indi.json"
with open(filename) as f:
    data = json.load(f)
    json.dump(data, open("data.json", "w"), indent = 4)
with open(filename, 'r') as f:
    data = json.load(f)
   # print(data[1]['admin']==a[9])
    for i in range(len(data)):
       data[i]['compliants']=0
    for i in range(len(data)):
        for j in range(len(a)):
            if data[i]['City']==a[j]:
                data[i]['compliants']=b[j]

#json.dump(data, open(f, "w"), indent = 4)
tempfile = os.path.join(os.path.dirname(filename), str(uuid.uuid4()))
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

# rename temporary file replacing old file
#os.rename(tempfile, filename)

#print(tempfile)
        
in_cities = pd.read_json("data/indi.json")

fig9=go.Figure()
    #in_cities[population]
#print(in_cities)
import plotly.express as px
px.set_mapbox_access_token('pk.eyJ1Ijoid2ViZXhwZXJ0c3VqZWV0IiwiYSI6ImNqdmh4MXM0dDAwMWs0NXFyNHkxc2o1eGwifQ.jgbBoS14uvv8i_lMrCQF5A')
df = px.data.carshare()
fig9 = px.scatter_mapbox(in_cities, lat="Lat", lon="Long", hover_name="City", hover_data=["compliants"],
                        color_discrete_sequence=["red"], zoom=3.7, height=700)

fig9.update_layout(margin={"r":0,"t":0,"l":0,"b":1})
fig9.update_layout(
    template="plotly_dark",
    annotations=[
        dict(
            text="Source: NOAA",
            showarrow=False,
            xref="paper",
            yref="paper",
            x=0,
            y=0)
    ]
)
#fig.show()
import dash
import dash_core_components as dcc
import dash_html_components as html
import uuid
import plotly.graph_objects as go # or plotly.express as px
#fig = go.Figure()

