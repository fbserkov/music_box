from datetime import datetime
from importlib import reload
import os
from time import sleep

from mutagen.mp3 import MP3
import pygame

import playlist


def play_file(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    sleep(MP3(filename).info.length)


def reload_playlist():
    try:
        reload(playlist)
    except SyntaxError as exc:
        print(exc)
        play_file('siren.mp3')
    return playlist.LIST


def main():
    pygame.init()
    while True:
        sleep(10)
        for item in reload_playlist():
            if item['time'] == datetime.now().strftime('%H:%M'):
                print(item['time'], item['mp3'])
                play_file(os.path.join(playlist.DIR, item['mp3'] + '.mp3'))


if __name__ == '__main__':
    main()
