# -*- coding: utf-8 -*-
"""lvadsusr80_D.stuthi_lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EMg-Gqpp0RJGwYsRdbyxAssSnJmQeoCG
"""

#classification
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder,StandardScaler

df=pd.read_csv("/content/loan_approval.csv")
df
#Data Preprocessing & EDA
#checking missing values
df.isnull().sum()
#filling null values
# df=df.fillna(df[['loan_id', ' no_of_dependents',
#        ' income_annum', ' loan_amount', ' loan_term', ' cibil_score',
#        ' residential_assets_value', ' commercial_assets_value',
#        ' luxury_assets_value', ' bank_asset_value']],df.mean())

#df=df.dropna()
#Calculating for outliers values
z_score=abs((df-df.mean())/df.std())
df.info()
#removing outliers from the data
df=df[z_score<3]
df=df[df[['loan_id', ' no_of_dependents', ' education', ' self_employed',' income_annum', ' loan_amount', ' loan_term', ' cibil_score',' residential_assets_value', ' commercial_assets_value',' luxury_assets_value',' bank_asset_value', ' loan_status']]!=np.NaN]
df.info()
#Encoding the Categorical values
encoder=LabelEncoder()
df['education']=encoder.fit_transform(df['education'])
df['self_employed']=encoder.fit_transform(df['self_employed'])
#featuring the data
X=df1[['loan_id',' no_of_dependents',' education',' self_employed',' income_annum',' loan_amount',' loan_term',' cibil_score',' residential_assets_value',' commercial_assets_value',' luxury_assets_value',' bank_asset_value']]
Y=df1[' loan_status']
#Splitting the data
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3)
#model Training and testing
Model=DecisionTreeClassifier()
Model.fit(x_train,y_train)
y_pred=Model.predict(x_test,y_test)
report=classification_report(y_test,y_pred)
print(report)

df=pd.read_csv("/content/loan_approval.csv")
df

df.isnull().sum()

df1=df
df1[' education']=encoder.fit_transform(df1[' education'])
df1[' self_employed']=encoder.fit_transform(df1[' self_employed'])
X=df1[['loan_id',' no_of_dependents',' education',' self_employed',' income_annum',' loan_amount',' loan_term',' cibil_score',' residential_assets_value',' commercial_assets_value',' luxury_assets_value',' bank_asset_value']]
Y=df1[' loan_status']
#Splitting the data
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3)
#model Training and testing
Model=DecisionTreeClassifier()
Model.fit(x_train,y_train)
y_pred=Model.predict(x_test)
report=classification_report(y_test,y_pred)
print(report)

#therefore this is my final model for loan approval

df.columns

df=df[df[['loan_id', ' no_of_dependents', ' education', ' self_employed',' income_annum', ' loan_amount', ' loan_term', ' cibil_score',' residential_assets_value', ' commercial_assets_value',' luxury_assets_value',' bank_asset_value', ' loan_status']]!=np.NaN]
df