# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import requests

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


file_name = "auto.csv"

### Data Normalization
""" 
Normalization is the process of the transforming value of several into a similar range. Typical normatlization including scaling the 
variable so the variable average is 0, scaling the variable so the variance is 1, or scaling the variable so the variable values range
from 0 to 1.
Example: To demonstate normalization, to scale the columns "Length", "Width"  and "Height".
"""

df = pd.read_csv(file_name, names=headers)

df['height'] = df['height']/df['height'].max()

print df[['length','width','height']].head()