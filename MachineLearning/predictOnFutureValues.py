# currently it is linear regression, we need some error to measure accuracy 

# clf = joblib.load('filename.pkl')  # load classifier 

# given ['Adj. Open','Adj. Close', 'Adj. Volume','Adj. High', 'Adj. Low'], we can predict 1% into future 

# In our case 'adj close' is clearly correlated to 'label' (we can verify this by doing a df.corr() before all the transforms).
from __future__ import division 
# if using python 2.7, need this to prevent division issue in 2.7
import pandas as pd 
import quandl
import math
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pylab


# use ensemble for faster classification

from sklearn.ensemble import RandomForestClassifier

# ensemble learning
# good results with 1000 data rows and linear svm kernel
# can make more fast using csv instead of calling from quandl
# import accelerate

def predictML(stocksDf, useLinear):
	forecast_out = int(math.ceil(0.01*len(stocksDf))) # train 1% into future
	print(forecast_out)

	stocksDf['future'] = stocksDf['Adj. Close'].shift(-forecast_out)
	# stocksDf['future'] = stocksDf['future'].dropna(how='any') 
	# print(stocksDf)

	print stocksDf
	# stocksDf = stocksDf.dropna(inplace=True) # drop na 
	stocksDf = stocksDf.dropna(how='any')
	print stocksDf
	
	X = np.array(stocksDf.drop(['future'],1))
	X = preprocessing.scale(X)
	predict_index = len(X)-2
	predict_value = X[predict_index-20:]
	X = X[:predict_index-2]
	print(X.shape)
	
	# X_lately = X[-forecast_out:]
	# X = X[:-forecast_out:]

	y = np.array(stocksDf['future']) # y is the 1% forcast 
	y = y[:predict_index-2] # to keep consistent
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2) # 20% training data, 80% testing 

	if useLinear:
		clf = LinearRegression(n_jobs=-1)
		print("Crunching...")

		# clf.fit(X_train,y_train)
		clf.fit(X_train,y_train) # all data till now
		# joblib.dump(clf, 'LinearRegressionClf.pkl') # save the classifier to file

		# clf = joblib.load('LinearRegressionClf.pkl')
		# print clf
		accuracy = clf.score(X_test,y_test) # test on data not used for training, is around 95%
		print(accuracy)
		print clf.predict(predict_value) # give array of last 10 days to get 1% into each values future
		# print clf.predict() # predict into 1% future given todays ['Adj. Open','Adj. Close','S&P Open', 'Adj. Volume','Adj. High', 'Adj. Low']
	else:
		X = np.array(stocksDf.drop(['future'],1))
		X = preprocessing.scale(X)
		y = stocksDf['future'] # y is the 1% forcast 
		# y = y[:predict_index-2] # to keep consistent
		X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2) # 20% training data, 80% testing 
		y_train = np.asarray(stocksDf['future'], dtype="float64")
		clf = RandomForestClassifier(min_samples_leaf=2, n_estimators=50)
		print("Crunching...")
		# clf.fit(X_train,y_train)
		clf.fit(X_train,y_train) # all data till now
		# joblib.dump(clf, 'LinearRegressionClf.pkl') # save the classifier to file

		# clf = joblib.load('LinearRegressionClf.pkl')
		# print clf
		accuracy = clf.score(X_test,y_test) # test on data not used for training, is around 95%
		print(accuracy)
		print clf.predict(predict_value) # give array of last 10 days to get 1% into each values future
		# print clf.predict() # predict into 1% future given todays ['Adj. Open','Adj. Close','S&P Open', 'Adj. Volume','Adj. High', 'Adj. Low']
	

def predictMLSaved(stocksDf):
	stocksDf = stocksDf.dropna(how='any')
	X = np.array(stocksDf)
	# use same preprocessing scale used while training
	print stocksDf.tail(10)
	X = preprocessing.scale(X)
	predict_index = len(X)-1
	predict_values = X[predict_index-20:] # future for last 20 dates

	clf = LinearRegression(n_jobs=-1)

	print("Loading Classifier...")

	clf = joblib.load('LinearRegressionClf.pkl')
	# graph prediction and show dates of prediction
	print clf.predict(predict_values) # give array of last 10 days to get 1% into each values future
	
	# plot(stocksDf['Adj. Close'], "AAPL", "Date", "Prices")

def dailyReturn(data):
	# make chart
	# did price go up or down on a particular day
	daily_returns = data.copy()
	daily_returns = (data/data.shift(1)) - 1
	daily_returns.ix[0] = 0  # set daily return for row 0 to 0
	plot(daily_returns, "Stock Analysis" ,"Date", "Daily Returns")
	# print daily_returns
 	return daily_returns

def plot(data_frame, title_label, x_label, y_label):
	ax = data_frame.plot(title=title_label)
	ax.set_xlabel(x_label)
	ax.set_ylabel(y_label)
	pylab.show()

if __name__ == "__main__":
	symbols = ['AAPL', 'GOOGL', 'GLD']

	# df = quandl.get('Wiki/AAPL', authtoken="zzYfW2Zd_3J3Gt2o3Nz6", start_date="2010-12-12", end_date="2016-10-14")

	# sp500_df_all = quandl.get("YAHOO/INDEX_GSPC", authtoken="zzYfW2Zd_3J3Gt2o3Nz6", start_date="2010-12-12", end_date="2016-10-14")
	# df = df[['Adj. Open','Adj. Close', 'Adj. Volume','Adj. High', 'Adj. Low']]
	# sp500_df = sp500_df_all['Open']

	# frames = [df, sp500_df]
	# df = pd.concat(frames, axis=1) # concatenate column-wise, remove Nan Data
	# df.columns = ['Adj. Open','Adj. Close','S&P Open', 'Adj. Volume','Adj. High', 'Adj. Low']

	# max
	# print df['Adj. Close'].max()''

	# compare with S&P 
	# dailyReturn(df['Adj. Close'])
	# dailyReturn(sp500_df_all['Close'])

	# only when need new classifier
	# predictML(df, False)

	# use trained classifier

	# df = df.dropna(how='any')
	# print df
	# df.to_csv('data/training.csv', encoding='utf-8')

	read_df = pd.read_csv('data/training.csv', index_col = "Date")
	# print read_df
	# predictMLSaved(read_df)
	predictML(read_df, True)
