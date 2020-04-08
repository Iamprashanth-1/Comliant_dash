#token = open(".mapbox_token").read() # you will need your own token

import pandas as pd
import pathlib
from collections import Counter
import json
#in_cities = pd.read_csv("E:\in.csv")
#print(us_cities)
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import os
import uuid


import plotly.express as px
df= pd.read_csv('data/customer29.csv')
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

fig3 = px.scatter_mapbox(in_cities, lat="lat", lon="lng", hover_name="admin", hover_data=["compliants"],
                        color_discrete_sequence=["blue"], zoom=3.72, height=600,width=570)
fig3.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                "https://api.mapbox.com/styles/v1/prashanth-reddy/ck8q89rc21jha1iqj2znnisqk.html?fresh=true&title=view&access_token=pk.eyJ1IjoicHJhc2hhbnRoLXJlZGR5IiwiYSI6ImNrOHE4NG41ZzAwemIza3A1a29uMTI5dmkifQ.gMkPHTgJU_mRp1cRBiiX3g"
            ]
        }
      ])
fig3.update_layout(margin={"r":1,"t":1,"l":1,"b":2})
#fig3.show()



