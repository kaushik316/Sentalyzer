from auth import consumer_key, consumer_secret, access_token, access_token_secret
import requests
import tweepy 
import re
import sentalyzer_module as sm 
import nltk


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

searchterm = 'Exxon stock'
num_of_tweets = 75

def clean_tweets(wordlist):
	for i in range(0, len(wordlist)):
		wordlist[i] = re.sub(r'#|[^a-zA-Z ]','',wordlist[i])
		wordlist[i] = re.sub(r"rt|'|http\S+|@\S+","",wordlist[i])
	return wordlist


raw_tweets = [tweet.text.lower() for tweet in tweepy.Cursor(api.search,q=searchterm,count=num_of_tweets).items(num_of_tweets)]
clean_tweets = list(set(clean_tweets(raw_tweets)))

sm.popular_words(clean_tweets, pos="noun")
sm.pct_positive(clean_tweets)

