# currently it is linear regression, we need some error to measure accuracy 

# clf = joblib.load('filename.pkl')  # load classifier 

# given ['Adj. Open','Adj. Close', 'Adj. Volume','Adj. High', 'Adj. Low'], we can predict 1% into future 

# In our case 'adj close' is clearly correlated to 'label' (we can verify this by doing a df.corr() before all the transforms).
# label buy or sell based on increasing future then do f1 score test-recall and precision
# ~ 77% accurate, increase 

from __future__ import division # preventing division issue in 2.7
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
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
import time

# ensemble learning
# good results with 1000 data rows and linear svm kernel
# can make more fast using csv instead of calling from quandl
# import accelerate

def predictML(stocksDf, useLinear, symbol):
	stocksDf = stocksDf.dropna(how='any')
	print stocksDf

	X = np.array(stocksDf.drop(['Decision'],1))
	X = preprocessing.scale(X)
	predict_index = len(X)-2
	predict_value = X[predict_index-20:]
	X = X[:predict_index-2]
	print(X.shape)
	
	# X_lately = X[-forecast_out:]
	# X = X[:-forecast_out:]

	y = np.array(stocksDf['Decision']) # y is the 1% forcast 
	y = y[:predict_index-2] # to keep consistent
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.5) # 20% training data, 80% testing 

	if useLinear:
		# use KNN or other binary classifiers
		clf = LinearRegression(n_jobs=-1)
		print("Crunching...")

		clf.fit(X_train,y_train)
		# clf.fit(X,y) # all data till now
		file_name = 'KNNClf_%s.pkl' %symbol
		joblib.dump(clf, file_name) # save the classifier to file

		# clf = joblib.load('LinearRegressionClf.pkl')
		# print clf
		accuracy = clf.score(X_test,y_test) # test on data not used for training, is around 95%
		print(accuracy)
		print clf.predict(predict_value) # give array of last 10 days to get 1% into each values future
		# print clf.predict() # predict into 1% future given todays ['Adj. Open','Adj. Close','S&P Open', 'Adj. Volume','Adj. High', 'Adj. Low']
		# y_true = y_test
		# y_pred = clf.predict(X_test)
		# print f1_score(y_true, y_pred, average='macro')  
	else:
		X = np.array(stocksDf.drop(['Decision'],1))
		X = preprocessing.scale(X)
		y = np.array(stocksDf['Decision']) # y is the 1% forcast 
		# y = y[:predict_index-2] # to keep consistent
		X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2) # 20% training data, 80% testing 
		clf = RandomForestClassifier(min_samples_leaf=2, n_estimators=100)
		print("Crunching...")
		# clf.fit(X_train,y_train)
		clf.fit(X_train,y_train) # all data till now
		file_name = 'RFClf_%s.pkl' %symbol
		joblib.dump(clf, file_name) # save the classifier to file

		# clf = joblib.load('LinearRegressionClf.pkl')
		# print clf
		accuracy = clf.score(X_test,y_test) # test on data not used for training, is around 95%
		
		print(accuracy)
		print clf.predict(predict_value) # give array of last 10 days to get 1% into each values future
		# print clf.predict() # predict into 1% future given todays ['Adj. Open','Adj. Close','S&P Open', 'Adj. Volume','Adj. High', 'Adj. Low']
		# f1 score
		# y_true = y_test
		# y_pred = clf.predict(X_test)
		# print f1_score(y_true, y_pred, average='binary') 

def predictMLSaved(stocksDf, symbol):
	# stocksDf = stocksDf.drop(['Decision'], axis=1)

	predict_index = 14
	stocksDf = stocksDf.dropna(how='any')
	X = np.array(stocksDf)
	# use same preprocessing scale used while training
	# predicted_df = pd.DataFrame(clf.predict(to_predict), columns=['Predicted_Winner'])
	# predicted_df.to_csv('predictions.csv', encoding='utf-8')
	print len(stocksDf['Adj. Close'].tail(predict_index))
	predicted_df = pd.DataFrame()
	predicted_df['to_predict'] = stocksDf['Adj. Close'].tail(predict_index)
	predicted_df = predicted_df.reset_index(drop=True)
	print stocksDf['Adj. Close'].tail(predict_index)
	X = preprocessing.scale(X)
	
	predict_values = X[len(X)-predict_index:] # future for last 14 dates

	print("Loading Classifier...")

	file_name = 'RFClf_%s.pkl' %symbol
	clf = joblib.load(file_name)
	# graph prediction and show dates of prediction
	# print clf.predict(predict_values) # give array of last 10 days to get 1% into each values future
	# predicted_df['Predicted'] = pd.DataFrame(clf.predict(predict_values))
	temp_df = pd.DataFrame(clf.predict(predict_values), columns=['Predicted'])
	# plot(stocksDf['Adj. Close'], "AAPL", "Date", "Prices")
	frames = [predicted_df, temp_df]
	result = pd.concat(frames, axis=1)
	print result

