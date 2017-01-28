import tweepy

from textblob import TextBlob

consumer_key='DkfpeEPnXvRdi3XuLQosB9JiS'

consumer_secret='c9N84QVegylLrCaDy1bFEG9upLFUeDoqgL2EMEKMS7an2suWji'

access_token='223766287-0J4pevKOSZcIJl1FvdVfwdveTVTQS3jWTliyZ9Qu'

access_token_secret='B1HMOojOsLhCNCgz7zrQpyElCQHXVL0bi54dy7hvFfoQ5'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweet=api.search('bb ki vines')

for tweet in public_tweet:
   print tweet.text.encode("utf-8")
   analysis=TextBlob(tweet.text)
   print analysis.sentiment