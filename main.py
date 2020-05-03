from box import Box
my_box = Box(directory='/home/fedor/Music/')

# Пара 1  TODO Определять пару одной функцией
my_box.add_music(start='05:30:00')  # start
my_box.add_music(start='06:15:00')  # end
my_box.add_music(start='06:20:00')  # start
my_box.add_music(start='07:05:00')  # end

# Пара 2
my_box.add_music(start='08:35:00')  # start
my_box.add_music(start='09:20:00')  # end
my_box.add_music(start='09:25:00')  # start
my_box.add_music(start='10:10:00')  # end

# Пара 3
my_box.add_music(start='10:25:00')  # start
my_box.add_music(start='11:10:00')  # end
my_box.add_music(start='11:15:00')  # start
my_box.add_music(start='12:00:00')  # end

# Пара 4
my_box.add_music(start='13:00:00')  # start
my_box.add_music(start='13:45:00')  # end
my_box.add_music(start='13:50:00')  # start
my_box.add_music(start='14:35:00')  # end

# Пара 5
my_box.add_music(start='14:50:00')  # start
my_box.add_music(start='15:35:00')  # end
my_box.add_music(start='15:40:00')  # start
my_box.add_music(start='16:25:00')  # end

# Пара 6
my_box.add_music(start='17:55:00')  # start
my_box.add_music(start='18:40:00')  # end
my_box.add_music(start='18:45:00')  # start
my_box.add_music(start='19:30:00')  # end

print(my_box)
my_box.start()
