# Basic Analysis and Visualization
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import csv
from datetime import timedelta
# Mapping
import geopandas
import geopy
from geopy.geocoders import Nominatim
import folium
from geopy.extra.rate_limiter import RateLimiter
from folium import plugins
from folium.plugins import MarkerCluster
# Statistical OLS Regression Analysis matplotlib inline
import statsmodels.api as sm
from statsmodels.compat import lzip
from statsmodels.formula.api import ols
#Scipy sklearn Predictions
from sklearn.ensemble import GradientBoostingRegressor

df = pd.read_csv("Crime.csv")
df = df.set_index("Victims")

group_by_address = df.groupby("Block Address")["Block Address"].count().sort_values()

group_by_crime = df.groupby("Crime Name2")["Crime Name2"].count().sort_values()

m = folium.Map([32.37,86.3077], zoom_start=10)
for index, row in df.iterrows():
    folium.CircleMarker([row['Latitude'], row['Longitude']],
                        radius=3,
                        popup=row['Crime Name1'],
                        fill_color="#3db7e4", # divvy color
                       ).add_to(m)
m.save("footprint.html")
