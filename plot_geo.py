import geopandas
import numpy as np
import pandas as pd
from shapely.geometry import Point
import missingno as msn
import seaborn as sns
import matplotlib.pyplot as plt
import json

country = geopandas.read_file('India/Indian_States.shp')

country['total_cases'] = -1

# country.loc[country.st_nm == 'Andaman & Nicobar Island', 'total_cases'] = 100

with open('Data/data.json') as f:
	data = json.load(f)

for state in data:
	country.loc[country.st_nm == state['state'], 'total_cases'] = int(state['total_cases'])

country = country[country.total_cases != -1]

ax = country.plot(column='total_cases', legend=True)
country.apply(lambda x: ax.annotate(s=str(x.total_cases), xy=x.geometry.centroid.coords[0], ha='center'),axis=1);
ax.set_title('Heat Map for COVID-19')


plt.show()