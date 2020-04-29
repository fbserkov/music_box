from box import Box, Music

Box(music_dir='/home/fedor/Music/', music_tuple=(
    # Пара 1
    Music(time='05:30', mp3='siren', volume=0.5),  # job
    Music(time='06:15', mp3='candyman_19_cue_2b_piano'),  # break
    Music(time='06:20', mp3='siren', volume=0.5),  # job
    Music(time='07:05', mp3='candyman_19_cue_2b_piano'),  # break

    # Пара 2
    Music(time='08:35', mp3='siren', volume=0.5),  # job
    Music(time='09:20', mp3='candyman_19_cue_2b_piano'),  # break
    Music(time='09:25', mp3='siren', volume=0.5),  # job
    Music(time='10:10', mp3='candyman_19_cue_2b_piano'),  # break

    # Пара 3
    Music(time='10:25', mp3='siren', volume=0.5),  # job
    Music(time='11:10', mp3='candyman_19_cue_2b_piano'),  # break
    Music(time='11:15', mp3='siren', volume=0.5),  # job
    Music(time='12:00', mp3='candyman_19_cue_2b_piano'),  # break

    # Пара 4
    Music(time='13:00', mp3='siren', volume=0.5),  # job
    Music(time='13:45', mp3='candyman_19_cue_2b_piano'),  # break
    Music(time='13:50', mp3='siren', volume=0.5),  # job
    Music(time='14:35', mp3='candyman_19_cue_2b_piano'),  # break

    # Пара 5
    Music(time='14:50', mp3='siren', volume=0.5),  # job
    Music(time='15:35', mp3='candyman_19_cue_2b_piano'),  # break
    Music(time='15:40', mp3='siren', volume=0.5),  # job
    Music(time='16:25', mp3='Zivert - Life'),  # break

    # Пара 6
    Music(time='17:55', mp3='siren', volume=0.5),  # job
    Music(time='18:40', mp3='candyman_19_cue_2b_piano'),  # break
    Music(time='18:45', mp3='siren', volume=0.5),  # job
    Music(time='19:30', mp3='Zivert - Life'),  # break
)).start()
