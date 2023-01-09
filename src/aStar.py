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
	size = int(sqrt(len(grid)))
	# tuple of tile : (totalcost, cost, current, parrent)
	# totalcost: total cost of nodes, moves + heuristic
	# cost: moves used to reach this node
	# current: current grid
	# parrent: parent grid
	DIRECTIONS = {(1, 0), (-1, 0), (0, 1), (0, -1)}
	opened = [(0,0,grid,None)]
	heapq.heapify(opened)
	hash_close = {} # définir hash_close comme un dictionnaire vide
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
	start_time = time.perf_counter()
	while(opened != []):
		# print("closed = ",len(hash_close))
		# print("opened = ",len(opened))
		_, moves, cell, parent = heapq.heappop(opened)
		if (cell == goal):
			print("FOUND")
			# 4.3 secondes pour un 4x4
			reversedPath = [cell]
			cell = parent
			while cell is not None:
				reversedPath.append(cell)
				cell = hash_close[cell] # utiliser hash_close au lieu de closed
			end_time = time.perf_counter()
			total_time += end_time - start_time
			print(f"Temps total d'exécution de la ligne de code spécifique : {total_time:.6f} secondes")
			return reversed(reversedPath)
		# print("Hello")
		for drow, dcol in DIRECTIONS:

			# start_time = time.perf_counter()

			newCell = cellMovement(cell,drow,dcol,size) # 2.36 secondes 4x4

			# end_time = time.perf_counter()
			# total_time += end_time - start_time
			# print(f"Temps total d'exécution de la ligne de code spécifique : {total_time:.6f} secondes")

			if newCell in hash_close or newCell == cell: # utiliser hash_close au lieu de closed
				continue

			# start_time = time.perf_counter()

			heuristicCost = heuristicFunction(newCell,goal,size) # 0.67 secondes 4x4

			# end_time = time.perf_counter()
			# total_time += end_time - start_time
			# print(f"Temps total d'exécution de la ligne de code spécifique : {total_time:.6f} secondes")
			heapq.heappush(opened,(moves+heuristicCost,moves+1,newCell,cell))
			hash_close[cell] = parent # utiliser hash_close au lieu de closed

	# ajouter le hash du "close" ici
	hash_close = hash(frozenset(hash_close.items())) # hasher les items du dictionnaire hash_close
	print("Aster failed for whateverReason")
	return None