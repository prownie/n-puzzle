import math
#Distance for each tile to goal placement

def manhattanDistance(grid, goal, size, memo={}):
    # Vérification de la présence du coût de Manhattan de la grille dans le dictionnaire de mémoïsation
    if grid in memo:
        return memo[grid]
    
    # Calcul du coût de Manhattan
    cost = 0
    goal_pos = [0] * (size*size)
    for i in range(size*size):
        goal_pos[goal[i]] = i
    for index in range(0, size * size):
        if (grid[index] == 0):
            continue
        row = index % size
        col = index // size
        goal_row, goal_col = goal_pos[grid[index]] % size, goal_pos[grid[index]] // size
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