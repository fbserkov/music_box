import os
from time import sleep

from mutagen.mp3 import MP3
import pygame

DIR = '/home/fedor/Music/'
filename = os.path.join(DIR, 'Zivert - Life.mp3')
print(MP3(filename).info.length)

pygame.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()
sleep(10)
