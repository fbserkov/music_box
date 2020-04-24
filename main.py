import os
from time import sleep

from mutagen.mp3 import MP3
import pygame

DIR = '/home/fedor/Music/'


def get_length(filename):
    return MP3(filename).info.length


def play(filename):
    pygame.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    sleep(10)


if __name__ == '__main__':
    _filename = os.path.join(DIR, os.listdir(DIR)[0])
    print(get_length(_filename))
    play(_filename)
