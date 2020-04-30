import geopandas
import numpy as np
import pandas as pd
from shapely.geometry import Point
import missingno as msn
import seaborn as sns
import matplotlib.pyplot as plt
import json

country = geopandas.read_file('India/Indian_States.shp')
# print(help(geopandas.geodataframe.GeoDataFrame))

with open('Data/data.json') as f:
	data = json.load(f)

country['total_cases'] = -1

for state in data:
	country[country.st_nm == state['state']].total_cases = pd.Series([int(state['total_cases'])])
	print(type(country[country.st_nm == state['state']].total_cases))
	print(type(pd.Series(int(state['total_cases']))))
	print(country[country.st_nm == state['state']])
	print(pd.Series(int(state['total_cases'])))
	break


# fin.plot()
# plt.show()
	

# df = pd.DataFrame(data)
# plt.figure(1)
# plt.title('To check for missing values')
# msn.bar(df, color='darkolivegreen')

# # country.plot()
# plt.show()

# world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
# print(world.info())
# cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))

# world = world[(world.pop_est>0) & (world.name!="Antarctica")]
# world['gdp_per_cap'] = world.gdp_md_est / world.pop_est


# print(world.info())
# world.plot(column='pop_est')


# plt.show()