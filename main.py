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
    for _dict in playlist.LIST:
        if (
                datetime.now().hour == _dict['hour'] and
                datetime.now().minute == _dict['minute']
        ):
            filename = os.path.join(playlist.DIR, _dict['filename'])
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            sleep(MP3(filename).info.length)
