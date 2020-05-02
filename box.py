import copy
from datetime import datetime, timedelta
from time import sleep

from music import Music


def get_seconds(time1, time2):
    return (
        (3600 * time2.hour + 60 * time2.minute + time2.second) -
        (3600 * time1.hour + 60 * time1.minute + time1.second)
    )


class Box:
    def __init__(self):
        self._music_list = []

    def add_music(self, start, music):
        start = datetime.strptime(start, '%H:%M:%S').time()
        music = copy.copy(music)
        music.start = start
        self._music_list.append(music)

    def start(self):
        time1 = datetime.now().time()
        while self._music_list:
            # TODO Учёт длины файла, если он играет перед занятием
            music = self._music_list.pop(0)
            seconds = get_seconds(time1=time1, time2=music.start)
            if seconds > 0:
                # TODO обновляемый таймер в консоли: "до следущего трека"
                sleep(seconds)
                music.play()
                time1 = datetime.now().time()

    # TODO отображение списка воспроизведения (Box.__str__)


if __name__ == '__main__':
    print('\nТЕСТ: Воспроизведение звука гонга через 5 секунд. Три раза.')
    box = Box()
    gong = Music(mp3='gong')

    start = datetime.now()
    for _ in range(3):
        start += timedelta(seconds=5)
        box.add_music(start=start.strftime('%H:%M:%S'), music=gong)

    box.start()
