print('Samantha Moross''\n''Project 3''\n''Section 002: Wednesday 5:30-6:30 pm''\n''Twitter API B')

print('-----------')

#D) Twitter API: twitterhw3b.py

import tweepy
from textblob import TextBlob
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

consumer_key = '66yyc4VEWqdze1c14wjIOjm93'
consumer_secret = 'XJu649Ydvwhxcv1stdu4vhOtWxGPaRE1FyvxobpK3NuwRRMIlY'
access_token = 	'290741488-Sik07q8LDzdjhmknQm0hEn3WCtiAlabNEZ402cky'
access_token_secret = '89PQqLV0BfJB25A7O9ZiVzeqwN4MyYaHJi829iz20pa6R'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#sets authorization tokens

api = tweepy.API(auth)
#Defines the API

pol_count = 0
pol_total = 0

sub_count = 0
sub_total = 0

search_term = input('Input Search ') #user inputs search term
for tweet in tweepy.Cursor(api.search, q=search_term, result_type="recent", include_entities=True, lang="en").items(100):
	print (tweet.text) #prints 100 most recent tweets that have the keyword 
	text = TextBlob(tweet.text) #combines all the tweets into a single text

	pol_count = pol_count + 1
	pol_total = pol_total + text.polarity

	sub_count = sub_count + 1
	sub_total = sub_total + text.subjectivity

avg_pol = pol_total/pol_count
avg_sub = sub_total/sub_count

print('-----------')
print("Average subjectivity is " +str(avg_sub))
print("Average polarity is " + str(avg_pol))





