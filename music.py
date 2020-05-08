"""
A module containing a description of the Music class and a set of tests.
"""
from datetime import datetime
import os
import random


class Music:
    """
    Description of the object used to start playing the specified sound file.
    Or a random file from the specified directory. It is possible to control
    the volume level.
    """
    def __init__(self, directory, mp3=None, gain=1.0):
        """
        Music object constructor.

        :param directory: path where mp3-files to use are located
        :param mp3: name of mp3-file
        :param gain: volume control parameter
        """
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
        """
        Forms a string representation of a Music object.

        :return: Format string 'HH:MM:SS - mp3_file_name'
        """
        if self.start:
            return f'{self.start.strftime("%H:%M:%S")} - {self._mp3}'
        return f'{datetime.now().strftime("%H:%M:%S")} - {self._mp3}'

    def play(self):
        """
        Play a sound file attached to a Music object.

        :return: None
        """
        cmd = 'cvlc'  # using VLC without a graphical interface
        cmd += ' "%s"'  # "" for file names with spaces
        cmd += ' --gain %s'  # volume control
        cmd += ' --play-and-exit'
        cmd += ' 2> /dev/null'
        os.system(cmd % (self._filename, self.gain))


def test1(names):
    """
    Testing the ability to create a Music object for a test set of sound files.

    :param names: Sound file names for use in the test.
    :return: None
    """
    for i, name in enumerate(names):
        music = Music(directory='test_music', mp3=name)
        print(f'({i + 1}/{len(names)})', music)
        music.play()
    assert input(
        'Were the notes played in direct order? (y/n) ') == 'y', 'test1'


def test2():
    """
    Checking the possibility of creating a Music object without specifying
    the name of the sound file. In this case, the file is selected randomly.

    :return: None
    """
    num = 10
    for i in range(num):
        music = Music(directory='test_music')
        print(f'({i + 1}/{num})', music)
        music.play()
    assert input('Were the notes played randomly? (y/n) ') == 'y', 'test2'


def test3(names):
    """
    Checking the ability to adjust the volume level.

    :param names: Sound file names for use in the test.
    :return: None
    """
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
