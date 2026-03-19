import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix/netflix_titles.csv")
#Checknig the Basic information
print(df.info())
print(df.head())
print(df.describe())

#Checking for missing values
print("Number of missing Values: ")
print(df.isnull().sum())

#Remove duplicates
print("Number of duplicates: ")
print(df.duplicated().sum())

#if any Missing value it print 0
print(df.fillna(0))

#shape of the dataset
print("Shape of the dataset: ", df.shape)

#Distribution of Movies and TV shows
plt.figure(figsize=(6,4))
sns.countplot(x="type",data = df)
plt.title("Distribution of Movies and TV shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
