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


if __name__ == '__main__':  # tests
    from datetime import datetime

    Box(music_dir='', music_tuple=(
        Music(time=datetime.now().strftime('%H:%M'), mp3='siren', volume=0.5),
    )).start()
