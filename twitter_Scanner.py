import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt
import csv 

#Variables that contains the user credentials to access Twitter API 
access_token = "301847288-lWXEQAwNc7kvyIF4E6w3TCzj7FfWYyUs2FKXbkcR"
access_token_secret = "dXv1ktTNVsHVHsx7AUyVilLOx3tEWPc0Ffi8BvSh9VN10"
consumer_key = "MyrxJJIAAbIupjvNbqyUTzJOZ"
consumer_secret = "ZBZrMl7jEv1DGt76hCV60K7j8Z8uDx8K710cO1w6SBelNVSeqD"

def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []  
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print "...%s tweets downloaded so far" % (len(alltweets))
    
    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    
    #write the csv  
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
    
    pass

    # put it in a data frame 


class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    # l = StdOutListener()
    # auth = OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # stream = Stream(auth, l)

    # # filter Twitter Streams to capture data by the keywords
    # stream.filter(track=['stocks', '$AAPL', 'higher in pre market', 'hot stocks', 'pre market'])

    get_all_tweets('StockTwits')

    tweets_data_path = 'twitter_data.txt'

    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    print len(tweets_data)

    tweets = pd.DataFrame()

    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
    tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
    tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
    tweets_by_lang = tweets['lang'].value_counts()

    print(tweets)

    # fig, ax = plt.subplots()
    # ax.tick_params(axis='x', labelsize=15)
    # ax.tick_params(axis='y', labelsize=10)
    # ax.set_xlabel('Languages', fontsize=15)
    # ax.set_ylabel('Number of tweets' , fontsize=15)
    # ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
    # tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

    # tweets_by_country = tweets['country'].value_counts()

    # fig, ax = plt.subplots()
    # ax.tick_params(axis='x', labelsize=15)
    # ax.tick_params(axis='y', labelsize=10)
    # ax.set_xlabel('Countries', fontsize=15)
    # ax.set_ylabel('Number of tweets' , fontsize=15)
    # ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
    # tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
