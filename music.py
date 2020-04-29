from datetime import date, datetime
import os
from time import sleep

from mutagen.mp3 import MP3
import pygame


class Music:
    pygame.init()
    _music_dir = ''

    def __init__(self, time, mp3, volume=1.0):
        time = time + ':00' if len(time) == 5 else time
        self._time = datetime.strptime(
            f'{date.today()} {time}', '%Y-%m-%d  %H:%M:%S')
        self.filename = os.path.join(Music._music_dir, mp3 + '.mp3')  # TODO Проверка существования файла
        self.volume = volume

    def __str__(self):
        return f'{self._time} - {self.filename}'

    def _play(self):
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play()
        sleep(MP3(self.filename).info.length)

    def __call__(self):
        if str(self._time) == str(datetime.now()).split('.')[0]:  # TODO
            print(self)
            self._play()


if __name__ == '__main__':  # tests
    Music(time=datetime.now().strftime('%H:%M:%S'), mp3='siren', volume=0.5)()
