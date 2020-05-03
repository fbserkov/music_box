import os
from random import choice


class Music:
    def __init__(self, directory, mp3=None, gain=1):
        # TODO Не только mp3 теперь
        if not mp3:
            mp3 = choice([
                name[:-4] for name in os.listdir(directory)
                if name.endswith('.mp3')
            ])
        filename = os.path.join(directory, mp3 + '.mp3')
        assert os.path.exists(filename), 'No file ' + filename
        self.filename = filename
        self.gain = gain
        self.start = None

    def __str__(self):
        return f'{self.start} - {self.filename}'

    def play(self):
        print(self)
        os.system(
            f'cvlc "{self.filename}" --gain {self.gain} --play-and-exit')


if __name__ == '__main__':  # TODO Тест для файла с пробелом в имени
    print('\nТЕСТ: Воспроизведение звука гонга.')
    music = Music(directory='test_music')
    music.play()

    print('\nТЕСТ: Воспроизведение с меньшей громкостью.')
    music.gain = 0.5
    music.play()
