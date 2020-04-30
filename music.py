from datetime import date, datetime
from time import sleep

from mutagen.mp3 import MP3
import pygame

pygame.init()


class Music:
    def __init__(self, time, filename, volume=1.0):
        time = time + ':00' if len(time) == 5 else time
        self._time = datetime.strptime(
            f'{date.today()} {time}', '%Y-%m-%d  %H:%M:%S')
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
        if str(self._time) == str(datetime.now()).split('.')[0]:  # TODO
            print(self)
            self._play()


if __name__ == '__main__':  # tests
    for _ in range(3):
        Music(time=datetime.now().strftime('%H:%M:%S'), filename='gong.mp3')()
