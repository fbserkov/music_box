from box import Box

my_box = Box(music_dir='/home/fedor/Music/')

# Пара 1
my_box.add_music(time='05:30:00', mp3='siren', volume=0.5),  # job
my_box.add_music(time='06:15:00', mp3='candyman_19_cue_2b_piano'),  # break
my_box.add_music(time='06:20:00', mp3='siren', volume=0.5),  # job
my_box.add_music(time='07:05:00', mp3='candyman_19_cue_2b_piano'),  # break

# Пара 2
my_box.add_music(time='08:35:00', mp3='siren', volume=0.5),  # job
my_box.add_music(time='09:20:00', mp3='candyman_19_cue_2b_piano'),  # break
my_box.add_music(time='09:25:00', mp3='siren', volume=0.5),  # job
my_box.add_music(time='10:10:00', mp3='candyman_19_cue_2b_piano'),  # break

# Пара 3
my_box.add_music(time='10:25:00', mp3='siren', volume=0.5),  # job
my_box.add_music(time='11:10:00', mp3='candyman_19_cue_2b_piano'),  # break
my_box.add_music(time='11:15:00', mp3='siren', volume=0.5),  # job
my_box.add_music(time='12:00:00', mp3='candyman_19_cue_2b_piano'),  # break

# Пара 4
my_box.add_music(time='13:00:00', mp3='siren', volume=0.5),  # job
my_box.add_music(time='13:45:00', mp3='candyman_19_cue_2b_piano'),  # break
my_box.add_music(time='13:50:00', mp3='siren', volume=0.5),  # job
my_box.add_music(time='14:35:00', mp3='candyman_19_cue_2b_piano'),  # break

# Пара 5
my_box.add_music(time='14:50:00', mp3='siren', volume=0.5),  # job
my_box.add_music(time='15:35:00', mp3='candyman_19_cue_2b_piano'),  # break
my_box.add_music(time='15:40:00', mp3='siren', volume=0.5),  # job
my_box.add_music(time='16:25:00', mp3='Zivert - Life'),  # break

# Пара 6
my_box.add_music(time='17:55:00', mp3='siren', volume=0.5),  # job
my_box.add_music(time='18:40:00', mp3='candyman_19_cue_2b_piano'),  # break
my_box.add_music(time='18:45:00', mp3='siren', volume=0.5),  # job
my_box.add_music(time='19:30:00', mp3='Zivert - Life'),  # break

my_box.start()
