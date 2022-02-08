#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 22:30:52 2019

@author: Donna Nguyen, Janki Patel, Vanessa Zetino

This code will be used to analyze NASA's tweets stored on a CSV file.
"""

import os
import tweepy
import pandas

consumer_key='a76f8FxIPD1sYcWtNHe61TkGM'
consumer_secret='o5GRXNnQZLnxZ5BVYiyBT91PjnY1pPuqx41kjBvYDAvuJXAaY1'
access_token='1186414415890927617-qGOYJzQhG2idpX2k9nfygXYhtf8J5m'
access_token_secret='2mfKvBGXSTyx1RY5fjUrVC1hRq0tl6yD1Zr1nEcyzJaEZ'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# Create API object
api = tweepy.API(auth)

# Create a tweet
#api.update_status("Hello Tweepy")

tweet_id = '1192826446231654400'
tweet = api.get_status(tweet_id)
solar_tweet = api.search("solar eclipse from:NASA")
print(solar_tweet)
retweets = str(tweet.retweet_count)
likes = str(tweet.favorite_count)
print('Retweets: ' + retweets)
print('Likes: ' + likes)