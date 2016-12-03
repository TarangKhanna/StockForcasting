# currently it is linear regression, we need some error to measure accuracy 

# clf = joblib.load('filename.pkl')  # load classifier 

# given ['Adj. Open','Adj. Close', 'Adj. Volume','Adj. High', 'Adj. Low'], we can predict 1% into future 

# In our case 'adj close' is clearly correlated to 'label' (we can verify this by doing a df.corr() before all the transforms).
# label buy or sell based on increasing future then do f1 score test-recall and precision
# ~ 77% accurate, increase 
# wolframalpha for more data
# find pre market movers
# use xgboost
# arc 

# mean reversion for long term prediction
from __future__ import division # preventing division issue in 2.7
import pandas as pd 
import quandl
import math
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pylab
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
import time
import os
# for tuning hyper parameters we use grid search
from sklearn.grid_search import GridSearchCV   #Perforing grid search
import xgboost

class predictStocks:

	def __init__(self):
		pass

	def predictML(self,stocksDf, useRegression, symbol):
		stocksDf = stocksDf.dropna(how='any')
		# print stocksDf
		# X = np.array()
		if useRegression:
			X = np.array(stocksDf.drop(['Future'],1))
		else:
			X = np.array(stocksDf.drop(['Decision'],1))

		X = preprocessing.scale(X)
		predict_index = len(X)-2
		predict_value = X[predict_index-20:]
		# X = X[:predict_index-2]
		# print(X.shape)

		# X_lately = X[-forecast_out:]
		# X = X[:-forecast_out:]
		# y = np.array()

		if useRegression:
			y = np.array(stocksDf['Future']) # y is set forecast out
		else:
			y = np.array(stocksDf['Decision']) 

		# lb = preprocessing.LabelBinarizer(neg_label=0, pos_label=1, sparse_output=False)
		# # lb.fit([0,1])
		# y = lb.fit_transform(y)

		# le_decision = preprocessing.LabelEncoder()

		#to convert into numbers

		# y = le_decision.fit_transform(y)

		#to convert back

		# y = le_decision.inverse_transform(y)

		# y = y[:predict_index-2] # to keep consistent
		X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5) # 50% training data, 50% testing 
		
		# print y

		best_clf = RandomForestClassifier(min_samples_leaf=2, n_estimators=100)
		# best_clf = KNeighborsClassifier(n_neighbors=10, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None, n_jobs=-1)
		best_accuracy = 0.0
		best_algo = 'RF'

		num_runs = 2
		for _ in xrange(num_runs):
			if useRegression:
				# use KNN or other binary classifiers
				clf = LinearRegression(n_jobs=-1)
				# print("Crunching...")

				clf.fit(X_train,y_train)
				# clf.fit(X,y) # all data till now
				file_name = 'LinearRegressionClf_%s.pkl' %symbol
				joblib.dump(clf, file_name) # save the classifier to file

				# clf = joblib.load('LinearRegressionClf.pkl')
				# print clf
				accuracy = clf.score(X_test,y_test) # test on data not used for training, is around 95%
				# print(accuracy)
				# print clf.predict(predict_value) # give array of last 10 days to get 1% into each values future
				# print clf.predict() # predict into 1% future given todays ['Adj. Open','Adj. Close','S&P Open', 'Adj. Volume','Adj. High', 'Adj. Low']
				# y_true = y_test
				# y_pred = clf.predict(X_test)
				# print f1_score(y_true, y_pred, average='macro') 
				if accuracy > best_accuracy:
					best_clf = clf
					best_accuracy = accuracy
					best_algo = 'Linear' 
			else:
				X = np.array(stocksDf.drop(['Decision'],1))
				X = preprocessing.scale(X)
				y = np.array(stocksDf['Decision']) # y is the 1% forcast 
				# y = y[:predict_index-2] # to keep consistent

				# to convert into numbers
				# y = le_decision.fit_transform(y)
				X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2) # 20% training data, 80% testing 
				# clf = RandomForestClassifier(min_samples_leaf=2, n_estimators=100)

				# best is {'max_depth': 8, 'min_child_weight': 2}

				clf = xgboost.XGBClassifier(
											learning_rate =0.1,
											n_estimators=1000,
											max_depth=8,
											min_child_weight=2,
											gamma=0,
											subsample=0.8,
											colsample_bytree=0.8,
											objective= 'binary:logistic',
											nthread=4,
											seed=27)

				# print("Crunching...")
				# clf.fit(X_train,y_train)
				clf.fit(X_train,y_train) # all data till now
				
				# clf = joblib.load('LinearRegressionClf.pkl')
				# print clf
				accuracy = clf.score(X_test,y_test) # test on data not used for training, is around 95%
				
				# print(accuracy)
				# print clf.predict(predict_value) # give array of last 10 days to get 1% into each values future
				# print clf.predict() # predict into 1% future given todays ['Adj. Open','Adj. Close','S&P Open', 'Adj. Volume','Adj. High', 'Adj. Low']
				# f1 score
				# y_true = y_test
				# y_pred = clf.predict(X_test)
				# print f1_score(y_true, y_pred, average='binary') 
				if accuracy > best_accuracy:
					best_clf = clf
					best_accuracy = accuracy
					best_algo = 'XG'
		file_name = 'XGClf_%s.pkl' %symbol
		joblib.dump(best_clf, file_name) # save the classifier to file
		# print 'best accuracy:'
		# print best_accuracy

	def modelOptimization(self):	
		# param_test1 = {
		# 	'max_depth':range(3,10,2),
		# 	'min_child_weight':range(1,6,2)
		# }
		# gsearch1 = GridSearchCV(estimator = xgboost.XGBClassifier( learning_rate =0.1, n_estimators=140, max_depth=5,
		# 	min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8,
		# 	objective= 'binary:logistic', nthread=4, scale_pos_weight=1, seed=27), 
		# 	param_grid = param_test1, scoring='roc_auc',n_jobs=4,iid=False, cv=5)
		# gsearch1.fit(X_train,y_train)
		# print gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_	
		# param_test2 = {
		#  'max_depth':[6,7,8],
		#  'min_child_weight':[2,3,4]
		# }
		# gsearch2 = GridSearchCV(estimator = xgboost.XGBClassifier( learning_rate=0.1, n_estimators=140, max_depth=5,
		#  min_child_weight=2, gamma=0, subsample=0.8, colsample_bytree=0.8,
		#  objective= 'binary:logistic', nthread=4, scale_pos_weight=1,seed=27), 
		#  param_grid = param_test2, scoring='roc_auc',n_jobs=4,iid=False, cv=5)
		# gsearch2.fit(X_train,y_train)
		# print gsearch2.grid_scores_, gsearch2.best_params_, gsearch2.best_score_

		# param_test2b = {
		#  'min_child_weight':[2,6,8,10,12]
		# }
		# gsearch2b = GridSearchCV(estimator = xgboost.XGBClassifier( learning_rate=0.1, n_estimators=140, max_depth=4,
		#  min_child_weight=2, gamma=0, subsample=0.8, colsample_bytree=0.8,
		#  objective= 'binary:logistic', nthread=4, scale_pos_weight=1,seed=27), 
		#  param_grid = param_test2b, scoring='roc_auc',n_jobs=4,iid=False, cv=5)
		# gsearch2b.fit(X_train,y_train)	
		# print gsearch2b.grid_scores_, gsearch2b.best_params_, gsearch2b.best_score_
		pass	

	def binaryClassifySaved(self,stocksDf, symbol, predict_index):
		# stocksDf = stocksDf.drop(['Decision'], axis=1)
		# predict_index = 14
		stocksDf = stocksDf.dropna(how='any')
		X = np.array(stocksDf)
		# use same preprocessing scale used while training
		# predicted_df = pd.DataFrame(clf.predict(to_predict), columns=['Predicted_Winner'])
		# predicted_df.to_csv('predictions.csv', encoding='utf-8')
		# print len(stocksDf['Adj. Close'].tail(predict_index))
		predicted_df = pd.DataFrame()
		predicted_df['to_predict'] = stocksDf['Adj. Close'].tail(predict_index)
		predicted_df = predicted_df.reset_index(drop=True)
		# print stocksDf['Adj. Close'].tail(predict_index)
		X = preprocessing.scale(X)
		
		predict_values = X[len(X)-predict_index:] # future for last set dates

		# print("Loading Classifier...")

		file_name = 'XGClf_%s.pkl' %symbol
		clf = joblib.load(file_name)
		# graph prediction and show dates of prediction
		# print clf.predict(predict_values) # give array of last 10 days to get 1% into each values future
		# predicted_df['Predicted'] = pd.DataFrame(clf.predict(predict_values))
		temp_df = pd.DataFrame(clf.predict(predict_values), columns=['Predicted'])
		# plot(stocksDf['Adj. Close'], "AAPL", "Date", "Prices")
		frames = [predicted_df, temp_df]
		result = pd.concat(frames, axis=1)

		le = preprocessing.LabelEncoder()
		# le.classes_ = np.load('Label_Encoder.npy')

		print result
		cur_path = os.getcwd()
		file_name = '/data/%s_predicted_classification.csv' %symbol
		abs_path = cur_path+file_name
		temp_df.to_csv(abs_path, encoding='utf-8')
		result = pd.concat(frames, axis=1)

		# print result
		return abs_path

	# returns file name of the csv with predicted values
	def regressionSaved(self,stocksDf, symbol, predict_index):
		# predict_index = 14
		stocksDf = stocksDf.dropna(how='any')
		X = np.array(stocksDf)
		# print len(stocksDf['Adj. Close'].tail(predict_index))
		predicted_df = pd.DataFrame()
		predicted_df['to_predict'] = stocksDf['Adj. Close'].tail(predict_index)
		predicted_df = predicted_df.reset_index(drop=True)
		# print stocksDf['Adj. Close'].tail(predict_index)
		X = preprocessing.scale(X)
		
		predict_values = X[len(X)-predict_index:] # future for last predict_index dates

		# print("Loading Classifier...")

		file_name = 'LinearRegressionClf_%s.pkl' %symbol
		clf = joblib.load(file_name)
		temp_df = pd.DataFrame(clf.predict(predict_values), columns=['Predicted'])
		frames = [predicted_df, temp_df]
		cur_path = os.getcwd()
		file_name = '/data/%s_predicted_values.csv' %symbol
		abs_path = cur_path+file_name
		predicted_df.to_csv(abs_path, encoding='utf-8')
		result = pd.concat(frames, axis=1)

		# print result
		return abs_path

	def dailyReturn(self,data):
		# make chart
		# did price go up or down on a particular day
		daily_returns = data.copy()
		daily_returns = (data/data.shift(1)) - 1
		daily_returns.ix[0] = 0  # set daily return for row 0 to 0
		# plot(daily_returns, "Stock Analysis" ,"Date", "Daily Returns")
		# print daily_returns
	 	return daily_returns

	def plot(self,data_frame, title_label, x_label, y_label):
		ax = data_frame.plot(title=title_label)
		ax.set_xlabel(x_label)
		ax.set_ylabel(y_label)
		pylab.show()

	# download and clean symbol data
	def download_data(self,symbol):
		# use current date
		till_date = time.strftime("%Y-%m-%d")
		# print 'Till Date:'
		# print till_date

		to_download = 'Wiki/%s' %symbol
		df = quandl.get(to_download, authtoken="zzYfW2Zd_3J3Gt2o3Nz6", start_date="2010-12-12", end_date=till_date)

		sp500_df_all = quandl.get("YAHOO/INDEX_GSPC", authtoken="zzYfW2Zd_3J3Gt2o3Nz6", start_date="2010-12-12", end_date=till_date)
		df = df[['Adj. Open','Adj. Close', 'Adj. Volume','Adj. High', 'Adj. Low']]
		# print sp500_df_all
		sp500_df = sp500_df_all[['Open', 'Adjusted Close']]

		frames = [df, sp500_df]
		df = pd.concat(frames, axis=1) # concatenate column-wise, remove Nan Data
		df.columns = ['Adj. Open','Adj. Close','S&P Open','Adj. High', 'Adj. Low', 'Adj. Volume',  'S&P Adj. Close']
		# add moving average
		df = df.dropna(how='any')
		# print df
		file_name = 'data/%s_training.csv' %symbol
		df.to_csv(file_name, encoding='utf-8')

	def stocksRegression(self, stockName, forecast_out):
		self.download_data(stockName)
		file_name = 'data/%s_training.csv' %stockName
		read_df = pd.read_csv(file_name, index_col = "Date")
		# forecast_out = 14
		# print 'predicting into: ' + str(forecast_out)
		read_df['Daily Returns'] = self.dailyReturn(read_df['Adj. Close'])
		to_predict_df = read_df.copy(deep=True)
		
		read_df['Future'] = read_df['Adj. Close'].shift(-forecast_out)	

		read_df = read_df.dropna(how='any')

		self.predictML(read_df, True, stockName)
		cur_path = os.getcwd()
		file_paths = []
		file_training = '/data/%s_training.csv' %stockName
		abs_path = cur_path+file_training
		file_paths.append(self.regressionSaved(to_predict_df, stockName, forecast_out))
		file_paths.append(abs_path)
		return file_paths

	def stocksClassify(self, stockName, forecast_out):
		self.download_data(stockName)
		file_name = 'data/%s_training.csv' %stockName
		read_df = pd.read_csv(file_name, index_col = "Date")
		# forecast_out = 14
		# print 'predicting into: ' + str(forecast_out)
		read_df['Daily Returns'] = self.dailyReturn(read_df['Adj. Close'])
		to_predict_df = read_df.copy(deep=True)
		
		read_df['Future'] = read_df['Adj. Close'].shift(-forecast_out)

		read_df = read_df.dropna(how='any')

		decisions = []
		pe_ratio = []
		for index, row in read_df.iterrows():
			# floating point comparison careful
			# if 2 % increase in two weeks, then classify as a buy
			# another method is to get historical buy-sell ratings
			if (round(row['Future'],3) > round((1.02*row['Adj. Close']),3)):
				decisions.append('Buy')
			elif (round(row['Future'],3) < ((-1.00*row['Adj. Close']),3)):
				decisions.append('Sell')
			else:
				decisions.append('Hold')
	
		read_df_binary = read_df.copy(deep=True)
		read_df_binary['Decision'] = decisions
		# print read_df_binary['Decision'].value_counts()

		read_df_regression = read_df.copy(deep=True)

		read_df_binary = read_df_binary.drop(['Future'], axis=1)
		# print read_df_binary

		cur_path = os.getcwd()
		file_paths = []
		file_training = '/data/%s_training.csv' %stockName
		abs_path = cur_path+file_training
		file_paths.append(self.binaryClassifySaved(to_predict_df, symbol, forecast_out))
		file_paths.append(abs_path)
		return file_paths

