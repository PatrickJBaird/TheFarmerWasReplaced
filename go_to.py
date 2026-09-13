from __builtins__ import *

tiles_to_move = 0

def go_to(x,y):
	current_x = get_pos_x()
	current_y = get_pos_y()

	travel_x(current_x,x)
	travel_y(current_y,y)    

def travel_y(current_y,y):

	tiles_to_move = current_y - y

	while tiles_to_move < 0:
		if can_move(North):
			move(North)
			tiles_to_move += 1
		else:
			break
		

	while tiles_to_move > 0:
		if can_move(South):
			move(South)
			tiles_to_move -= 1
		else:
			break

def travel_x(current_x,x):

	tiles_to_move = current_x - x

	while tiles_to_move < 0:
		if can_move(East):
			move(East)
			tiles_to_move += 1
		else:
			break

	while tiles_to_move > 0:
		if can_move(West):
			move(West)
			tiles_to_move -= 1
		else:
			break