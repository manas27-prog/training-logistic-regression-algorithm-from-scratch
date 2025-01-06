# -*- coding: utf-8 -*-
"""training logistic regression algorithm from scratch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1l7VDymcjlqZP_x-l5cYMxpBsDkh6TLsS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv('/content/heart_attack_youngsters_india.csv')

df.head()

print(df.columns)
columns_to_drop = [col for col in ["Region", "Urban/Rural", "Screen Time (hrs/day)", "Alcohol Consumption","Exercise Induced Angina"] if col in df.columns]
df.drop(columns=columns_to_drop, inplace=True)

df.head()

df.shape

df.isnull().sum()

categorical_features = ['Gender', 'SES', 'Smoking Status', 'Diet Type', 'Physical Activity Level', 'Family History of Heart Disease', 'Diabetes', 'Hypertension', 'Stress Level', 'ECG Results', 'Chest Pain Type','Blood Pressure (systolic/diastolic mmHg)']
for feature in categorical_features:
    label_encoder = LabelEncoder()
    df[feature] = label_encoder.fit_transform(df[feature])

df['Heart Attack Likelihood'] = df['Heart Attack Likelihood'].map({'No': 0, 'Yes': 1})

X = df.drop('Heart Attack Likelihood', axis=1)
y = df['Heart Attack Likelihood']

X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=40)

"""##Logistic Regression from scratch"""

class Logistic_regression:
    def __init__(self):
        self.parameters = {}

    def forward_propagation(self, X_train):
        predictions = np.dot(X_train, self.parameters['w']) + self.parameters['b']
        return predictions

    def sigmoid(self, predictions):
        return 1 / (1 + np.exp(-predictions))

    def compute_cost(self, A, y_train):
        m = y_train.shape[0]
        y_train = y_train.astype(np.float64)
        A = A.astype(np.float64)
        if A.ndim > 1:
            A = A.flatten()
        cost = -(1 / m) * np.sum(y_train * np.log(A) + (1 - y_train) * np.log(1 - A))
        return cost

    def backward_propagation(self, X_train, A, y_train):
        m = y_train.shape[0]
        if A.ndim > 1:
            A = A.flatten()
        dw = (1 / m) * np.dot(X_train.T, (A - y_train))
        db = (1 / m) * np.sum(A - y_train)
        return {"dw": dw, "db": db}

    def update_parameters(self, derivates, lr):
        self.parameters['m'] = self.parameters['m'] - lr * derivates['m']
        self.parameters['c'] = self.parameters['c'] - lr * derivates['c']

    def initialize_parameters(self, X_train):
        self.parameters['w'] = np.zeros((X_train.shape[1], 1))
        self.parameters['b'] = 0
        self.loss = []
        return self.parameters

    def fit(self, X_train, y_train, num_iterations=1000, lr=0.01):
        self.initialize_parameters(X_train)
        for i in range(num_iterations):
            predictions = self.forward_propagation(X_train)
            A = self.sigmoid(predictions)
            cost = self.compute_cost(A, y_train)
            derivates = self.backward_propagation(X_train, A, y_train)
            if i % 100 == 0:
                print(f"Iteration {i}: Cost = {cost}")

    def predict(self, X_test):
        Z = np.dot(X_test, self.parameters['w']) + self.parameters['b']
        A = self.sigmoid(Z)
        return np.where(A > 0.5, 1, 0)

"""y=mx+c

sigmoid=1/1+e^-predictions

find error cost =-1/m * sum (ylogp(p(x)) + (1-y)log(1-p(x))
"""

model1=Logistic_regression()
model1.fit(X_train,Y_train)

from sklearn.metrics import accuracy_score
y_pred=model.predict(X_test)
accuracy=accuracy_score(Y_test,y_pred)
print(f"Accuracy:{accuracy}")

"""##Model"""

model=LogisticRegression()
model.fit(X_train,Y_train)

model.predict(X_test)

from sklearn.metrics import accuracy_score
y_pred=model.predict(X_test)
accuracy=accuracy_score(Y_test,y_pred)
print(f"Accuracy:{accuracy}")