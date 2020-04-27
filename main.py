from datetime import datetime
from importlib import reload
import os
from time import sleep

from mutagen.mp3 import MP3
import pygame

import playlist


pygame.init()
while True:
    sleep(10)
    try:
        reload(playlist)
    except SyntaxError:
        pass
    for alarm in playlist.LIST:
        hour, minute = map(int, alarm['time'].split(':'))
        now = datetime.now()
        if now.hour == hour and now.minute == minute:
            print(alarm['time'], alarm['filename'])
            filename = os.path.join(
                playlist.DIR, alarm['filename'] + playlist.EXT)
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            sleep(MP3(filename).info.length)