def dailyReturn(data):
	# make chart
	# did price go up or down on a particular day
	daily_returns = data.copy()
	daily_returns = (data/data.shift(1)) - 1
	daily_returns.ix[0] = 0  # set daily return for row 0 to 0
	# plot(daily_returns, "Stock Analysis" ,"Date", "Daily Returns")
	# print daily_returns
 	return daily_returns

def plot(data_frame, title_label, x_label, y_label):
	ax = data_frame.plot(title=title_label)
	ax.set_xlabel(x_label)
	ax.set_ylabel(y_label)
	pylab.show()

# download and clean symbol data
def download_data(symbol):
	# use current date
	till_date = time.strftime("%Y-%m-%d")
	print till_date
	to_download = 'Wiki/%s' %symbol
	df = quandl.get(to_download, authtoken="zzYfW2Zd_3J3Gt2o3Nz6", start_date="2010-12-12", end_date=till_date)

	sp500_df_all = quandl.get("YAHOO/INDEX_GSPC", authtoken="zzYfW2Zd_3J3Gt2o3Nz6", start_date="2010-12-12", end_date=till_date)
	df = df[['Adj. Open','Adj. Close', 'Adj. Volume','Adj. High', 'Adj. Low']]
	print sp500_df_all
	sp500_df = sp500_df_all[['Open', 'Adjusted Close']]

	frames = [df, sp500_df]
	df = pd.concat(frames, axis=1) # concatenate column-wise, remove Nan Data
	df.columns = ['Adj. Open','Adj. Close','S&P Open','Adj. High', 'Adj. Low', 'Adj. Volume',  'S&P Adj. Close']
	# add moving average
	df = df.dropna(how='any')
	print df
	file_name = 'data/%s_training.csv' %symbol
	df.to_csv(file_name, encoding='utf-8')

if __name__ == "__main__":
	symbols = ['AAPL', 'GOOGL', 'GLD']
	symbol = 'AAPL'
	download_data(symbol)

	# max
	# print df['Adj. Close'].max()''

	# compare with S&P 
	

	# only when need new classifier

	# use trained classifier

	# read_df = pd.read_csv('data/AAPL_training.csv', index_col = "Date")
	file_name = 'data/%s_training.csv' %symbol
	read_df = pd.read_csv(file_name, index_col = "Date")

	read_df['Daily Returns'] = dailyReturn(read_df['Adj. Close'])
	# dailyReturn(sp500_df_all['Close'])
	print read_df
	# add decision column
	# if ['future'] > ['Adj. Close'] then ['Decision'] = Buy
	
	# forecast_out = int(math.ceil(0.01*len(read_df))) # train 1% into future
	forecast_out = 14
	print 'predicting into: ' + str(forecast_out)
	to_predict_df = read_df.copy(deep=True)

	read_df['Future'] = read_df['Adj. Close'].shift(-forecast_out)

	read_df = read_df.dropna(how='any')

	decisions = []
	for index, row in read_df.iterrows():
		# floating point comparison careful
		# if 2 % increase in two weeks, then classify as a buy
		# another method is to get historical buy-sell ratings
		if (round(row['Future'],3) > round((1.03*row['Adj. Close']),3)):
			decisions.append('Buy')
		elif (round(row['Future'],3) < ((1.03*row['Adj. Close']),3)):
			decisions.append('Sell')
		else:
			decisions.append('Hold')

	read_df['Decision'] = decisions
	print read_df['Decision'].value_counts()

	read_df = read_df.drop(['Future'], axis=1)
	# print read_df
	predictML(read_df, False, symbol)
	predictMLSaved(to_predict_df, symbol)



