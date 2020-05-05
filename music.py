from datetime import datetime
import os
import random


class Music:
    def __init__(self, directory, mp3=None, gain=1.0):
        if not mp3:
            mp3 = random.choice([
                name[:-4] for name in os.listdir(directory)
                if name.endswith('.mp3')
            ])
        self._directory = directory
        self._mp3 = mp3
        self._filename = os.path.join(directory, mp3 + '.mp3')
        assert os.path.exists(self._filename), 'No file ' + self._filename
        self.gain = gain
        self.start = None

    def __str__(self):
        if self.start:
            return f'{self.start.strftime("%H:%M:%S")} - {self._mp3}'
        return f'{datetime.now().strftime("%H:%M:%S")} - {self._mp3}'

    def play(self):
        cmd = 'cvlc "%s" --gain %s --play-and-exit 2> /dev/null'
        os.system(cmd % (self._filename, self.gain))


def test1(names):
    # A space in the names is not accidental. Files with spaces in the name
    # should not cause an error.
    for name in names:
        music = Music(directory='test_music', mp3=name)
        print(music)
        music.play()
    assert input(
        'Were the notes played in direct order? (y/n) ') == 'y', 'test1'


def test2():
    for _ in range(10):
        music = Music(directory='test_music')
        print(music)
        music.play()
    assert input('Were the notes played randomly? (y/n) ') == 'y', 'test2'


def test3(names):
    for i, name in enumerate(names):
        music = Music(directory='test_music', mp3=name, gain=1-i/10)
        print(music)
        music.play()
    assert input('Did the playback volume decrease? (y/n) ') == 'y', 'test3'


if __name__ == '__main__':
    NAMES = 'd o', 'r e', 'm i', 'f a', 's o', 'l a', 's i'
    test1(NAMES)
    test2()
    test3(reversed(NAMES))
