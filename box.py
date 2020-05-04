from copy import copy
from datetime import datetime, timedelta
from time import sleep

from music import Music


def get_seconds(time1, time2):
    return (
        (3600 * time2.hour + 60 * time2.minute + time2.second) -
        (3600 * time1.hour + 60 * time1.minute + time1.second)
    )


class Box:
    def __init__(self, directory):
        self.directory = directory
        self.music_list = []

    def add_music(self, start, music=None):
        start = datetime.strptime(start, '%H:%M:%S').time() # TODO add date!
        music = copy(music) if music else Music(self.directory)
        music.start = start
        self.music_list.append(music)
        self.music_list.sort(key=lambda _: _.start)

    def add_period(self, start, duration=timedelta(minutes=45)):  # TODO test
        self.add_music(start)
        start = (
            datetime.strptime(start, '%H:%M:%S') +
            duration
        ).strftime('%H:%M:%S')
        self.add_music(start)

    def add_couple(
            self, start,
            durations=(timedelta(minutes=45), timedelta(minutes=5))
    ):  # TODO test
        self.add_period(start, durations[0])
        start = (
                datetime.strptime(start, '%H:%M:%S') +
                durations[0] + durations[1]
        ).strftime('%H:%M:%S')
        self.add_period(start, durations[0])

    def __str__(self):
        return '\n'.join(str(_) for _ in self.music_list)

    def start(self):
        time1 = datetime.now().time()
        while self.music_list:
            music = self.music_list.pop(0)
            seconds = get_seconds(time1=time1, time2=music.start)
            if seconds > 0:
                # TODO обновляемый таймер в консоли: "до следущего трека"
                sleep(seconds)
                music.play()
                time1 = datetime.now().time()


def test1():
    box = Box(directory='test_music')
    box.add_music(start='01:00:00')
    box.add_music(start='03:00:00')
    box.add_music(start='02:00:00')
    assert [_.start.hour for _ in box.music_list] == [1, 2, 3], 'test1'


def test2():
    # TODO Выбрать другой звук (для разнообразия)
    print('\nТЕСТ: Воспроизведение звука гонга.')
    box = Box(directory='test_music')
    gong = Music(box.directory, mp3='gong')
    start = datetime.now() + timedelta(seconds=1)
    box.add_music(start.strftime('%H:%M:%S'), music=gong)
    box.start()


def test3():
    # TODO Дабавить ещё несколько звуков в test_music
    print('\nТЕСТ: Воспроизведение случайного звука.')
    box = Box(directory='test_music')
    start = datetime.now() + timedelta(seconds=1)
    box.add_music(start.strftime('%H:%M:%S'))
    box.start()


def test4():
    print('\nТЕСТ: Воспроизведение через 5, 10 и 15 секунд.')
    box = Box(directory='test_music')
    gong = Music(box.directory, mp3='gong')  # Длительность менее 5 секунд!
    start = datetime.now()
    for _ in range(3):
        start += timedelta(seconds=5)
        box.add_music(start=start.strftime('%H:%M:%S'), music=gong)
    box.start()


if __name__ == '__main__':
    for test in test1, test2, test3, test4:
        test()
