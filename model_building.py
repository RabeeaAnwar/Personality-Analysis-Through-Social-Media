# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 08:57:04 2019

@author: MY
"""

#%%
import pandas as pd


#%%
data=pd.read_csv('traits_essays.csv',encoding='latin1')
data.head()
#%%
#labels=data[['Extraversion','Agreeableness','Conscientiousness','Neuroticism','Openness']]
labels=data.iloc[:,-5:]
tweets=data.iloc[:,1]

#%%
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer()
X=vectorizer.fit_transform(tweets)
#print(X)
y=labels

#%% TFIDF prac
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
     'This is the first document.',
     'This document is the second document.',
     'And this is the third one.',
     'Is this the first document?',
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X.shape)

#%%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#%% apply xgboost
import xgboost as xgb
xgb_regr=xgb.XGBRegressor(max_depth=3,n_estimators=300,learning_rate=0.05).fit(X_train,y_train)
predictions=xgb_regr.predict(X_test)

#%% apply randomforest
from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor(n_estimators=1000,random_state=42)
rf.fit(X_train,y_train)
pred=rf.predict(X_test)
#%%
print(44)

#%% linear regression
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,y_train)
pred=lr.predict(X_test)
#print(lr.score(X_test,y_test))

#%% check accuracy
from sklearn.metrics import r2_score
print(r2_score(y_test,pred))

#%% plot on graph
import matplotlib.pyplot as plt
plt.plot(range(len(y_test)),y_test)
plt.show()
print()
plt.plot(range(len(pred)),pred)
plt.show()

#%%checking NN
from keras.models import Sequential
from keras.layers import Dense
from keras import losses
from keras import activations

model=Sequential()

#%%
model.add(Dense(X.shape[1],activation=activations.relu,input_shape=(X.shape[1],)))
model.add(Dense(50,activation=activations.relu))
model.add(Dense(50,activation=activations.relu))
model.add(Dense(5,activation=activations.relu))

model.compile(optimizer='adam',loss=losses.mean_absolute_error)

model.fit(X_train,y_train,verbose=2,epochs=100)
nn_pred=model.predict(X_test)
print(r2_score(y_test,nn_pred))

#%%SVM
from sklearn.svm import SVR
reg=SVR()
reg.fit(X_train,y_train)
svm_pred=reg.predict(X_test)
print(r2_score(y_test,svm_pred))

#%%
from sklearn.tree import DecisionTreeRegressor
reg=DecisionTreeRegressor()
reg.fit(X_train,y_train)
tree_pred=reg.predict(X_test)
print(r2_score(y_test,tree_pred))





