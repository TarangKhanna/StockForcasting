# predicting ajusted close using adjusted open price

import pandas as pd 
import quandl
import math
import numpy as np
from sklearn import svm

df = quandl.get('Wiki/GOOGL', authtoken="") # removed auth token for GitHub, TODO, find a better way
df = df[['Adj. Open','Adj. Close']]

# print(df.size) # 6062 data points
useDataPoints = int(math.ceil(0.8*df.size))
print(useDataPoints)
# print(df[0:3000])
# print(df[3002:6060])
predicting = (df['Adj. Open'][3002])
print(predicting)
# print(type(predicting))
# PredictCloseFromOpen(df[0:3000])

X = np.array(df[0:3000]['Adj. Open']) # stock opening price  
Y = (df[0:3000]['Adj. Close']).astype(str) # stock closing price 
clf = svm.SVC(kernel='linear', C = 1.0) # (kernel='poly',degree=1, C = 1.0)#
X = X.reshape(-1, 1) # one feature so we need to reshape

clf.fit(X,Y)
print("Prediction:")
print(clf.predict(predicting))
print("Real:")
print(df['Adj. Close'][3002])

X_test = np.array(df[3001:6000]['Adj. Open'])
y_test = (df[3001:6000]['Adj. Close']).astype(str) # label needs to be a string
print(clf.score()) # how well is it predicting