from time import sleep
from music import Music


class Box:
    def __init__(self, music_dir=''):
        self._music_dir = music_dir
        self._music_list = []

    def add_music(self, time, mp3=None, volume=1.0):
        self._music_list.append(Music(time, mp3, volume))

    def start(self):
        Music._music_dir = self._music_dir
        while self._music_list:
            for play in self._music_list:
                play()
            sleep(1)


if __name__ == '__main__':  # tests
    from datetime import datetime

    # TODO Несколько запусков
    box = Box()
    box.add_music(time=datetime.now().strftime('%H:%M:%S'), mp3='gong')
    box.start()
