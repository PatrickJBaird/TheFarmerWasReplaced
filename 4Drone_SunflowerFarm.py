from __builtins__ import *

DRONE_COUNT = 4


# =====================
# Crop Care
# =====================

def water_crop():

	if num_items(Items.Water) > 0:

		if get_water() < 0.75:
			use_item(Items.Water)


def fertilize_crop():

	if num_items(Items.Fertilizer) > 0:

		if not can_harvest():
			use_item(Items.Fertilizer)


# =====================
# Tile Logic
# =====================

def work_tile():

	entity = get_entity_type()

	if can_harvest():
		harvest()
		entity = None

	if get_ground_type() != Grounds.Soil:
		till()

	if entity == None:
		plant(Entities.Sunflower)

	water_crop()
	#fertilize_crop()


# =====================
# Column Assignment
# =====================

def drone_columns(drone_id, world):

	start_col = (
		world * drone_id
	) // DRONE_COUNT

	end_col = (
		world * (drone_id + 1)
	) // DRONE_COUNT

	return start_col, end_col


# =====================
# Initial Positioning
# =====================

def move_to_column(target):

	while get_pos_x() < target:
		move(East)

	while get_pos_x() > target:
		move(West)


def move_to_bottom():

	while get_pos_y() > 0:
		move(South)


# =====================
# Worker
# =====================

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

		# Return to strip origin

		while get_pos_x() > start_col:
			move(West)

		while get_pos_y() > 0:
			move(South)


# =====================
# Launch Drones
# =====================

def launch_farm():

	spawn_drone(run_worker, 1)
	spawn_drone(run_worker, 2)
	spawn_drone(run_worker, 3)

	run_worker(0)


launch_farm()