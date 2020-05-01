import copy
from datetime import datetime, timedelta
from time import sleep

from music import Music


def get_seconds(time1, time2):
    return (
        (3600 * time2.hour + 60 * time2.minute + time2.second) -
        (3600 * time1.hour + 60 * time1.minute + time1.second)
    )


class Box:
    def __init__(self):
        self._music_list = []

    def add_music(self, time, music):
        time = datetime.strptime(time, '%H:%M:%S').time()
        music = copy.copy(music)
        music.time = time
        self._music_list.append(music)

    def start(self):
        time1 = datetime.now().time()
        while self._music_list:
            music = self._music_list.pop(0)
            seconds = get_seconds(time1=time1, time2=music.time)
            if seconds > 0:
                sleep(seconds)
                music.play()
                time1 = datetime.now().time()


if __name__ == '__main__':  # tests
    box = Box()
    gong = Music(mp3='gong')
    now = datetime.now()

    for _ in range(3):
        box.add_music(time=now.strftime('%H:%M:%S'), music=gong)
        now += timedelta(seconds=5)
    box.start()
