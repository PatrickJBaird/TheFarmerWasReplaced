from go_to import *
from maze_runner import *

ws_left = num_items(Items.Weird_Substance)

while ws_left  >= 12:
	
	go_to(0,0)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance,12)
	run_maze()