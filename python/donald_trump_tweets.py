#!/usr/bin/python
import tweepy
import csv 
import os

# Consumer keys and access tokens, used for OAuth
consumer_key = 'CENSORED'
consumer_secret = 'CENSORED'
access_token = 'CENSORED'
access_token_secret = 'CENSORED'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

allTweets=[]

screen_name = "realDonaldTrump"

new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode="extended", include_rts=False)

allTweets.extend(new_tweets)

oldest = allTweets[-1].id -1

while len(new_tweets) > 0:
	print("getting new tweets before %s" % (oldest))
	new_tweets = api.user_timeline(screen_name = screen_name, count = 200, max_id = oldest, tweet_mode="extended", include_rts=False)
	allTweets.extend(new_tweets)
	oldest = allTweets[-1].id - 1
	print("Downloaded %s tweets so far..." % (len(allTweets)))
	
printTweets=[[tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")] for tweet in allTweets]

with open('donaldTrump.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(["id","date","text"])
	writer.writerows(printTweets)
pass


