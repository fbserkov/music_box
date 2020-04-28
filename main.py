from music_box import Play, start

start(music_dir='/home/fedor/Music/', play_list=(
    # Пара 1
    Play(time='05:30', mp3='siren', volume=0.5),  # job
    Play(time='06:15', mp3='candyman_19_cue_2b_piano'),  # break
    Play(time='06:20', mp3='siren', volume=0.5),  # job
    Play(time='07:05', mp3='candyman_19_cue_2b_piano'),  # break

    # Пара 2
    Play(time='08:35', mp3='siren', volume=0.5),  # job
    Play(time='09:20', mp3='candyman_19_cue_2b_piano'),  # break
    Play(time='09:25', mp3='siren', volume=0.5),  # job
    Play(time='10:10', mp3='candyman_19_cue_2b_piano'),  # break

    # Пара 3
    Play(time='10:25', mp3='siren', volume=0.5),  # job
    Play(time='11:10', mp3='candyman_19_cue_2b_piano'),  # break
    Play(time='11:15', mp3='siren', volume=0.5),  # job
    Play(time='12:00', mp3='candyman_19_cue_2b_piano'),  # break

    # Пара 4
    Play(time='13:00', mp3='siren', volume=0.5),  # job
    Play(time='13:45', mp3='candyman_19_cue_2b_piano'),  # break
    Play(time='13:50', mp3='siren', volume=0.5),  # job
    Play(time='14:35', mp3='candyman_19_cue_2b_piano'),  # break

    # Пара 5
    Play(time='14:50', mp3='siren', volume=0.5),  # job
    Play(time='15:35', mp3='candyman_19_cue_2b_piano'),  # break
    Play(time='15:40', mp3='siren', volume=0.5),  # job
    Play(time='16:25', mp3='Zivert - Life'),  # break

    # Пара 6
    Play(time='17:55', mp3='siren', volume=0.5),  # job
    Play(time='18:40', mp3='candyman_19_cue_2b_piano'),  # break
    Play(time='18:45', mp3='siren', volume=0.5),  # job
    Play(time='19:30', mp3='Zivert - Life'),  # break

    # Тест
    Play(time='19:08', mp3='siren', volume=0.2),  # job
))
