from time import sleep
from signal import Signal


def start(music_dir, play_list):
    Signal.music_dir = music_dir
    while True:
        sleep(1)
        for play in play_list:
            play()
