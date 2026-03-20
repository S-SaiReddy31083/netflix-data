import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import  sklearn


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

#Predicting the Whether title is Movie or Tv show
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

le_type = LabelEncoder()
le_country = LabelEncoder()
le_rating = LabelEncoder()

df["type"] = le_type.fit_transform(df["type"])
df["country"] = le_country.fit_transform(df["country"])
df["rating"] = le_rating.fit_transform(df["rating"])


#Input features and target/output variable 
x = df[["country","rating"]]
y = df["type"]

#Logistic Regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x,y)

#Making the Predictions
y_pred = model.predict(x)
print("Predicted Values: ",y_pred)

#Checking the Accuracy of the model
from sklearn.metrics import accuracy_score
print("Accuracy of the model: ",accuracy_score(y,y_pred))

#Classification Report
from sklearn.metrics import classification_report
print("Classification_report: ",classification_report(y, y_pred))

#Confusion matrix
from sklearn.metrics import confusion_matrix
print("Confusion Matrix: ",confusion_matrix(y, y_pred))

#Graph representation of the confusion matrix using the seaborn library
sns.heatmap(confusion_matrix(y, y_pred), annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

#Checking in the Line plot the relationship between country and rating
sns.lineplot(x="country",y = "rating", data = df)
plt.title("Relationship between country and rating")
plt.xlabel("Country")
plt.ylabel("Rating")
plt.show()