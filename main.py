from box import Box
from music import Music

my_box = Box()

Music.directory = '/home/fedor/Music/'
siren = Music(mp3='siren', volume=0.5)
candyman = Music(mp3='candyman_19_cue_2b_piano')
zivert = Music(mp3='Zivert - Life')

# Пара 1
my_box.add_music(time='05:30:00', music=siren),  # start
my_box.add_music(time='06:15:00', music=candyman),  # end
my_box.add_music(time='06:20:00', music=siren),  # start
my_box.add_music(time='07:05:00', music=zivert),  # end

# Пара 2
my_box.add_music(time='08:35:00', music=siren),  # start
my_box.add_music(time='09:20:00', music=candyman),  # end
my_box.add_music(time='09:25:00', music=siren),  # start
my_box.add_music(time='10:10:00', music=zivert),  # end

# Пара 3
my_box.add_music(time='10:25:00', music=siren),  # start
my_box.add_music(time='11:10:00', music=candyman),  # end
my_box.add_music(time='11:15:00', music=siren),  # start
my_box.add_music(time='12:00:00', music=zivert),  # end

# Пара 4
my_box.add_music(time='13:00:00', music=siren),  # start
my_box.add_music(time='13:45:00', music=candyman),  # end
my_box.add_music(time='13:50:00', music=siren),  # start
my_box.add_music(time='14:35:00', music=zivert),  # end

# Пара 5
my_box.add_music(time='14:50:00', music=siren),  # start
my_box.add_music(time='15:35:00', music=candyman),  # end
my_box.add_music(time='15:40:00', music=siren),  # start
my_box.add_music(time='16:25:00', music=zivert),  # end

# Пара 6
my_box.add_music(time='17:55:00', music=siren),  # start
my_box.add_music(time='18:40:00', music=candyman),  # end
my_box.add_music(time='18:45:00', music=siren),  # start
my_box.add_music(time='19:30:00', music=zivert),  # end

my_box.start()
