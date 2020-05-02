from box import Box
from music import Music

my_box = Box()

Music.directory = '/home/fedor/Music/'
siren = Music(mp3='siren', gain=0.5)
candyman = Music(mp3='candyman_19_cue_2b_piano')
zivert = Music(mp3='Zivert - Life')  # TODO mp3=None - случайный файл

# Пара 1  TODO Определять пару одной функцией
my_box.add_music(start='05:30:00', music=siren)  # start
my_box.add_music(start='06:15:00', music=candyman)  # end
my_box.add_music(start='06:20:00', music=siren)  # start
my_box.add_music(start='07:05:00', music=zivert)  # end

# Пара 2
my_box.add_music(start='08:35:00', music=siren)  # start
my_box.add_music(start='09:20:00', music=candyman)  # end
my_box.add_music(start='09:25:00', music=siren)  # start
my_box.add_music(start='10:10:00', music=zivert)  # end

# Пара 3
my_box.add_music(start='10:25:00', music=siren)  # start
my_box.add_music(start='11:10:00', music=candyman)  # end
my_box.add_music(start='11:15:00', music=siren)  # start
my_box.add_music(start='12:00:00', music=zivert)  # end

# Пара 4
my_box.add_music(start='13:00:00', music=siren)  # start
my_box.add_music(start='13:45:00', music=candyman)  # end
my_box.add_music(start='13:50:00', music=siren)  # start
my_box.add_music(start='14:35:00', music=zivert)  # end

# Пара 5
my_box.add_music(start='14:50:00', music=siren)  # start
my_box.add_music(start='15:35:00', music=candyman)  # end
my_box.add_music(start='15:40:00', music=siren)  # start
my_box.add_music(start='16:25:00', music=zivert)  # end

# Пара 6
my_box.add_music(start='17:55:00', music=siren)  # start
my_box.add_music(start='18:40:00', music=candyman)  # end
my_box.add_music(start='18:45:00', music=siren)  # start
my_box.add_music(start='19:30:00', music=zivert)  # end

my_box.start()
