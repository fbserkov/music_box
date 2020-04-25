import os
from time import sleep

from mutagen.mp3 import MP3
import pygame

from playlist import DIR, my_list


def get_length(filename):
    return MP3(filename).info.length


def play(filename):
    pygame.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    sleep(get_length(_filename))


if __name__ == '__main__':
    _filename = os.path.join(DIR, my_list[0]['filename'])
    while True:
        sleep(1)
        if False:  # Если пора запускать
            play(_filename)
