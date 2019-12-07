import time
import tweepy
import json
import requests
from textblob import TextBlob

#twitter keys
consumer_key = 'OmIemP8z6G9wmvAv4a3N9yR6k'
consumer_secret = 'lmUa6me3TQa3N5YSp0Y7m3lJ0XFOOFrC0kk3KZaCu1KQPfJYNB'
access_token = '385988316-ow3vIPPx5pRiHTGYk5SbuVpyk803XFYSBb2Sxqpm'
access_token_secret = 'rwEih4j9lEo9Uy6k65LTqJmO6NvqPXLCJ03oRAkmKXrGA'

#Particle Keys
particle_url = 'https://api.particle.io/v1/devices/e00fce6837e36cdaedf5ec05/led?access_token=7a7eaec24841b190f0c8baf54921f2ca87846ad1'
particle_token = '7a7eaec24841b190f0c8baf54921f2ca87846ad1'
particle_id = 'e00fce6837e36cdaedf5ec05'

#Variables
mood_string = 'neutral'
mood = 0
num = 1
number_tweets = 0
tweet_list = []

#Auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define the search term and the date_since date as variables
search_words = "#tellmeastory"
t = "2018-11-16"

def scrap(date_since):
    global number_tweets
    global mood
    # global date_since
    tweets = tweepy.Cursor(api.search,
                  q=search_words,
                  lang="en",
                  since=date_since).items(5)

    # Iterate and print tweets
    for tweet in tweets:
        if tweet.text not in tweet_list:
            tweet_list.append(tweet.text)
            raw_tweet = TextBlob(tweet.text)
            mood = mood + raw_tweet.sentiment.polarity
            number_tweets = number_tweets + 1
        # print("Tweet: ", tweet.text)
        # print(raw_tweet.sentiment.polarity)
        # print("Creado: ",tweet.created_at)
        # print ("Variable t", t)


while True:
    time.sleep(8)
    timer = t
    scrap(timer)

    if (mood > 2):
        mood_string = "2"
    else:
        if (mood < 2 and mood > - 2):
            mood_string = "1"
        else:
            if (mood < -2):
                mood_string = "0"

    data = {'arg' : mood_string,
            'ACCESS_TOKEN' : particle_token }

    x = requests.post(url = particle_url, data = data)

    print(tweet_list)
    print ("Mood_string: ", mood_string)
    print ("Mood_float", mood)
    print("Number of Tweets", number_tweets)
    # print ("Respuesta de Particle", x.text)
    # print (api.rate_limit_status())
