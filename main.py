#importing all the built-in functions
from __builtins__ import *

#get the width and height of the farm
#Get size of world 
def farmSize():
	farm = get_world_size()
	height = farm
	width = farm
	return height, width

#harvest function
def collect():
	if can_harvest():
		harvest()

#Plant Hay, Bush, Wood, Carrot, Pumpkin Functions
def plant_Hay():
	#plant grass if there is no other plant on the square
	if get_entity_type() == None or get_entity_type() == Entities.Grass:
		plant(Entities.Grass)

def plant_Bush():
	plant(Entities.Bush)

def plant_Tree(x,y):
	#plant tree on odd coordinates if there is no pumpkin on the square
	if not is_even(x):
		if not is_even(y) and get_entity_type() != Entities.Pumpkin and get_entity_type() != Entities.Sunflower and get_entity_type() != Entities.Cactus:
			plant(Entities.Tree)

def plant_Carrot(x,y):
	#plant carrot on first 2 even y coordinates if there is no tree or pumpkin on the square
	if get_entity_type() != Entities.Tree and get_entity_type() != Entities.Pumpkin and get_entity_type() != Entities.Sunflower:
					if is_even(y) and y <= 3:
						if get_ground_type() != Grounds.Soil:
							till()
						plant(Entities.Carrot)

def plant_Pumpkin(x, y):
	#plant pumpkin 3x3 area at top right of farm
	if y > (height - 6):
					if x > (width - 6):						
						if get_ground_type() != Grounds.Soil:
							till()
						plant(Entities.Pumpkin)

def plant_Sunflower(x,y):
	if x % 3 == 0 and y % 3 == 0:
		if get_entity_type() != Entities.Pumpkin and x <= (width - 5) and y <= (height - 5):
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Sunflower)

def plant_Cactus(x,y):
	if x <= (2) and y > (height - 4):
		if get_entity_type() != Entities.Pumpkin and get_entity_type() != Entities.Sunflower:
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)
	if x >= 4 and x <= 7 and y > (height - 4):
			if get_entity_type() != Entities.Pumpkin and get_entity_type() != Entities.Sunflower:
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Cactus)

#sorts cactus by measuring and swapping 
def sort_CactusA(x,y):
	
	#move drone to starting position
	move_to_start(x,y)

	#move drone to first cactus row
	while y != height -1:
		move(North)
		y = get_pos_y()

	#Sort cactie with larger to the north and east of smaller	
	sort_Cactus_r()
	move(South)
	sort_Cactus_r()
	move(South)
	sort_Cactus_r()
	move(North)
	move(North)
	sort_Cactus_c()
	move(East)
	sort_Cactus_c()
	move(East)
	sort_Cactus_c()

#sorts cactus by measuring and swapping 
def sort_CactusB(x,y):
	
	#move drone to starting position
	move_to_start(x,y)

	#move drone to first cactus row
	while y != height -1:
		move(North)
		y = get_pos_y()
	while x != 4:
		move(East)
		x = get_pos_x()

	#Sort cactie with larger to the north and east of smaller	
	sort_Cactus_r()
	move(South)
	sort_Cactus_r()
	move(South)
	sort_Cactus_r()
	move(North)
	move(North)
	sort_Cactus_c()
	move(East)
	sort_Cactus_c()
	move(East)
	sort_Cactus_c()

#sort cactus column
def sort_Cactus_r():
	sort_Cactus_e()
	move(East)
	sort_Cactus_e()
	move(West)
	sort_Cactus_e()

#sort Cactus row
def sort_Cactus_c():
	sort_Cactus_s()
	move(South)
	sort_Cactus_s()
	move(North)
	sort_Cactus_s()

#sort cactus to the east
def sort_Cactus_e():
	if get_entity_type() == Entities.Cactus:
			a = measure()
			b = measure(East)
			if b < a and b != None: # type: ignore
				swap(East)

#sort Cactus to teh south
def sort_Cactus_s():
	if get_entity_type() == Entities.Cactus:
			a = measure()
			b = measure(South)
			if b > a and b != None: # type: ignore
				swap(South)

#Check if number is even
def is_even(n):
	return n % 2 == 0

#Water the crops if they are not ready to harvest
def water_Crops():
	if num_items(Items.Water) > 0:
		if not can_harvest():
			if get_water() < 0.5:
				use_item(Items.Water)

#Fertilize the crops if they are not ready for harvest
def fertilize_Crops():
	if num_items(Items.Fertilizer) > 0:
		if not can_harvest():
				use_item(Items.Fertilizer)

#get the current position of the drone
def get_pos():
	return (get_pos_x(), get_pos_y())

#world traversal function
def traverse(width, height):
	for x in range(width):
		for y in range(height):
			move(North)

			#get the current position of the drone
			x, y = get_pos()

			#Harvesting the crops if they are ready to harvest
			collect()

			#Planting pumpkins on top 4 squares of farm
			plant_Pumpkin(x, y)

			#Planting sunflowers
			plant_Sunflower(x, y)

			#Planting Cactus
			plant_Cactus(x, y)
			
			#Planting Trees on odd coordinates
			plant_Tree(x, y)

			#Planting Carrots 
			plant_Carrot(x, y)
			
			#Planting Grass if no Tree or Carrot is planted
			plant_Hay()

			#Watering the crops
			water_Crops()
			if x % 3 == 0 and y % 3 == 0:
				#Fertilizing the crops
				fertilize_Crops()
		move(East)
	x, y = get_pos()
	sort_CactusA(x,y)
	sort_CactusB(x,y)

#move drone to starting position
def move_to_start(x,y):
	while x != 0:
		move(West)
		x = get_pos_x()
		
	while y != 0:
		move(South)
		y = get_pos_y()

while True:
	x,y = get_pos()
	move_to_start(x,y)
	height, width = farmSize()
	traverse(width, height)