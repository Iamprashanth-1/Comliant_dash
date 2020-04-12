import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import matplotlib
import plotly.express as px
import pandas as pd
from datetime import date,datetime
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#import jajo 
from collections import Counter
fig5= go.Figure()
df= pd.read_csv('data/customer29.csv')
def dudos(thug,life,idil):
    #print(df['Date received'][0])
    rr=idil
    poi=[]
    for i in range(len(rr)):
        poi.append(rr[i])
    hoi=dict(Counter(poi))
    #print(hoi)
    
    date_format = '%m-%d-%y'
    cc=0
    sss=0
    mm=0
    for i in range(len(thug)):
        a=[]
        s=thug[i]
        for j in range(len(s)):
            if s[j]=='-':
                a.append(int(s[:j]))
                if s[j]==s[j+2]:
                    a.append(int(s[j+1:j+2]))
                else:
                    a.append(int(s[j+1:j+3]))
                break
        #print(a)
        aa=int(s[-4:])
        a.append((aa))

    #    s=df['Date received'][i]
        ss=life[i]
        b=[]
        for j in range(len(ss)):
            if ss[j]=='-':
                b.append(int(ss[:j]))
                if ss[j]==ss[j+2]:
                    b.append(int(ss[j+1:j+2]))
                else:
                    b.append(int(ss[j+1:j+3]))
                break
        aaa=int(ss[-4:])
        b.append((aaa))
        #print(a,b)

        d=abs(date(a[2],a[0],a[1])-date(b[2],b[0],b[1]))
    
        #print(d)
        if d.days==0:
            cc+=1
        elif d.days==1:
            sss+=1
        else:
            mm+=1
    
    lol=list(hoi.keys())
    mol=list(hoi.values())
    # Create figure
    colors = ['pink', 'mediumturquoise', 'darkorange', 'lightgreen']
    colors1=['red','yellow','brown','grey','blue','tan']
    colo=colors+colors1
    # Disable the autosize on double click because it adds unwanted margins around the image
    # More detail: https://plotly.com/python/configuration-options/
    #fig.show(config={'doubleClick': 'reset'})
    fig5 = make_subplots(1, 2,specs=[[{'type':'domain'}, {'type':'domain'}]])
    #subplot_titles=['Resolved within', 'How they submitted'])
    fig5.add_trace(go.Pie(labels=['Resolved within 24hrs','resolved within 48hrs','Unresolved'], values=[cc,sss,mm],sort=False, scalegroup='one',
    name='Resolved within'), 1, 1)
   # fig5.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                    #  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig5.add_trace(go.Pie(labels=lol, values=mol,sort=False, scalegroup='one',
    name='How they resolved'), 1, 2)
    fig5.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                      marker=dict(colors=colo, line=dict(color='#000000', width=2)))

    fig5.update_layout(
        template="plotly_dark",
        margin=dict(r=10, t=25, b=40, l=60),
        annotations=[
            dict(
                text="Source: NPCI",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0,
                y=0)
        ]
    )
    #fig5.update_layout(title_text='RESOLVED ISSUES WiTHIN hrs')
    return fig5
