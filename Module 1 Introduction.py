""""
Introduction of Data Analysis with Python
Objective :
    1. Data Acquisition
    2. Basic Insight of dataset

Data source: https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data
"""

# Import pandas library
import pandas as pd
import numpy as np
import requests

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

# This function will download the dataset into your browser
def download (url, filename):
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

# Read Data

# Download the date in local machine.
download(path, "auto.csv")

# Read the online file by the URL.
df = pd.read_csv(path, header=None)

print df.head(5)

# QUESTION NO 1: Check the bottom 10 rows of data frame "df".

print df.tail(10)


# Add Headers
# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

print headers

df.columns = headers
print df.head(10)

