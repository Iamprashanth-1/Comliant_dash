# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# required imports

import xlrd
import random
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib
from collections import Counter

import flask
import dash
import dash_table
import matplotlib.colors as mcolors
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import base64
from os import path, getcwd
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

sns.set_style('whitegrid')


# %%
# preview the prepared DataFrame
def mergedd(s):

    df= pd.read_csv('data/customer29.csv')
    #df = pd.DataFrame(final_list, columns=columns)
    df.head()


    # %%
    # Keeping only the required columns

    state_wise_total_crimes = df[['State', 'Date received']]
    data_for_map = state_wise_total_crimes
    data_for_map.head()


    # %%
    # reading the state wise shapefile of India in a GeoDataFrame and preview it

    fp = "E:\Igismap\Indian_States.shp"
    map_df = gpd.read_file(fp)
    #map_df.head()
    #map_df

    # %%
    # Correct spellings of states from out dataframe to match those of GeoDataframe
    # I found these 4 names manually

    #data_for_map['State'].iloc[1] = 'Arunanchal Pradesh'

    # %%
    # Plot the default map

    #map_df.plot()


    # %%
    # Join both the DataFrames by state names
    #print(type(map_df))
    data_for_map1= data_for_map['State'].value_counts().index
    data_for_map2= data_for_map['State'].value_counts()

    #print(data_for_map1, data_for_map2)
    #merged= data_for_map2
    data_for_map3= pd.DataFrame(list(zip(data_for_map1, data_for_map2)), 
                   columns =['State', 'Count'])

   # data_for_map3
    merged = map_df.set_index('st_nm').join(data_for_map3.set_index('State'))
    merged.head()


    # %%
    # NA check

    merged.isna().sum()
    merged.fillna(0)

    # %%
    # Summary to get the max and min value

    merged.describe()


    # %%
    # create figure and axes for Matplotlib and set the title
    fig, ax = plt.subplots(1, figsize=(10, 6))
    ax.axis('off')
    ax.set_title('State Wise NPCI complaints in India', fontdict={'fontsize': '25', 'fontweight' : '3'})

    # plot the figure
    (merged.plot(column='Count', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True))



    # %%
    # We save the output as a PNG image

    fig.savefig("F:\dash-nlp-master\State_wise.png", dpi=100)
    for i in df['State']:
        return i
def plotly_wordclou(df):
    
    df.head()


    # %%
    # Keeping only the required columns

    state_wise_total_crimes = df[['State', 'Date received']]
    data_for_map = state_wise_total_crimes
    data_for_map.head()


    # %%
    # reading the state wise shapefile of India in a GeoDataFrame and preview it

    fp = "E:\Igismap\Indian_States.shp"
    map_df = gpd.read_file(fp)
    #map_df.head()
    #map_df

    # %%
    # Correct spellings of states from out dataframe to match those of GeoDataframe
    # I found these 4 names manually

    #data_for_map['State'].iloc[1] = 'Arunanchal Pradesh'

    # %%
    # Plot the default map

    #map_df.plot()


    # %%
    # Join both the DataFrames by state names
    #print(type(map_df))
    data_for_map1= data_for_map['State'].value_counts().index
    data_for_map2= data_for_map['State'].value_counts()

    #print(data_for_map1, data_for_map2)
    #merged= data_for_map2
    data_for_map3= pd.DataFrame(list(zip(data_for_map1, data_for_map2)), 
                   columns =['State', 'Count'])

   # data_for_map3
    merged = map_df.set_index('st_nm').join(data_for_map3.set_index('State'))
    complaints_text = list(df["State"].dropna().values)
    if len(complaints_text) < 1:
        return {}, {}, {}

        # join all documents in corpus
    text = " ".join(list(complaints_text))

    word_clou = WordCloud(stopwords=set(STOPWORDS), max_words=100, max_font_size=90)
    word_clou.generate(text)

    word_list = []
    freq_list = []
    fontsize_list = []
    position_list = []
    orientation_list = []
    color_list = []
    s=[]
    for i in df['State']:
        s.append(i)
    sf=dict(Counter(s))


    for word in sf :
        word_list.append(word)
        freq_list.append(sf[word])
        #fontsize_list.append(fontsize)
        #position_list.append(position)
       # orientation_list.append(orientation)
        color='#ff0000'
        color_list.append(color)

        # get the positions
    x_arr = list(range(1,len(sf)+1))
    y_arr = []
    for i in freq_list:
        y_arr.append(i)

        # get the relative occurence frequencies
    new_freq_list = []
    for i in freq_list:
        new_freq_list.append(i * 80)

    trace = go.Scatter(
            x=x_arr,
            y=y_arr,
            textfont=dict(size=new_freq_list, color=color_list),
            hoverinfo="text",
            textposition="top center",
            hovertext=["{0} - {1}".format(w, f) for w, f in zip(word_list, freq_list)],
            mode="text",
            text=word_list,
        )

    layout = go.Layout(
        {
            "xaxis": {
                "showgrid": False,
                "showticklabels": False,
                "zeroline": False,
                "automargin": True,
                "range": [-100, 250],
            },
            "yaxis": {
                "showgrid": False,
                "showticklabels": False,
                "zeroline": False,
                "automargin": True,
                "range": [-100, 450],
            },
            "margin": dict(t=20, b=20, l=10, r=10, pad=4),
            "hovermode": "closest",
            }
        )

    wordclou_figure_data = {"data": [trace], "layout": layout}
    word_list_top = word_list[:25]
    word_list_top.reverse()
    freq_list_top = freq_list[:25]
    freq_list_top.reverse()

    frequenc_figure_data = {
            "data": [
                {
                    "y": word_list_top,
                    "x": freq_list_top,
                    "type": "bar",
                    "name": "",
                    "orientation": "h",
                }
            ],
            "layout": {"height": "550", "margin": dict(t=20, b=20, l=100, r=20, pad=4)},
        }
    return frequenc_figure_data


