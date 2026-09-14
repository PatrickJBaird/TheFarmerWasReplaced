from __builtins__ import *
from go_to import *

companion_requests = []


# -----------------------
# Utilities
# -----------------------

def farm_size():
	size = get_world_size()
	return size, size


def move_to_start():

	while get_pos_x() > 0:
		move(West)

	while get_pos_y() > 0:
		move(South)


def is_even(n):
	return n % 2 == 0


# -----------------------
# Companion System
# -----------------------

def remember_companion():

	result = get_companion()

	if result == None:
		return

	plant_type, location = result

	tx = location[0]
	ty = location[1]

	for request in companion_requests:

		if request[0] == tx and request[1] == ty:
			return

	companion_requests.append(
		[tx, ty, plant_type]
	)


def plant_companion(x, y):

	for i in range(len(companion_requests)):

		request = companion_requests[i]

		if request[0] == x and request[1] == y:

			plant(request[2])

			companion_requests.pop(i)

			return True

	return False


# -----------------------
# Harvesting
# -----------------------

def collect():

	if can_harvest():

		harvest()

		remember_companion()


# -----------------------
# Crop Zones
# -----------------------

def plant_pumpkin(x, y, width, height):

	if x > width - 6 and y > height - 6:

		if get_ground_type() != Grounds.Soil:
			till()

		plant(Entities.Pumpkin)

		return True

	return False


def plant_sunflower(x, y, width, height):

	if x % 3 == 0 and y % 3 == 0:

		if x <= width - 5 and y <= height - 5:

			if get_ground_type() != Grounds.Soil:
				till()

			plant(Entities.Sunflower)

			return True

	return False


def plant_cactus(x, y, height):

	if y > height - 4:

		if x <= 2 or (4 <= x <= 7):

			if get_ground_type() != Grounds.Soil:
				till()

			plant(Entities.Cactus)

			return True

	return False


def plant_tree(x, y):

	if not is_even(x) and not is_even(y):

		entity = get_entity_type()

		if (
			entity != Entities.Pumpkin
			and entity != Entities.Sunflower
			and entity != Entities.Cactus
		):
			plant(Entities.Tree)

			return True

	return False


def plant_carrot(y):

	if y <= 3 and is_even(y):

		entity = get_entity_type()

		if (
			entity != Entities.Tree
			and entity != Entities.Pumpkin
			and entity != Entities.Sunflower
		):

			if get_ground_type() != Grounds.Soil:
				till()

			plant(Entities.Carrot)

			return True

	return False


def plant_hay():

	entity = get_entity_type()

	if (
		entity == None
		or entity == Entities.Grass
	):
		plant(Entities.Grass)


# -----------------------
# Crop Care
# -----------------------

def water_crop():

	if num_items(Items.Water) > 0:

		if not can_harvest():

			if get_water() < 0.5:
				use_item(Items.Water)


def fertilize_crop():

	if num_items(Items.Fertilizer) > 0:

		if not can_harvest():
			use_item(Items.Fertilizer)


# -----------------------
# Tile Logic
# -----------------------

def process_tile(x, y, width, height):

	collect()

	if plant_companion(x, y):
		return

	if plant_pumpkin(x, y, width, height):
		return

	if plant_cactus(x, y, height):
		return

	if plant_sunflower(x, y, width, height):
		return

	if plant_tree(x, y):
		return

	if plant_carrot(y):
		return

	plant_hay()

	water_crop()

	if x % 3 == 0 and y % 3 == 0:
		fertilize_crop()


# -----------------------
# Snake Traversal
# -----------------------

def traverse(width, height):

	for x in range(width):

		if is_even(x):

			for y in range(height):

				go_to(x, y)

				process_tile(
					x,
					y,
					width,
					height
				)

		else:

			for y in range(
				height - 1,
				-1,
				-1
			):

				go_to(x, y)

				process_tile(
					x,
					y,
					width,
					height
				)


# -----------------------
# Main Loop
# -----------------------

while True:

	move_to_start()

	width, height = farm_size()

	traverse(
		width,
		height
	)