from math import sqrt
import heapq
from heuristics import manhattanDistance,manhattanDistanceLinearConflict,misplacedTiles

def cellMovement(cell, drow, dcol, size):
	newCell = list(cell)
	for i in range (0, len(newCell)):
		if newCell[i]==0:
			if drow !=0: #move up/down
				if i+drow*size >= 0 and i+drow*size<size*size: #move possible
					tmp = newCell[i+drow*size]
					newCell[i+drow*size] = 0
					newCell[i] = tmp
					break
			else: #move left/right
				if (dcol == -1 and  i % size > 0) or (dcol == 1 and i%size < size-1): #move possible
					tmp = newCell[i+dcol]
					newCell[i+dcol] = 0
					newCell[i] = tmp
					break
	return tuple(newCell)


def aStar(grid, goal, heuristic):
	size = int(sqrt(len(grid)))
	# tuple of tile : (totalcost, cost, current, parrent)
	# totalcost: total cost of nodes, moves + heuristic
	# cost: moves used to reach this node
	# current: current grid
	# parrent: parent grid
	DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
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

	while(opened != []):
		_, moves, cell, parent = heapq.heappop(opened)
		if (cell == goal):
			# print("FOUND")
			reversedPath = [cell]
			cell = parent
			while cell is not None:
				reversedPath.append(cell)
				cell = closed[cell]
			return reversed(reversedPath)
		for drow, dcol in DIRECTIONS:
			newCell = cellMovement(cell,drow,dcol,size)
			if newCell in closed:
				continue
			
			heuristicCost = heuristicFunction(newCell,goal,size) 
			# print("potential new cell: ", newCell," with a cost of: ", heuristicCost)
			heapq.heappush(opened,(moves+heuristicCost,moves+1,newCell,cell))

			closed[cell] = parent
	print("Aster failed for whateverReason")
