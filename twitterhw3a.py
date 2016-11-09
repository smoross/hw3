#Twitter API: twitterhw3a.py

import tweepy
print ('Project 3''\n''Samantha Moross''\n''Section 002: Wednesday 5:30-6:30 pm')

#Retrieve unique code from Twitter
consumer_key = '66yyc4VEWqdze1c14wjIOjm93'
consumer_secret = 'XJu649Ydvwhxcv1stdu4vhOtWxGPaRE1FyvxobpK3NuwRRMIlY'
access_token = 	'290741488-Sik07q8LDzdjhmknQm0hEn3WCtiAlabNEZ402cky'
access_token_secret = '89PQqLV0BfJB25A7O9ZiVzeqwN4MyYaHJi829iz20pa6R'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#Generates auth string for OAuth method of authentication
auth.set_access_token(access_token, access_token_secret)
#Refreshes oauth method at a later time

api = tweepy.API(auth) 
#Authenticates, allows us to create tweets, delete tweets, and find Twitter users

img = "Friends.jpg" #Extract img
txt = "#UMSI-206 #Proj3" #Add Text

api.update_with_media(img,status=txt) #Adds text as image status

print("No output necessary")
