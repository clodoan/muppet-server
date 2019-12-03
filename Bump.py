from sseclient import SSEClient
import time
import json
import pygame as pg

messages = SSEClient('https://api.spark.io/v1/events/bump?access_token=7a7eaec24841b190f0c8baf54921f2ca87846ad1')

music_file = "data/fart1.mp3"
volume = 0.8

# optional volume 0 to 1.0

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
# pick a MP3 music file you have in the working folder
# otherwise give the full file path
# (try other sound file formats too)


for msg in messages:
    y = msg.data
    if y == "":
        print("empty")
    else:
        play_music(music_file, volume)

    # yjs = json.loads(y)
    # print(yjs)

    # if type(y) is not str:
    #     yjs = json.loads(y)
    #     print(yjs)
        # filtername = "bump"
        # if yjs[filtername] == "ouch":
        #      play_music(music_file, volume)


     # x = json.dumps(msg)

     # if msg["data"] == "ouch":
     #    print("ouch")


    # if "ouch" not in messages:
    #     play_music(music_file, volume)

    # x = messages
    # y = json.loads(x)
    # if messages["data"] == "ouch":

# while True:
#     print(messages)
#     time.sleep(1)
