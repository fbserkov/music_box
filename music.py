from datetime import datetime
import os
from time import sleep

from mutagen.mp3 import MP3
import pygame

pygame.init()


class Music:
    directory = './'

    def __init__(self, mp3, volume=1.0):
        filename = os.path.join(Music.directory, mp3 + '.mp3')
        assert os.path.exists(filename), 'No file ' + filename
        self._filename = filename
        self._volume = volume
        self.time = None

    def play(self):
        print(self.time, '-', self._filename)
        pygame.mixer.music.load(self._filename)
        pygame.mixer.music.set_volume(self._volume)
        pygame.mixer.music.play()
        sleep(MP3(self._filename).info.length)

    def check(self):
        assert self.time, 'No time'
        now = datetime.now().time()
        if (
                self.time.hour == now.hour and
                self.time.minute == now.minute and
                self.time.second == now.second
        ):
            self.play()


if __name__ == '__main__':  # tests
    music = Music(mp3='gong')
    # music.check()
    music.play()

    music.time = datetime.now().time()
    music.check()
