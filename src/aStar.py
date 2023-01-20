from math import sqrt
import time
import heapq
from heuristics import manhattanDistance,manhattanDistanceLinearConflict,misplacedTiles

def cellMovement(cell, drow, dcol, size):
	newCell = list(cell)
	index = newCell.index(0)
	newIndex = index + drow * size + dcol
	if (drow != 0 and newIndex >= 0 and newIndex < size * size) or (dcol != 0 and (dcol == -1 and index % size != 0) or (dcol == 1 and (index + 1) % size != 0)):
		newCell[index], newCell[newIndex] = newCell[newIndex], newCell[index]

		return tuple(newCell)
	return tuple(newCell)


def aStar(grid, goal, heuristic):
	size = int(sqrt(len(grid)))
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
	print(goal)
	while(opened != []):
		_, moves, cell, parent = heapq.heappop(opened)
		if (cell == goal):
			reversedPath = [cell]
			cell = parent
			while cell is not None:
				reversedPath.append(cell)
				cell = hash_close[cell]
			end_time = time.perf_counter()
			total_time += end_time - start_time
			print(f"Temps total d'exécution de la ligne de code spécifique : {total_time:.6f} secondes")
			return list(reversed(reversedPath))
		for drow, dcol in DIRECTIONS:
			newCell = cellMovement(cell,drow,dcol,size)

			if  newCell == cell or newCell in hash_close:
				continue
			heuristicCost = heuristicFunction(newCell,goal,size)

			heapq.heappush(opened,(moves+heuristicCost,moves+1,newCell,cell))
		hash_close[cell] = parent

	print("Aster failed for whateverReason")
	return None