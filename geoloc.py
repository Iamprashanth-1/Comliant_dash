#token = open(".mapbox_token").read() # you will need your own token

import pandas as pd
import pathlib
from collections import Counter
import json

import os
import uuid
import plotly.graph_objects as go

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
        
df = pd.read_json("data/in1.json", orient='records')

            
    #in_cities[population]
#print(in_cities)

df['text'] = df['admin'] + '<br>Complaints ' + (df['compliants']).astype(str)
limits = [(0,3),(4,10),(11,20),(20,30)]

fig2 = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    df_sub= df
    fig2.add_trace(go.Scattergeo(
    locationmode = 'ISO-3',
    lon = df_sub['lng'],
    lat = df_sub['lat'],
    text = df_sub['text'],
    marker = dict(
        size = df_sub['compliants']*80,
        color = 'lightgreen',
        line_color='rgb(40,40,40)',
        line_width=0.5,
        sizemode = 'area'
    ),
    name = '{0} - {1}'.format(lim[0],lim[1])))

fig2.update_layout(
        title_text = 'NPCI Statewise Complaints',
        showlegend = True,
        autosize=False,
         width=1000,
        height=1000,
        geo = dict(
            scope = 'asia',
            landcolor = 'rgb(217, 217, 217)',
        )
    )

#fig2.show()