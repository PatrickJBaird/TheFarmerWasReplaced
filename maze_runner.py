from go_to import *

def run_maze_Wall_Follow():

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

def is_visited(visited, x, y):

	for pos in visited:

		if pos[0] == x and pos[1] == y:
			return True

	return False

def run_maze():
	directions = [[North, 0, 1],[East, 1, 0],[South, 0, -1],[West, -1, 0]]
	visited = []
	path = []
	treasure_found = get_entity_type()
	treasure_pos = measure()
	tx = treasure_pos[0]
	ty = treasure_pos[1]

	while treasure_found != Entities.Treasure:

		x = get_pos_x()
		y = get_pos_y()

		visited.append([x,y])

		best_dir = None
		best_score = 999999

		# Try unvisited neighbours first
		for direction, dx, dy in directions:

			nx = x + dx
			ny = y + dy

			if can_move(direction):

				if not is_visited(visited, nx, ny):

					score = abs(tx - nx) + abs(ty - ny)

					if score < best_score:
						best_score = score
						best_dir = direction

		if best_dir != None:

			path.append(best_dir)
			move(best_dir)

		else:

			# Backtrack
			if len(path) == 0:
				return

			last = path.pop()

			if last == North:
				move(South)

			elif last == South:
				move(North)

			elif last == East:
				move(West)

			else:
				move(East)		

		if get_entity_type() == Entities.Treasure:
			treasure_found = get_entity_type()
			harvest()