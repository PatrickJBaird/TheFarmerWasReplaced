from __builtins__ import *

#set number of drones
DRONE_COUNT = 4

#water Crops
def water_crop():

	if num_items(Items.Water) > 0:

		if get_water() < 0.5:
			use_item(Items.Water)

#fertilize crops
def fertilize_crop():

	if num_items(Items.Fertilizer) > 0:

		if not can_harvest():
			use_item(Items.Fertilizer)


#farm the current tile
def work_tile():

	if can_harvest():
		harvest()

	entity = get_entity_type()

	if entity == None or entity == Entities.Grass:
		plant(Entities.Grass)

	water_crop()
	#fertilize_crop()


#assign drone to specific area
def drone_columns(drone_id, world):

	start_col = (
		world * drone_id
	) // DRONE_COUNT

	end_col = (
		world * (drone_id + 1)
	) // DRONE_COUNT

	return start_col, end_col


#position drone to starting point
def move_to_column(target):

	while get_pos_x() < target:
		move(East)

	while get_pos_x() > target:
		move(West)

#move to bottom row
def move_to_bottom():

	while get_pos_y() > 0:
		move(South)


#run dron functions
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

				# Travel North
				for y in range(world):

					work_tile()

					if y < world - 1:
						move(North)

			else:

				# Travel South
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

		# Return to start of strip

		while get_pos_x() > start_col:
			move(West)

		while get_pos_y() > 0:
			move(South)


#launch farm and spawn drones
def launch_farm():

	spawn_drone(run_worker, 1)
	spawn_drone(run_worker, 2)
	spawn_drone(run_worker, 3)

	# Main drone
	run_worker(0)

#start script
launch_farm()