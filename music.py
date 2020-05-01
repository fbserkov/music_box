from datetime import datetime
from time import sleep

from mutagen.mp3 import MP3
import pygame

pygame.init()


class Music:
    def __init__(self, filename, volume=1.0):
        self._filename = filename
        self.volume = volume
        self.time = None

    def play(self):
        print(self.time, '-', self._filename)
        pygame.mixer.music.load(self._filename)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play()
        sleep(MP3(self._filename).info.length)

    def check(self):
        now = datetime.now().time()
        if (
                self.time.hour == now.hour and
                self.time.minute == now.minute and
                self.time.second == now.second
        ):
            self.play()


if __name__ == '__main__':  # tests
    music = Music(filename='gong.mp3')
    music.play()

    music.time = datetime.now().time()
    music.check()
