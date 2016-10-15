# sentiment analysis on tweets for AAPL
# TODO-get more tweets 
# TODO-tweets from reliable accounts
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt
import csv 
from textblob import TextBlob
import numpy as np

#Variables that contains the user credentials to access Twitter API 
access_token = "301847288-lWXEQAwNc7kvyIF4E6w3TCzj7FfWYyUs2FKXbkcR"
access_token_secret = "dXv1ktTNVsHVHsx7AUyVilLOx3tEWPc0Ffi8BvSh9VN10"
consumer_key = "MyrxJJIAAbIupjvNbqyUTzJOZ"
consumer_secret = "ZBZrMl7jEv1DGt76hCV60K7j8Z8uDx8K710cO1w6SBelNVSeqD"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def analyze_stock(stock):
	public_tweets = api.search(stock)
	tweets = pd.DataFrame()
	analysis_list = []
	polarity_list = []
	subjectivity_list = []
	tweet_text = []
	for tweet in public_tweets:
		tweet_text.append(tweet.text.encode("utf-8"))
		analysis = TextBlob(tweet.text)
		# prints-Sentiment(polarity=0.0, subjectivity=0.0), polarity is how positive or negative, subjectivity is if opinion or fact
		# analysis_list.append('polarity:' + str(analysis.sentiment.polarity) + ' subjectivity:' + str(analysis.sentiment.subjectivity))
		polarity_list.append(str(analysis.sentiment.polarity))
		subjectivity_list.append(str(analysis.sentiment.subjectivity))

	tweets['text'] = np.array(tweet_text)
	# tweets['analysis'] = np.array(analysis_list)
	tweets['polarity'] = np.array(polarity_list)
	tweets['subjectivity'] = np.array(subjectivity_list)
	tweets = tweets.sort_values(by=['subjectivity'], ascending=0)
	print tweets
	tweets.to_csv('%s.csv' % stock)

analyze_stock('$AAPL')
analyze_stock('$GOOGL')

