from __builtins__ import *
from go_to import *

def plant_cactus_farm(width,height):
	for i in range(height):
		for j in range(width):
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
			move(East)
		move(North)

def sort_Farm_EveryTile(width,height,is_sorted):
	while is_sorted != True:
		is_sorted = True

		go_to(0,0)
		# Move smaller values left
		for y in range(height):
			for x in range(width -1):
				go_to(x,y)

				a = measure()
				b = measure(East)
				if a > b:
					swap(East)
					sorted = False

		# Move smaller values down
		for y in range(1,height):
			for x in range(width):
				go_to(x,y)

				a = measure()
				b = measure(South)
				if a < b:
					swap(South)
					is_sorted = False


def build_farm_map(width, height):
	farm = []

	for y in range(height):
		row = []

		for x in range(width):
			go_to(x, y)
			row.append(measure())

		farm.append(row)

	return farm


def horizontal_pass(farm, width, height):
	changed = False

	for y in range(height):
		for x in range(width - 1):

			if farm[y][x] > farm[y][x + 1]:

				go_to(x, y)
				swap(East)

				temp = farm[y][x]
				farm[y][x] = farm[y][x + 1]
				farm[y][x + 1] = temp

				changed = True

	return changed


def vertical_pass(farm, width, height):
	changed = False

	for y in range(1, height):
		for x in range(width):

			if farm[y][x] < farm[y - 1][x]:

				go_to(x, y)
				swap(South)

				temp = farm[y][x]
				farm[y][x] = farm[y - 1][x]
				farm[y - 1][x] = temp

				changed = True

	return changed


def sort_farm(width, height):

	farm = build_farm_map(width, height)

	changed = True

	while changed:

		changed = False

		if horizontal_pass(farm, width, height):
			changed = True

		if vertical_pass(farm, width, height):
			changed = True

	return farm


def run_Cactus_Farm():
	#for Testing
	set_world_size(9)

	height = get_world_size()
	width = get_world_size()

	go_to(0,0)
	plant_cactus_farm(width,height)
	sort_farm(width,height)
	go_to(0,0)
	harvest()