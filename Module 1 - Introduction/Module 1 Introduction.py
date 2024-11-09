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

### Read Data

# Download the date in local machine.
download(path, "auto.csv")

# Read the online file by the URL.
df = pd.read_csv(path, header=None)

print df.head(5)

""" 
QUESTION NO 1: Check the bottom 10 rows of data frame "df".

 Hindprint df.tail(10)
"""

### Add Headers
# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

print headers

df.columns = headers
print df.head(10)

""" 
QUESTION NO : 2 Find the name of the columns of the dataframe.

Hinds : print df.columns
"""

### SAVE DATA
df.to_csv("automobile.csv", index=False)

### BASIC INSIGHT OF THE DATASET
# Data Type : Data has variety type, including object, float, int bool datetime64.
print df.dtypes

# Describe: To get the statistical summary of the each columns, count value, mean value, standard deviation  etc.
print df.describe()

# Describe function by default work on Int type, however we can apply all.
print df.describe(include='all')

""""
Question #3: 
You can select the columns of a dataframe by indicating the name of each column. For example, you can select the three columns as follows:

dataframe[[' column 1 ',column 2', 'column 3']]

Where "column" is the name of the column, you can apply the method ".describe()" to get the statistics of those columns as follows:

dataframe[[' column 1 ',column 2', 'column 3'] ].describe()

Apply the method to ".describe()" to the columns 'length' and 'compression-ratio'.

"""

# Answer 3:
print df[['length', 'compression-ratio']].describe()

# Info : Concise summary of the dataframe.
df.info()

# LAB No 1: END - THANK YOU!