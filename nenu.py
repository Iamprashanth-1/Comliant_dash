# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# required imports

import xlrd
import random
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt

sns.set_style('whitegrid')


# %%
# preview the prepared DataFrame

df= pd.read_csv('F:\dash-nlp-master\data\customer29.csv')
#df = pd.DataFrame(final_list, columns=columns)
df.head()


# %%
# Keeping only the required columns

state_wise_total= df[['State', 'Date received']]
data_for_map = state_wise_total
data_for_map.head()


# %%
# reading the state wise shapefile of India in a GeoDataFrame and preview it

fp = "E:\Igismap\Indian_States.shp"
map_df = gpd.read_file(fp)
#map_df.head()
map_df

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

data_for_map3
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
merged.plot(column='Count', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)


# %%
# We save the output as a PNG image

fig.savefig("F:\dash-nlp-master\State_wis.png", dpi=100)
