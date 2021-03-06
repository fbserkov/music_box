from copy import copy
from datetime import datetime, timedelta
import sys
from time import sleep

from music import Music


class Box:
    """
    TODO
    """
    def __init__(self, directory):
        """
        Box object constructor.

        :param directory: path where mp3-files to use are located
        """
        self.directory = directory
        self.music_list = []

    def add_music(self, start, music=None):
        """
        Adds to the playback schedule one sound signal tied to the specified
        time.

        :param start:
        :param music:
        :return:
        """
        now = datetime.now()
        start = datetime.strptime(
            now.strftime('%d.%m.%Y') + ' ' + start, '%d.%m.%Y %H:%M:%S')
        if start < now:
            start += timedelta(1)

        music = copy(music) if music else Music(self.directory)
        music.start = start
        self.music_list.append(music)
        self.music_list.sort(key=lambda _: _.start)

    def add_period(self, start, duration=timedelta(minutes=45)):
        """
        Adds one period to the playback schedule: signal of the beginning
        and signal of end.

        :param start: start time of the period
        :param duration: length of the period
        """
        self.add_music(start)
        start = (
            datetime.strptime(start, '%H:%M:%S') +
            duration
        ).strftime('%H:%M:%S')
        self.add_music(start)

    def add_couple(
            self, start,
            durations=(timedelta(minutes=45), timedelta(minutes=5))
    ):
        """
        Adds two periods at once.

        :param start: start time of the first period
        :param durations: a tuple containing the length of periods and the gap
        between periods
        """
        self.add_period(start, durations[0])
        start = (
                datetime.strptime(start, '%H:%M:%S') +
                durations[0] + durations[1]
        ).strftime('%H:%M:%S')
        self.add_period(start, durations[0])

    def add_triple(
            self, start,
            durations=(timedelta(minutes=45), timedelta(minutes=10))
    ):
        """
        Adds three periods at once.

        :param start: start time of the first period
        :param durations: a tuple containing the length of periods and the gap
        between periods
        """
        self.add_period(start, durations[0])
        start = (
                datetime.strptime(start, '%H:%M:%S') +
                durations[0] + durations[1]
        ).strftime('%H:%M:%S')
        self.add_period(start, durations[0])
        start = (
                datetime.strptime(start, '%H:%M:%S') +
                durations[0] + durations[1]
        ).strftime('%H:%M:%S')
        self.add_period(start, durations[0])

    def __str__(self):
        """
        Forms a string representation of a Box object as a set string
        representation of a contained Music objects.
        """
        return '\n'.join(str(_) for _ in self.music_list)

    def start(self, test=False):
        """
        Launches the generated playback schedule to work.

        :param test: if true, the loop will not be infinite.
        """
        now = datetime.now()
        while self.music_list:
            music = self.music_list.pop(0)
            print('WAIT', music, end='')
            sys.stdout.flush()
            if music.start > now:
                sleep((music.start - now).seconds)
                print('\rPLAY', end='')
                music.play()
                print('\rDONE')
                now = datetime.now()  # update after sleep and play
            else:
                print('\rSKIP')
            if not test:
                music.start += timedelta(1)
                self.music_list.append(music)


def test1():
    """
    Box.add_music() method verification: that the ordering of Music objects by
    start time is respected.
    """
    box = Box(directory='test_music')
    box.add_music(start='00:00:00')
    box.add_music(start='02:00:00')
    box.add_music(start='01:00:00')
    assert [_.start.hour for _ in box.music_list] == [0, 1, 2], 'test1'


def test2():
    """
    Box.add_music() method verification: that the elapsed time is scheduled
    for the next day.
    """
    box = Box(directory='test_music')
    start1 = (datetime.now() + timedelta(minutes=5)).strftime('%H:%M:%S')
    start2 = (datetime.now() - timedelta(minutes=5)).strftime('%H:%M:%S')
    box.add_music(start1)
    box.add_music(start2)
    assert ((
        box.music_list[1].start.date() -
        box.music_list[0].start.date()
    ) == timedelta(1)), 'test2'


def test3():
    """Box.add_period() method verification."""
    box = Box(directory='test_music')
    box.add_period(start='00:00:00')
    assert (
        [(_.start.hour, _.start.minute) for _ in box.music_list] ==
        [(0, 0), (0, 45)]
    ), 'test3'


def test4():
    """Box.add_couple() method verification."""
    box = Box(directory='test_music')
    box.add_couple(start='00:00:00')
    assert (
        [(_.start.hour, _.start.minute) for _ in box.music_list] ==
        [(0, 0), (0, 45), (0, 50), (1, 35)]
    ), 'test4'


def test5():
    """Box.add_triple() method verification."""
    box = Box(directory='test_music')
    box.add_triple(start='00:00:00')
    assert (
        [(_.start.hour, _.start.minute) for _ in box.music_list] ==
        [(0, 0), (0, 45), (0, 55), (1, 40), (1, 50), (2, 35)]
    ), 'test5'


def test6():
    """Checking the launch to play explicitly specified sound file."""
    box = Box(directory='test_music')
    music = Music(box.directory)  # explicit music object
    start = datetime.now() + timedelta(seconds=1)
    box.add_music(start.strftime('%H:%M:%S'), music)
    box.start(test=True)
    assert input('Did you hear the note? (y/n) ') == 'y', 'test6'


def test7():
    """Checking the launch for play implicitly specified sound file."""
    box = Box(directory='test_music')
    start = datetime.now() + timedelta(seconds=1)
    box.add_music(start.strftime('%H:%M:%S'))
    box.start(test=True)
    assert input('Did you hear the note? (y/n) ') == 'y', 'test7'


def test8():
    """
    Checking the launch to play music according to the generated schedule.
    """
    box = Box(directory='test_music')
    start = datetime.now()
    for _ in range(5):
        duration = 3  # must be more than file duration in test_music
        start += timedelta(seconds=duration)
        box.add_music(start=start.strftime('%H:%M:%S'))
    box.start(test=True)
    assert input(
        'Did the notes sound every three seconds? (y/n) ') == 'y', 'test8'


if __name__ == '__main__':
    for num in 1, 2, 3, 4, 5, 6, 7, 8:
        eval(f'test{num}()')
