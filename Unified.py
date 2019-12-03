import time
import tweepy
import json
import requests
import pygame as pg
from textblob import TextBlob
from sseclient import SSEClient

# from datetime import timedelta

#twitter keys
consumer_key = 'OmIemP8z6G9wmvAv4a3N9yR6k'
consumer_secret = 'lmUa6me3TQa3N5YSp0Y7m3lJ0XFOOFrC0kk3KZaCu1KQPfJYNB'
access_token = '385988316-ow3vIPPx5pRiHTGYk5SbuVpyk803XFYSBb2Sxqpm'
access_token_secret = 'rwEih4j9lEo9Uy6k65LTqJmO6NvqPXLCJ03oRAkmKXrGA'

#Particle Keys
particle_url = 'https://api.particle.io/v1/devices/e00fce6860fd075a10f01dc9/led?access_token=7a7eaec24841b190f0c8baf54921f2ca87846ad1'
particle_token = '7a7eaec24841b190f0c8baf54921f2ca87846ad1'
particle_id = 'e00fce6860fd075a10f01dc9'

#GetEvent
messages = SSEClient('https://api.spark.io/v1/events/bump?access_token=7a7eaec24841b190f0c8baf54921f2ca87846ad1')

#Variables
mood_string = '0'
mood = 0
rocket = 0
tweet_list = []
# rand_int = Math.randomint(16)
# music_file ="data/{0}/{1}.mp3".format(folder, rand_int)
music_file = "data/angry/1.mp3"
volume = 0.8 # optional volume 0 to 1.0

#Auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define the search term and the date_since date as variables
search_words = "#blackfriday"
t = "2018-11-16"

def scrap(date_since):
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


def play_music(music_file, volume=0.8):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''

    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)

    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)


while True:
    timer = t
    scrap(timer)
    print (tweet_list)
    time.sleep(5)

    #Mood
    if (mood > 5):
        mood_string = "happy"
    else:
        mood_string = "sad"

        #POST
        data = {'arg' : mood_string,
                'ACCESS_TOKEN' : particle_token }

        x = requests.post(url = particle_url, data = data)

        #Debug
        print ("Mood_string: ", mood_string)
        print ("Mood_float", mood)
        # print ("Respuesta de Particle", x.text)
        # print (api.rate_limit_status())


def bumping():
    for msg in messages:
        y = msg.data
        if y == "":
            print("empty")
        else:
            play_music(music_file, volume)
