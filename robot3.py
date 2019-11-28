import time
import tweepy
import json
import requests
from textblob import TextBlob
# from datetime import timedelta

consumer_key = 'OmIemP8z6G9wmvAv4a3N9yR6k'
consumer_secret = 'lmUa6me3TQa3N5YSp0Y7m3lJ0XFOOFrC0kk3KZaCu1KQPfJYNB'
access_token = '385988316-ow3vIPPx5pRiHTGYk5SbuVpyk803XFYSBb2Sxqpm'
access_token_secret = 'rwEih4j9lEo9Uy6k65LTqJmO6NvqPXLCJ03oRAkmKXrGA'
particle_url = 'https://api.particle.io/v1/devices/e00fce6860fd075a10f01dc9/led?access_token=7a7eaec24841b190f0c8baf54921f2ca87846ad1'
particle_token = '7a7eaec24841b190f0c8baf54921f2ca87846ad1'
particle_id = 'e00fce6860fd075a10f01dc9'
mood_string = '0'
mood = 0

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Define the search term and the date_since date as variables
search_words = "#tuesdaythoughts"
t = "2018-11-16"

def unique(list1):
    unique_list = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # for x in unique_list:
    #     print (x)

def scrap(date_since):
    global mood
    # global date_since
    tweets = tweepy.Cursor(api.search,
                  q=search_words,
                  lang="en",
                  since=date_since).items(2)

    # Iterate and print tweets
    for tweet in tweets:
        raw_tweet = TextBlob(tweet.text)
        t = tweet.created_at
        mood = mood + raw_tweet.sentiment.polarity
        print("Tweet: ", tweet.text)
        print(raw_tweet.sentiment.polarity)
        # print("Creado: ",tweet.created_at)
        # print ("Variable t", t)


while True:
    timer = t
    scrap(timer)
    time.sleep(10)

    if (mood > 5):
        mood_string = "happy"
    else:
        mood_string = "sad"

    # if ( > 1):
    #     mood_string = "2"
    # else:
    #     if (mood > 0.5):
    #         mood_string = "1"
    #     else:
    #         if(mood >= 0):
    #             mood_string = "0"
    #         else:
    #             if (mood < 0):
    #                 mood_string = "-1"

    data = {'arg' : mood_string,
            'ACCESS_TOKEN' : particle_token }

    x = requests.post(url = particle_url, data = data)

    # print ("Respuesta de Particle", x.text)
    # print (api.rate_limit_status())
    # print ("Mood_string: ", mood_string)
    # print ("Mood_float", mood)
