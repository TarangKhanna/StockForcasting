# sentiment analysis on tweets for AAPL
# TODO-get more tweets 
# TODO-tweets from reliable accounts
# TODO-take into account retweets,likes,time,followers
# analyze google searches to predict stock market
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
	
	all_tweets = get_tweets(stock)
	tweets = pd.DataFrame()
	analysis_list = []
	polarity_list = []
	subjectivity_list = []
	tweet_text = []
	for tweet in all_tweets:
		tweet_text.append(tweet.text.encode("utf-8"))
		analysis = TextBlob(tweet.text)
		# prints-Sentiment(polarity=0.0, subjectivity=0.0), polarity is how positive or negative, subjectivity is if opinion or fact
		# analysis_list.append('polarity:' + str(analysis.se 1ntiment.polarity) + ' subjectivity:' + str(analysis.sentiment.subjectivity))
		polarity_list.append(str(analysis.sentiment.polarity))
		subjectivity_list.append(str(analysis.sentiment.subjectivity))

	tweets['text'] = np.array(tweet_text)
	# tweets['analysis'] = np.array(analysis_list)
	tweets['polarity'] = np.array(polarity_list)
	tweets['subjectivity'] = np.array(subjectivity_list)
	tweets = tweets.sort_values(by=['subjectivity'], ascending=0)
	print tweets
	tweets.to_csv('%s.csv' % stock)
	

def get_tweets(stock):
	alltweets = []  
	public_tweets = api.search(stock)
	alltweets.extend(public_tweets)
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(public_tweets) > 0:
	    print "getting tweets before %s" % (oldest)
	    
	    #all subsiquent requests use the max_id param to prevent duplicates
	    public_tweets = api.search(stock,count=200,max_id=oldest)
	    
	    #save most recent tweets
	    alltweets.extend(public_tweets)
	    
	    #update the id of the oldest tweet less one
	    oldest = alltweets[-1].id - 1
	    
	    print "...%s tweets downloaded so far" % (len(alltweets))

	    if len(alltweets) > 1000:
	    	break

	#transform the tweepy tweets into a 2D array that will populate the csv 
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in public_tweets]
	print outtweets
	return alltweets

analyze_stock('$AAPL')
analyze_stock('$GOOGL')

