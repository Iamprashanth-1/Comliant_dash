import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from collections import Counter
import pandas as pd


fig1 = go.Figure()
def statecity(pl):
    s=[]
    for i in pl:
            s.append(i)
    sf=dict(Counter(s))
    a=list(sf.keys())
    b=list(sf.values())
    #print(a,b)
    fig1.add_trace(
        go.Bar(
            x=b,
            y=a,
            marker=go.bar.Marker(
                color="yellow",
                line=dict(color="rgb(0, 0, 0)",
                          width=1)
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
        height=700,
        width=535,
        bargap=0.15,
        bargroupgap=0.1,
        barmode="stack",
        hovermode="x",
        margin=dict(r=1, l=10, b=10, t=100),
        title=("NPCI FASTAG COMPLIANTS<br>" +
               "<i>Based On States</i>"),

    )
    fig1.update_layout(
        template="plotly_dark",
        annotations=[
            dict(
                text="",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0,
                y=0)
        ]
    )
    return fig1

#fig.show()
#app = dash.Dash()


#app.run_server(debug=True, use_reloader=False)
