import os


class Music:
    directory = './'

    def __init__(self, mp3, gain=1):
        filename = os.path.join(Music.directory, mp3 + '.mp3')
        assert os.path.exists(filename), 'No file ' + filename
        self._filename = filename
        self._gain = gain
        self.start = None

    def __str__(self):
        return f'{self.start} - {self._filename}'

    def play(self):
        print(self)
        os.system(f'cvlc {self._filename} --gain {self._gain} --play-and-exit')


if __name__ == '__main__':
    print('\nТЕСТ: Воспроизведение звука гонга.')
    music = Music(mp3='gong')
    music.play()

    print('\nТЕСТ: Воспроизведение с меньшей громкостью.')
    music._gain = 0.5
    music.play()
