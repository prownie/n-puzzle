import math
#Distance for each tile to goal placement
def manhattanDistance(grid, goal, size, memo={}):
    # Vérification de la présence du coût de Manhattan de la grille dans le dictionnaire de mémoïsation
    if grid in memo:
        return memo[grid]
    
    # Précalcul des coordonnées de chaque tuile dans la grille goal
    goal_coords = {}
    for index in range(0, size * size):
        tile = goal[index]
        row = index // size
        col = index % size
        goal_coords[tile] = (row, col)
    
    # Calcul du coût de Manhattan
    cost = 0
    for index in range(0, size * size):
        if (grid[index] == 0):
            continue
        row = index // size
        col = index % size
        tile = grid[index]
        goal_row, goal_col = goal_coords[tile]
        cost += abs(goal_row - row) + abs(goal_col - col)
    
    # Ajout du coût de Manhattan de la grille au dictionnaire de mémoïsation
    memo[grid] = cost
    
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