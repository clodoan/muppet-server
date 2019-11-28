# import pygame
#import mixer Load the popular external library
from sseclient import SSEClient
import json

messages = SSEClient('https://api.spark.io/v1/events/bump?access_token=7a7eaec24841b190f0c8baf54921f2ca87846ad1')
# file = '/Users/claudio/Desktop/00\ Real\ Muppet/data/gameover.wav'
#
for msg in messages:
    print (msg)
#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load(file)
#     pygame.mixer.music.play()
#     pygame.event.wait()





# mixer.music.load('e:/LOCAL/Betrayer/Metalik Klinik1-Anak Sekolah.mp3')
