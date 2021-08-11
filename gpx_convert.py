'''
converts an input .gpx file to return  a data frame containing latitudes,
longitudes and elevation.

Parameters:
current_file: an input .gpx file 
'''


import gpxpy
import gpxpy.gpx 
import os 
import pandas as pd

def gpx_converter(current_file):
    try:
        gpx = gpxpy.parse(current_file)

        lats = []
        longs = []
        elevs = []

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    lats.append(point.latitude)
                    longs.append(point.longitude)
                    elevs.append(point.elevation)
    
        df = pd.DataFrame({'Latitude':lats, 'Longitude':longs, 'elevation':elevs})
        return df

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)


