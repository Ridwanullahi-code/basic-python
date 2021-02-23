# write a python program to print out a set containing all colors
# from color_list_1 which are not present in color_list_2
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
for color in color_list_1:
	if color not in color_list_2:
		print(color)


