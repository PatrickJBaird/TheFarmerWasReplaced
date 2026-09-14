from __builtins__ import *

DRONE_COUNT = 4

# Shared companion list
# [x, y, crop]
companion_map = []


# ==========================
# Companion Functions
# ==========================

def add_companion(x, y, crop):

	for comp in companion_map:

		if comp[0] == x and comp[1] == y:
			comp[2] = crop
			return

	companion_map.append(
		[x, y, crop]
	)


def get_companion_crop(x, y):

	for comp in companion_map:

		if comp[0] == x and comp[1] == y:
			return comp[2]

	return None


def update_companion_request():

	entity = get_entity_type()

	if entity != Entities.Carrot:
		return

	result = get_companion()

	if result == None:
		return

	crop = result[0]

	tx = result[1][0]
	ty = result[1][1]

	add_companion(
		tx,
		ty,
		crop
	)


# ==========================
# Crop Care
# ==========================

def water_crop():

	if num_items(Items.Water) > 0:

		if get_water() < 0.5:
			use_item(Items.Water)


def fertilize_crop():

	if num_items(Items.Fertilizer) > 0:

		if not can_harvest():
			use_item(Items.Fertilizer)


# ==========================
# Planting Logic
# ==========================

def plant_tile():

	x = get_pos_x()
	y = get_pos_y()

	companion_crop = get_companion_crop(
		x,
		y
	)

	if get_ground_type() != Grounds.Soil:
		till()

	if companion_crop != None:

		plant(companion_crop)

	else:

		plant(Entities.Carrot)


# ==========================
# Tile Processing
# ==========================

def work_tile():

	update_companion_request()

	if can_harvest():
		harvest()

	if get_entity_type() == None:
		plant_tile()

	water_crop()
	#fertilize_crop()


# ==========================
# Column Assignment
# ==========================

def drone_columns(drone_id, size):

	start_col = (
		size * drone_id
	) // DRONE_COUNT

	end_col = (
		size * (drone_id + 1)
	) // DRONE_COUNT

	return start_col, end_col


# ==========================
# Positioning
# ==========================

def move_to_column(target):

	while get_pos_x() < target:
		move(East)

	while get_pos_x() > target:
		move(West)


def move_to_bottom():

	while get_pos_y() > 0:
		move(South)


# ==========================
# Worker
# ==========================

def run_worker(drone_id):

	world = get_world_size()

	start_col, end_col = drone_columns(
		drone_id,
		world
	)

	move_to_column(start_col)
	move_to_bottom()

	while True:

		for x in range(start_col, end_col):

			if x % 2 == 0:

				for y in range(world):

					work_tile()

					if y < world - 1:
						move(North)

			else:

				for y in range(
					world - 1,
					-1,
					-1
				):

					work_tile()

					if y > 0:
						move(South)

			if x < end_col - 1:
				move(East)

		# Return to beginning of strip

		while get_pos_x() > start_col:
			move(West)

		while get_pos_y() > 0:
			move(South)


# ==========================
# Launch Drones
# ==========================

def launch_farm():

	spawn_drone(run_worker, 1)
	spawn_drone(run_worker, 2)
	spawn_drone(run_worker, 3)

	run_worker(0)


# ==========================
# Start Farm
# ==========================

launch_farm()