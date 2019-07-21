import tweepy
import csv
import pandas as pd
import numpy as np

consumer_key= 'WLpXq0qf6ocVTyzwaqVunbYpp'
consumer_secret = 'qV2tEsTQah2Ex4Y9PDcEWOuXScIWZ6H3yxRDmbqbh4SFZ7hUpa'

access_token='1112290132726411264-Aq7I5l2iNRBZh6khM07pmcIQ6gvM0a'
access_secret='tfIHL8MVFDleMeF7azzc4my1MiPg1qPb55zZctyL1irgB'

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api=tweepy.API(auth)

tweets = api.search(q="#datascience", count=1000, since="2019-05-22", lang = 'en')

message,favorite_count,retweet_count,created_at,user_name, user_location, user_verified=[],[],[],[],[],[],[]
for tweet in tweets:
    message.append(tweet.text)
    favorite_count.append(tweet.favorite_count)
    retweet_count.append(tweet.retweet_count)
    created_at.append(tweet.created_at)
    user_name.append(tweet.user.name)
    user_location.append(tweet.user.location)
    user_verified.append(tweet.user.verified)
    
df=pd.DataFrame({'Message':message,
                'Favourite Count':favorite_count,
                'Retweet Count':retweet_count,
                'Created At':created_at,
                'user_name':user_name,
                'user_location':user_location,
                'user_verified': user_verified})
				
df.to_csv("D:\Term 2\Data Visualization\Tweek\Tweets.csv")
