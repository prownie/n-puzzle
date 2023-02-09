from math import sqrt
import time
import heapq
from heuristics import manhattanDistance,manhattanDistanceLinearConflict,misplacedTiles

def cellMovement(cell, drow, dcol, size):
	newCell = list(cell)
	index = newCell.index(0)
	newIndex = index + drow * size + dcol
	# if (newIndex >= 0 and newIndex < size * size) or (dcol != 0 and (dcol == -1 and index % size != 0) or (dcol == 1 and (index + 1) % size != 0)):
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
	timeInHeuristic = 0
	timeInCellMovement = 0
	timeInCheckClose = 0
	timeInHeapPush = 0
	timeInPop = 0
	total_time = 0
	timeInCheckCloseBeforeDirection = 0
	timeInAddToClose =0
	cpt = 0
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
			print("closed = ", len(hash_close))
			print("opened = ", len(opened))
			print("path len = ", len(reversedPath))
			print("time in heuristic = ",timeInHeuristic)
			print("time in cell movement = ",timeInCellMovement)
			print("time in check hash_close before directions = ",timeInCheckCloseBeforeDirection)
			print("time in check close = ",timeInCheckClose)
			
			print(f"time spent in heuristic : {timeInHeuristic/total_time*100:.2f} %")
			print(f"time spent in cell movement : {timeInCellMovement/total_time*100:.2f} %")
			return list(reversed(reversedPath))

		startCheckCloseBeforeDirection = time.perf_counter()
		if cell in hash_close:
			continue
		timeInCheckCloseBeforeDirection += time.perf_counter() - startCheckCloseBeforeDirection

		for drow, dcol in DIRECTIONS:

			startCellMovement = time.perf_counter()
			newCell = cellMovement(cell,drow,dcol,size)
			timeInCellMovement += time.perf_counter() - startCellMovement


			startCheckClose = time.perf_counter()
			if newCell == cell or newCell in hash_close:
				continue
			timeInCheckClose += time.perf_counter() - startCheckClose

			startHeuristic = time.perf_counter()
			heuristicCost = heuristicFunction(newCell,goal,size)
			timeInHeuristic += time.perf_counter() - startHeuristic
			
			heapq.heappush(opened,(moves+heuristicCost,moves+1,newCell,cell))

		hash_close[cell] = parent
	print("Aster failed for whateverReason")
	return None