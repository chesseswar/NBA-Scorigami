import requests
import json
import tweepy
from load import loadScores

keys = open('keys.txt').read().split('\n')

CONSUMER_KEY = keys[0]
CONSUMER_SECRET = keys[1]
ACCESS_KEY = keys[2]
ACCESS_SECRET = keys[3]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

scores, games = loadScores('games.txt')
        
for score in scores:
    print(score, ' : ', scores[score])



#TODO: do this but with statlines instead of final scores too
