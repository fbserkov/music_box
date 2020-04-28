from datetime import datetime
import os
from time import sleep

from mutagen.mp3 import MP3
import pygame


class Play:
    music_dir = ''

    def __init__(self, time, mp3, volume=1):
        self.time = time  # TODO Проверка корректности значения времени
        self.mp3 = mp3  # TODO Проверка существования файла
        self.volume = volume

    def __str__(self):
        return f'{self.time} - {self.mp3}'

    def __call__(self):
        if self.time == datetime.now().strftime('%H:%M'):
            print(self)
            self._play()

    def _play(self):
        filename = os.path.join(Play.music_dir, self.mp3 + '.mp3')
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play()
        sleep(MP3(filename).info.length)


def start(music_dir, play_list):
    Play.music_dir = music_dir
    pygame.init()
    while True:
        sleep(1)
        for play in play_list:
            play()
