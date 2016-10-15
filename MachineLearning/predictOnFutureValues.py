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


# use ensemble for faster classification

from sklearn.ensemble import RandomForestClassifier

# ensemble learning
# good results with 1000 data rows and linear svm kernel
# can make more fast using csv instead of calling from quandl
# import accelerate

def PredictML(stocksDf, useSVM):
	forecast_out = int(math.ceil(0.01*len(stocksDf))) # train 1% into future
	print(forecast_out)

	stocksDf['future'] = stocksDf['Adj. Close'].shift(-forecast_out)
	# stocksDf['future'] = stocksDf['future'].dropna(how='any') 
	# print(stocksDf)

	print stocksDf
	# stocksDf = stocksDf.dropna(inplace=True) # drop na 
	stocksDf = stocksDf.dropna(how='any')
	print stocksDf

	stocksDf.to_csv('training.txt', sep='\t', encoding='utf-8')
	
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
	print(X)
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2) # 20% training data, 80% testing 

	print(X.shape)
	print(y.shape)

	clf = LinearRegression(n_jobs=-1)

	print("Crunching...")

	# clf.fit(X_train,y_train)
	clf.fit(X,y) # all data till now
	# accuracy = clf.score(X_test,y_test) # test on data not used for training, is around 95%
	# print(accuracy)
	print clf.predict(predict_value) # give array of last 10 days to get 1% into each values future
	# print clf.predict() # predict into 1% future given todays ['Adj. Open','Adj. Close','S&P Open', 'Adj. Volume','Adj. High', 'Adj. Low']

if __name__ == "__main__":
	df = quandl.get('Wiki/AAPL', authtoken="zzYfW2Zd_3J3Gt2o3Nz6", start_date="2010-12-12", end_date="2016-10-14")

	sp500_df = quandl.get("YAHOO/INDEX_GSPC", authtoken="zzYfW2Zd_3J3Gt2o3Nz6", start_date="2010-12-12", end_date="2016-10-14")
	df = df[['Adj. Open','Adj. Close', 'Adj. Volume','Adj. High', 'Adj. Low']]
	sp500_df = sp500_df['Open']

	frames = [df, sp500_df]
	df = pd.concat(frames, axis=1) # concatenate column-wise, remove Nan Data
	df.columns = ['Adj. Open','Adj. Close','S&P Open', 'Adj. Volume','Adj. High', 'Adj. Low']
	# print(df)

	# save to csv after making the correct data frame

	# df.fillna(-99999, inplace=True) 

	file_name = "stocksData.txt"
	# df.to_csv(file_name, sep='\t', encoding='utf-8')


	PredictML(df, False)