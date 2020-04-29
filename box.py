from time import sleep
from music import Music


class Box:
    def __init__(self, music_dir, music_tuple):
        self._music_dir = music_dir
        self._music_tuple = music_tuple

    def start(self):
        Music._music_dir = self._music_dir
        while True:
            sleep(1)
            for play in self._music_tuple:
                play()
