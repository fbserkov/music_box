from copy import copy
from datetime import datetime, timedelta
from time import sleep

from music import Music


class Box:
    def __init__(self, directory):
        self.directory = directory
        self.music_list = []

    def add_music(self, start, music=None):
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
        self.add_period(start, durations[0])
        start = (
                datetime.strptime(start, '%H:%M:%S') +
                durations[0] + durations[1]
        ).strftime('%H:%M:%S')
        self.add_period(start, durations[0])

    def __str__(self):
        return '\n'.join(str(_) for _ in self.music_list)

    def start(self):
        now = datetime.now()
        while self.music_list:
            music = self.music_list.pop(0)
            seconds = (music.start - now).seconds
            if seconds >= 0:
                sleep(seconds)
                music.play()
                now = datetime.now()
            music.start += timedelta(1)
            self.music_list.append(music)


def test1():
    box = Box(directory='test_music')
    start1 = (datetime.now() + timedelta(minutes=5)).strftime('%H:%M:%S')
    start2 = (datetime.now() - timedelta(minutes=5)).strftime('%H:%M:%S')
    box.add_music(start1)
    box.add_music(start2)
    assert ((
        box.music_list[1].start.date() -
        box.music_list[0].start.date()
    ) == timedelta(1)), 'test1'


def test2():
    box = Box(directory='test_music')
    box.add_music(start='00:00:00')
    box.add_music(start='02:00:00')
    box.add_music(start='01:00:00')
    assert [_.start.hour for _ in box.music_list] == [0, 1, 2], 'test2'


def test3():
    box = Box(directory='test_music')
    box.add_period(start='00:00:00')
    assert (
        [(_.start.hour, _.start.minute) for _ in box.music_list] ==
        [(0, 0), (0, 45)]
    ), 'test3'


def test4():
    box = Box(directory='test_music')
    box.add_couple(start='00:00:00')
    assert (
        [(_.start.hour, _.start.minute) for _ in box.music_list] ==
        [(0, 0), (0, 45), (0, 50), (1, 35)]
    ), 'test4'


def test5():
    box = Box(directory='test_music')
    music = Music(box.directory)  # explicit music object
    start = datetime.now() + timedelta(seconds=1)
    box.add_music(start.strftime('%H:%M:%S'), music)
    box.start()
    assert input('Did you hear the note? (y/n) ') == 'y', 'test5'


def test6():
    box = Box(directory='test_music')
    start = datetime.now() + timedelta(seconds=1)
    box.add_music(start.strftime('%H:%M:%S'))  # implicit music object
    box.start()
    assert input('Did you hear the note? (y/n) ') == 'y', 'test6'


def test7():
    box = Box(directory='test_music')
    start = datetime.now()
    for _ in range(5):
        duration = 3  # must be more than file duration in test_music
        start += timedelta(seconds=duration)
        box.add_music(start=start.strftime('%H:%M:%S'))
    box.start()
    assert input(
        'Did the notes sound every three seconds? (y/n) ') == 'y', 'test7'


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
