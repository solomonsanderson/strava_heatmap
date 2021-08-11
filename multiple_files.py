'''
iterates over the files in the directory of .gpx files
'''


import pathlib
from gpx_convert import gpx_converter
import pandas as pd
from alive_progress import alive_bar
from time import sleep
import os

def multiple(directory):
    frames = []

    number = len([item for item in os.listdir(directory)])
    with alive_bar(number, bar='classic', spinner = 'ball_scrolling') as bar:
        for path in pathlib.Path(directory).iterdir():
            # print(path)
            if path.is_file():
                current_file = open(path,'r')
                df = gpx_converter(current_file)
                frames.append(df)
                frame = pd.concat(frames)
                bar()
    return frame

