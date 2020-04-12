import plotly.graph_objects as go
from collections import Counter
import datetime
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
fig7=go.Figure()

dff= pd.read_csv('data/customer29.csv')
c=[]
for kk in dff['Date received']:
    c.append(kk)
dd=dict(Counter(c))
mm=list(dd.values())
hg=list(dd.keys())
kd=hg[0]
#print(dd)
pp=[]
ee=[]
for i in range(len(hg)):
    a=[]
    s=str(hg[i])
   # print(s)
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
    a.append(aa)      
    #print(a)
    e=str(a[2])+'-'+str(a[0])+'-'+str(a[1])
    ee.append(e)
    pp.append(datetime.datetime(year=a[2], month=a[0], day=a[1]))
#print(ee)
dif=dict()
sif=[]
dif['Date']=ee
dif['compliants']=mm
sif.append(dif)
#print(dif)
#print(pp)


#fig7 =px.line(dif,x='Date',y='compliants',title='Time Series with Range Slider and Selectors')
#fig7=go.Figure(data=[go.Scatter(x=pp,y=mm)])
fig7 =px.line(dif,x='Date',y='compliants',title='Time Series with Range Slider and Selectors')

fig7.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)


fig7.update_layout(
    height=600,
    template="plotly_dark",

)
fig7.update_xaxes(rangeslider_visible=True) 
