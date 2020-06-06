#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 23:55:19 2017

@author: shamim
"""

import pandas as pd
#import numpy as np
#import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv('features/features.csv',header=None)
#df=pd.read_csv('multiplied_training_data.csv',header=None)
X = df.loc[0:1350,0:59]
y = df.loc[0:1350,60]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

#df1 = pd.DataFrame(X_train)
#df2 = pd.DataFrame(X_test)
#df3 = pd.DataFrame(y_train)
#df4 = pd.DataFrame(y_test)

#df1.to_csv('X_train.csv',header=False,index=False)
#df2.to_csv('X_test.csv',header=False,index=False)
#df3.to_csv('y_train.csv',header=False,index=False)
#df4.to_csv('y_test.csv',header=False,index=False)
#filename = 'MyRandomForest.sav'

clf = RandomForestClassifier(n_estimators=100, max_depth=100)
clf.fit(X_train,y_train)
#pickle.dump(clf, open(filename, 'wb'))
s = clf.score(X_test,y_test)
#
#S = np.array([0.912562867,0.880557961,0.100077821,0.217889075,0.991566262,0.904988428,
#              0.60455277,0.39953125,0.243567329,0.978396156,0.907539987,0.721589533,
#              0.296109069,0.236434283,0.980700942,0.904549194,0.778904352,0.239453125,
#              0.244508721,0.980161549])
#
#res = clf.predict(S.reshape(-1,20))
#print("Predicted class : ",res)
print("Score = ",s*100,"%")

