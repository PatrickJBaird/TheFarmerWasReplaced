from go_to import *

def run_maze():

	treasure_located = get_entity_type()

	directions = [North, East, South, West]
	index = 0

	while treasure_located != Entities.Treasure:

		if can_move(directions[index]):
			move(directions[index])
			#turn left
			index = (index - 1) % 4
		else:
			move(directions[index])
			#turn right
			index = (index + 1) % 4
		
		treasure_located = get_entity_type()

	if treasure_located == Entities.Treasure:
		harvest()