if __name__ == "__main__":
	predict = predictStocks()
	symbol = 'GOOGL'
	print predict.stocksRegression(symbol, 14)

	print predict.stocksClassify(symbol, 14)
	# symbols = ['AAPL', 'GOOGL', 'GLD']
	# symbol = 'GOOGL'
	# download_data(symbol)

	# # max
	# # print df['Adj. Close'].max()''

	# # compare with S&P 
	
	# # only when need new classifier

	# # use trained classifier

	# # read_df = pd.read_csv('data/AAPL_training.csv', index_col = "Date")
	# file_name = 'data/%s_training.csv' %symbol
	# read_df = pd.read_csv(file_name, index_col = "Date")

	# read_df['Daily Returns'] = dailyReturn(read_df['Adj. Close'])
	# dailyReturn(sp500_df_all['Close'])
	# print read_df
	# # add decision column
	# # if ['future'] > ['Adj. Close'] then ['Decision'] = Buy
	
	# # forecast_out = int(math.ceil(0.01*len(read_df))) # train 1% into future
	# forecast_out = 14
	# print 'predicting into: ' + str(forecast_out)
	# to_predict_df = read_df.copy(deep=True)

	# read_df['Future'] = read_df['Adj. Close'].shift(-forecast_out)

	# read_df = read_df.dropna(how='any')

	# decisions = []
	# pe_ratio = []
	# for index, row in read_df.iterrows():
	# 	# floating point comparison careful
	# 	# if 3 % increase in two weeks, then classify as a buy
	# 	# another method is to get historical buy-sell ratings
	# 	if (round(row['Future'],3) > round((1.03*row['Adj. Close']),3)):
	# 		decisions.append('Buy')
	# 	elif (round(row['Future'],3) < ((1.03*row['Adj. Close']),3)):
	# 		decisions.append('Sell')
	# 	else:
	# 		decisions.append('Hold')

	# # read_df['P/E Ratio'] = pe_ratio	
	# read_df_binary = read_df.copy(deep=True)
	# read_df_binary['Decision'] = decisions
	# print read_df_binary['Decision'].value_counts()

	# read_df_regression = read_df.copy(deep=True)

	# read_df_binary = read_df_binary.drop(['Future'], axis=1)
	# # for regression
	# predictML(read_df_regression, True, symbol)
	# regressionSaved(to_predict_df, symbol)
	# for classification 
	# predictML(read_df_binary, False, symbol)
	# binaryClassifySaved(to_predict_df, symbol)


