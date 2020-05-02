import os
from random import choice


class Music:
    directory = './'

    def __init__(self, mp3=None, gain=1):  # TODO Не только mp3 теперь
        if not mp3:
            mp3 = choice([
                name[:-4] for name in os.listdir(Music.directory)
                if name.endswith('.mp3')
            ])
        filename = os.path.join(Music.directory, mp3 + '.mp3')
        assert os.path.exists(filename), 'No file ' + filename
        self._filename = filename
        self._gain = gain
        self.start = None

    def __str__(self):
        return f'{self.start} - {self._filename}'

    def play(self):
        print(self)
        os.system(
            f'cvlc "{self._filename}" --gain {self._gain} --play-and-exit')


if __name__ == '__main__':  # TODO Тест для файла с пробелом в имени
    print('\nТЕСТ: Воспроизведение звука гонга.')
    music = Music()
    music.play()

    print('\nТЕСТ: Воспроизведение с меньшей громкостью.')
    music._gain = 0.5
    music.play()
