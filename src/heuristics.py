import math
#Distance for each tile to goal placement
def manhattanDistance(grid, goal, size):
	cost = 0
	for index in range(0,size*size):
		if (grid[index] == 0):
			continue
		for indexGoal in range(0,size*size):
			if goal[indexGoal]==grid[index]:
				cost += abs(int(indexGoal/size)-int(index/size))+abs(int(indexGoal%size)-int(index%size))
				break
	# print(cost)
	return cost

def manhattanDistanceLinearConflict(grid, goal, size):
	cost = 0
	for index in range(0,size*size):
		if (grid[index] == 0):
			continue
		for indexGoal in range(0,size*size):
			if goal[indexGoal]==grid[index]:
				cost += abs(int(indexGoal/size)-int(index/size))+abs(int(indexGoal%size)-int(index%size))
				if (indexGoal != index and (int(indexGoal/size)==int(index/size) or int(indexGoal%size)==int(index%size))):
					cost+=1
				break
	# print(cost)
	return cost

def misplacedTiles(grid, goal, size):
	cost = 0
	for index in range(0, size*size):
		if (grid[index] == 0):
			continue
		if grid[index] != goal[index]:
			cost+=1
	# print(cost)
	return cost