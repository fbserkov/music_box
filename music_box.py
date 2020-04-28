from datetime import datetime
import os
from time import sleep

from mutagen.mp3 import MP3
import pygame


def play_file(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    sleep(MP3(filename).info.length)


def main(music_dir, play_list):
    pygame.init()
    while True:
        sleep(10)
        for item in play_list:
            if item['time'] == datetime.now().strftime('%H:%M'):
                print(item['time'], item['mp3'])
                play_file(os.path.join(music_dir, item['mp3'] + '.mp3'))
