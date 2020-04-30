from datetime import datetime
from time import sleep

from mutagen.mp3 import MP3
import pygame

pygame.init()


class Music:
    def __init__(self, time, filename, volume=1.0):
        self._time = time
        self._filename = filename
        self.volume = volume

    def __str__(self):
        return f'{self._time} - {self._filename}'

    def _play(self):
        pygame.mixer.music.load(self._filename)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play()
        sleep(MP3(self._filename).info.length)

    def __call__(self):
        now = datetime.now().time()
        if (
                self._time.hour == now.hour and
                self._time.minute == now.minute and
                self._time.second == now.second
        ):
            print(self)
            self._play()


if __name__ == '__main__':  # tests
    for _ in range(3):
        Music(time=datetime.now().time(), filename='gong.mp3')()
