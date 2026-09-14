from go_to import *
from maze_runner import *

def maze_farm():
	go_to(0,0)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance,48)
	run_maze()