# Input:
# adjusted open and S
# currently it is linear regression, we need some error to measure accuracy 

# TODO: python logger

# clf = joblib.load('filename.pkl')  # load classifier 
import pandas as pd 
import quandl
import math
import numpy as np
from sklearn import svm
from sklearn.externals import joblib

# use ensemble for faster classification

from sklearn.ensemble import RandomForestClassifier

# ensemble learning
# good results with 1000 data rows and linear svm kernel
# can make more fast using csv instead of calling from quandl
# import accelerate

def PredictML(stocksDf, useSVM):
	print df.shape
	useDataPoints = 3982
	df5 = df[0:useDataPoints]
	print(df5[['Adj. Open','S&P Open', 'Adj. Close']])

	X = np.array(stocksDf[0:useDataPoints][['Adj. Open','S&P Open']]) # stock opening price  
	# print(X)
	Y = (stocksDf[0:useDataPoints]['Adj. Close']).astype(str) # stock closing price 
	if useSVM:
		print "Using SVM Classifier"
		clf = svm.SVC(kernel='linear', C = 1.0) # (kernel='poly',degree=1, C = 1.0)#
		# joblib.dump(clf, 'SVMClf.pkl') # save the classifier to file
	else:
		print "Using Random Forest Classifier"
		clf = RandomForestClassifier(min_samples_leaf=2, n_estimators=50) #(n_estimators=10), min_samples_leaf = 2 seems optimum, the results vary on each run
		# joblib.dump(clf, 'RandomForestClf.pkl') # save the classifier to file
	# X = X.reshape(-1, 1) # for one feature

	

	print("Crunching...")

	clf.fit(X,Y)

	predictIndex = 3983
	print("Prediction for: {}".format(predictIndex))
	df6 = df[predictIndex:predictIndex+1] # normal indexing is giving errors
	predicting = (df6[['Adj. Open','S&P Open']])
	# print(predicting)
	predicted = clf.predict(predicting)[0] # [0] since it is np.array type
	print(predicted)
	# print(type(predicted))
	print("Exact Value:")
	exact_value = stocksDf['Adj. Close'][predictIndex].item() # .type since it is np.float type
	print(exact_value)
	# print(type(exact_value))
	errorInPrediction = ((math.fabs(float(predicted) - float(exact_value)))/float(exact_value)) * 100
	# print(type(errorInPrediction))
	# print(errorInPrediction)
	print('Error in prediction: {0:.2f}%'.format(errorInPrediction))

if __name__ == "__main__":
	df = quandl.get('Wiki/AAPL', authtoken="zzYfW2Zd_3J3Gt2o3Nz6", start_date="2000-12-12", end_date="2016-10-14") # can start from 1990

	sp500_df = quandl.get("YAHOO/INDEX_GSPC", authtoken="zzYfW2Zd_3J3Gt2o3Nz6", start_date="2000-12-12", end_date="2016-10-14")
	df = df[['Adj. Open','Adj. Close']]
	sp500_df = sp500_df['Open']
	# read from csv

	# print(sp500_df)
	# df.append(sp500_df)

	frames = [df, sp500_df]
	df = pd.concat(frames, axis=1) # concatenate column-wise, remove Nan Data
	df.columns = ['Adj. Open','Adj. Close','S&P Open']
	# print(df)

	# save to csv after making the correct data frame

	# print(df.size) # 6062 data points
	# useDataPoints = int(math.ceil(0.8*df.size))
	# print(useDataPoints)
	# print(df[0:3000])
	# print(df[3002:6060])

	df.dropna() #drop all rows that have any NaN values

	file_name = "stocksData.txt"
	# df.to_csv(file_name, sep='\t', encoding='utf-8')

	# df_predict = df[3002]

	PredictML(df, False)


	# PredictML(df, True)

	# print(type(predicting))
	# PredictCloseFromOpen(df[0:3000])

	# only a good test for labeled output, not regression
	# X_test = np.array(df[3001:6000]['Adj. Open'])
	# X_test = X_test.reshape(-1, 1) # one feature
	# y_test = (df[3001:6000]['Adj. Close']).astype(str)
	# print(clf.score(X_test, y_test))

	# @vectorize(["void(void)"], target='gpu')