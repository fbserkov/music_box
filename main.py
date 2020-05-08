from box import Box
my_box = Box(directory='/home/fedor/Music/')

my_box.add_triple(start='05:25:00')
my_box.add_triple(start='09:30:00')
my_box.add_triple(start='13:05:00')
my_box.add_triple(start='17:10:00')

# print(my_box)
my_box.start()
