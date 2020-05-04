from box import Box
my_box = Box(directory='/home/fedor/Music/')

my_box.add_couple(start='05:15:00')
my_box.add_couple(start='07:05:00')
my_box.add_couple(start='09:55:00')
my_box.add_couple(start='11:45:00')
my_box.add_couple(start='14:00:00')
my_box.add_couple(start='15:50:00')
my_box.add_couple(start='18:40:00')

print(my_box)
my_box.start()
