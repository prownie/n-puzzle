from math import sqrt
import time
import heapq
from heuristics import manhattanDistance,manhattanDistanceLinearConflict,misplacedTiles

def cellMovement(cell, drow, dcol, size):
    newCell = list(cell)
    for i, value in enumerate(newCell):
        if value == 0:
            # Déplacer la cellule vide vers le haut ou vers le bas
            if drow != 0:
                if i+drow*size >= 0 and i+drow*size<size*size:
                    newCell[i], newCell[i - size] = newCell[i - size], newCell[i]
                    return tuple(newCell)
            # Déplacer la cellule vide vers la gauche ou vers la droite
            elif (dcol == -1 and i % size > 0) or (dcol == 1 and i % size < size - 1):
                newCell[i], newCell[i + dcol] = newCell[i + dcol], newCell[i]
                return tuple(newCell)
    return tuple(newCell)

def aStar(grid, goal, heuristic):
	start_time = time.perf_counter()
	size = int(sqrt(len(grid)))
	# tuple of tile : (totalcost, cost, current, parrent)
	# totalcost: total cost of nodes, moves + heuristic
	# cost: moves used to reach this node
	# current: current grid
	# parrent: parent grid
	DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
	opened = [(0,0,grid,None)]
	heapq.heapify(opened)
	closed = {grid: None} #closed grid linked to parent
	match heuristic:
		case "ManhattanDistance":
			heuristicFunction = manhattanDistance
		case "ManhattanDistanceLinearConflict":
			heuristicFunction = manhattanDistanceLinearConflict
		case "MisplacedTiles":
			heuristicFunction = misplacedTiles
		case _:
			print("no heuristic chosen")

	total_time = 0
	while(opened != []):
		_, moves, cell, parent = heapq.heappop(opened)

    # afficher le temps total d'exécution en secondes
		if (cell == goal):
			print("FOUND")
			reversedPath = [cell]
			cell = parent
			while cell is not None:
				reversedPath.append(cell)
				cell = closed[cell]
			end_time = time.perf_counter()
			# ajouter le temps d'exécution de cette itération à la variable total_time
			total_time += end_time - start_time
			print(f"Temps total d'exécution de la ligne de code spécifique : {total_time:.6f} secondes")
			return reversed(reversedPath)
		print("Hello")
		for drow, dcol in DIRECTIONS:
			print("drow:", drow)
			print("dcol:", dcol)
			newCell = cellMovement(cell,drow,dcol,size)
			if newCell in closed or newCell == cell:
				continue
			heuristicCost = heuristicFunction(newCell,goal,size) 
			# print("potential new cell: ", newCell," with a cost of: ", heuristicCost, " and cell is :", cell)
			heapq.heappush(opened,(moves+heuristicCost,moves+1,newCell,cell))
			closed[cell] = parent
	# print(len(opened))
	print("Aster failed for whateverReason")
	return None
