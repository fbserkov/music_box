import copy
from datetime import datetime, timedelta
from time import sleep

from music import Music


class Box:
    def __init__(self):
        self._music_list = []

    def add_music(self, time, music):
        time = datetime.strptime(time, '%H:%M:%S').time()
        music = copy.copy(music)
        music.time = time
        self._music_list.append(music)

    def start(self):
        while self._music_list:
            for music in self._music_list:
                music.check()
            sleep(1)


if __name__ == '__main__':  # tests
    box = Box()
    gong = Music(mp3='gong')
    now = datetime.now()

    for _ in range(3):
        box.add_music(time=now.strftime('%H:%M:%S'), music=gong)
        now += timedelta(seconds=5)
    box.start()
