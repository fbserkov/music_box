'Module doc'  # TODO
from datetime import datetime
import os
import random


class Music:
    'Class'  # TODO
    def __init__(self, directory, mp3=None, gain=1.0):
        '''

        :param directory:
        :param mp3:
        :param gain:
        '''  # TODO
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
        # "%s" for file names with spaces
        cmd = 'cvlc "%s" --gain %s --play-and-exit 2> /dev/null'
        os.system(cmd % (self._filename, self.gain))


def test1(names):
    for i, name in enumerate(names):
        music = Music(directory='test_music', mp3=name)
        print(f'({i + 1}/{len(names)})', music)
        music.play()
    assert input(
        'Were the notes played in direct order? (y/n) ') == 'y', 'test1'


def test2():
    num = 10
    for i in range(num):
        music = Music(directory='test_music')
        print(f'({i + 1}/{num})', music)
        music.play()
    assert input('Were the notes played randomly? (y/n) ') == 'y', 'test2'


def test3(names):
    for i, name in enumerate(reversed(names)):
        music = Music(directory='test_music', mp3=name, gain=1-i/10)
        print(f'({i + 1}/{len(names)})', music)
        music.play()
    assert input('Did the playback volume decrease? (y/n) ') == 'y', 'test3'


if __name__ == '__main__':
    NAMES = 'do', 're', 'mi', 'fa', 'so', 'la', 'si'
    test1(NAMES)
    test2()
    test3(NAMES)
