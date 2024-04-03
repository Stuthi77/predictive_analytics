# -*- coding: utf-8 -*-
"""lvadsusr80_D.stuthi_lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tZQP-tVQqf3yjXFGOGxsbTff0ncCS041
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report,accuracy_score
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

df=pd.read_csv('/content/seeds.csv')
df

df.isnull().sum()

df=df.fillna(df.mean())

df.isnull().sum()

df.isna().sum()

z_score=abs((df-df.mean())/df.std())
print(z_score)
df=df[z_score<3]
df

df.isna().sum()

df.info()

df.columns

X=df[['Area', 'Perimeter', 'Compactness', 'Length of kernel','Width of kernel', 'Asymmetry coefficient', 'Length of kernel groove']]
scaler=StandardScaler()
X_scaler=scaler.fit_transform(X)
X.isna().sum()
X=X.dropna()

scaler=StandardScaler()
X_scaler=scaler.fit_transform(X)
wccs=[]
for i in range(1,40):
  Model=KMeans(n_clusters=i)
  Model.fit(X_scaler)
  wccs.append(Model.inertia_)

plt.plot(range(1, 40), wccs, marker='o', linestyle='--')
plt.title('Elbow Method')
plt.show()

k=5
Model=KMeans(n_clusters=5,init="k-means++",random_state=42)
Model.fit(X_scaler)
pred=Model.predict(X_scaler)
from sklearn.metrics import silhouette_score
a=silhouette_score(X_scaler,labels=Model)
print(a)