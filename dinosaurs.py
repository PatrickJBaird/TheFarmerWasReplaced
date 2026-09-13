from go_to import *

go_to(0,0)
change_hat(Hats.Dinosaur_Hat)

width = get_world_size() - 1
height = get_world_size() - 1

cant_move = False
e = True
n = True


while cant_move == False:
			while e:
				move(East)
				if get_pos_x() == width:
					e = False
				elif get_pos_x() == 0:
					e = True
			if n:
				move(North)
				if get_pos_y() == height:
					n = False
				elif get_pos_y() == 0:
					n = True
			elif n == False:
				move(South)
				if get_pos_y() == height:
					n = False
				elif get_pos_y() == 0:
					n = True
			while e == False:
				move(West)
				if get_pos_x() == width:
					e = False
				elif get_pos_x() == 0:
					e = True
			if n:
				move(North)
				if get_pos_y() == height:
					n = False
				elif get_pos_y() == 0:
					n = True
			elif n == False:
				move(South)
				if get_pos_y() == height:
					n = False
				elif get_pos_y() == 0:
					n = True
			

	

if cant_move == True:
	change_hat(Hats.Purple_Hat)