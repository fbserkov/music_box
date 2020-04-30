from datetime import datetime, timedelta
import os
from time import sleep

from music import Music


class Box:
    def __init__(self, music_dir=''):
        self._music_dir = music_dir
        self._music_list = []

    def add_music(self, time, mp3=None, volume=1.0):
        if mp3:
            time = datetime.strptime(time, '%H:%M:%S').time()
            # TODO Проверка существования файла
            filename = os.path.join(self._music_dir, mp3 + '.mp3')
            self._music_list.append(Music(time, filename, volume))

    def start(self):
        Music._music_dir = self._music_dir
        while self._music_list:
            for play in self._music_list:
                play()
            sleep(1)


if __name__ == '__main__':  # tests
    box = Box()
    now = datetime.now()
    for _ in range(3):
        box.add_music(now.strftime('%H:%M:%S'), mp3='gong')
        now += timedelta(seconds=5)
    box.start()
