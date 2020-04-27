from datetime import datetime
import os
from importlib import reload
from time import sleep

from mutagen.mp3 import MP3
import pygame

import playlist


def check():
    reload(playlist)
    now = datetime.now()
    current = 60 * now.hour + now.minute
    for _dict in playlist.LIST:
        expected = 60 * _dict['hour'] + _dict['minute']
        print(current, expected)
        if current == expected:
            play(os.path.join(playlist.DIR, _dict['filename']))


def get_length(filename):
    return MP3(filename).info.length


def play(filename):
    pygame.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    sleep(get_length(filename))


if __name__ == '__main__':
    while True:
        check()
        sleep(10)
