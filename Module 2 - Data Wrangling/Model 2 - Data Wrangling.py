"""
Objective:
i. Handling missing values
ii. Correct data format
iii. Standardize and Normalize Data.
iv Binning
v. Indicator variable
"""

# Data Wrangling is the process of converting data from the initial format to a format that may be better for analysis.

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import requests

# Download the data.
def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

# URL Link
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

download(filename, "auto.csv")

file_name = "auto.csv"
df = pd.read_csv(file_name, names = headers)

print df.head()

### Identify and handling missing value
df.replace("?", np.nan, inplace=True)

print df.head()

### Evaluating for missing data.
""" Following method can be use for identify the missing value.
    i. isnull()
    ii. notnull()
    
"""

missing_data = df.isnull()
print missing_data.head()

# "True" means the value is a missing value while "False" means the value is not a missing value.

# Count missing value in each column
for column in missing_data.columns.values.tolist():
    print column
    print missing_data[column].value_counts()
    print " "

# Calculate the mean value of the "normalized-losses" column

avg_norm_loss = df['normalized-losses'].astype('float').mean(axis=0)
print avg_norm_loss

df['normalized-losses'].replace(np.nan, avg_norm_loss, inplace=True)
print df['normalized-losses']


# Calculate the mean value for the "bore" column

avg_bore = df["bore"].astype('float').mean(axis=0)
print avg_bore

df["bore"].replace(np.nan, avg_bore, inplace=True)
print df["bore"]

# Calculate the mean value for the "stroke" column

avg_stroke = df["stroke"].astype('float').mean(axis=0)
print avg_stroke

df["stroke"].replace(np.nan, avg_stroke, inplace=True)
print df["stroke"]

# Calculate the mean value for the "horsepower" column

avg_horsepower = df["horsepower"].astype("float").mean(axis=0)
print avg_horsepower

df["horsepower"].replace(np.nan, avg_horsepower, inplace=True)
print df["horsepower"]

# Calculate the mean value for the "peak-rpm" column

avg_peakrpm = df["peak-rpm"].astype("float").mean(axis=0)
print avg_peakrpm

df["peak-rpm"].replace(np.nan, avg_peakrpm, inplace=True)
print df["peak-rpm"]

# Value Count

print df['num-of-doors'].value_counts()

df['num-of-doors'].replace(np.nan, "four", inplace=True)
print df['num-of-doors'].value_counts()

df.dropna(subset=['price'], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
print df.head()

# Correct Data Format, dtype() and astype()
print df.dtypes