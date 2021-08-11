'''
Plotting latitude and longditude coordinates with folium to create the heatmap
and saving heatmp as HTML file
'''


import folium
from folium import plugins
import numpy as np
from gpx_convert import gpx_converter
from multiple_files import multiple

coords = multiple('activities')

mapmap = folium.Map(location=[coords.mean()['Latitude'],coords.mean()['Longitude']])

heat_df = coords[['Latitude', 'Longitude']]
heat_df = heat_df.dropna(axis=0, subset=['Latitude', 'Longitude'])

heat_data = [[row['Latitude'],row['Longitude']] for index, row in heat_df.iterrows()]
plugins.HeatMap(heat_data).add_to(mapmap)

mapmap.save('map.html')