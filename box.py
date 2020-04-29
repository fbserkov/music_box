from time import sleep
from signal import Signal


class Box:
    def __init__(self, directory, playlist):
        self._music_dir = directory
        self._music_tuple = playlist

    def start(self):
        Signal.music_dir = self._music_dir
        while True:
            sleep(1)
            for play in self._music_tuple:
                play()
