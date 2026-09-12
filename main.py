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
	if y > (height - 5):
					if x > (width - 5):						
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
	if x < (width - 4) and y > (height - 4):
		if get_entity_type() != Entities.Pumpkin and get_entity_type() != Entities.Sunflower:
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Cactus)

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

while True:
	height, width = farmSize()
	traverse(width, height)