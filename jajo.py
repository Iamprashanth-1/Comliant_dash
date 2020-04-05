import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from collections import Counter
import pandas as pd
df= pd.read_csv('F:\dash-nlp-master\data\customer29.csv')

fig1 = go.Figure()
s=[]
for i in df['State']:
        s.append(i)
sf=dict(Counter(s))
a=list(sf.keys())
b=list(sf.values())

fig1.add_trace(
    go.Bar(
        x=b,
        y=a,
        marker=go.bar.Marker(
            color="rgb(253, 240, 54)",
            line=dict(color="rgb(0, 0, 0)",
                      width=2)
        ),
        orientation="h",
    )
)

# Add image
fig1.add_layout_image(
    dict(
        source='assets/npci_logo.png',
        xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    )
)

# update layout properties
fig1.update_layout(
    autosize=False,
    height=800,
    width=700,
    bargap=0.15,
    bargroupgap=0.1,
    barmode="stack",
    hovermode="x",
    margin=dict(r=20, l=300, b=75, t=125),
    title=("NPCI FASTAG COMPLIANTS<br>" +
           "<i>Based On States</i>"),
)

#fig.show()
#app = dash.Dash()


#app.run_server(debug=True, use_reloader=False)
