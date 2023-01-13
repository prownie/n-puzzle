from math import sqrt
import time
import heapq
from heuristics import manhattanDistance,manhattanDistanceLinearConflict,misplacedTiles


# je veux cree une fonction qui va me donner la liste des voisins d'un cell avec cell, drow, dcol, size
# def cellMovement(cell, drow, dcol, size):
#  je veux que cette fonction soit optimiser et me retourne un tuple(newCell)

# def cellMovement(cell, drow, dcol, size):
#     newCell = list(cell)
#     for i, value in enumerate(newCell):
#         if value == 0:
#             # Déplacer la cellule vide vers le haut ou vers le bas
#             if drow != 0:
#                 if i+drow*size >= 0 and i+drow*size<size*size:
#                     newCell[i], newCell[i - size] = newCell[i - size], newCell[i]
#                     return tuple(newCell)
#             # Déplacer la cellule vide vers la gauche ou vers la droite
#             elif (dcol == -1 and i % size > 0) or (dcol == 1 and i % size < size - 1):
#                 newCell[i], newCell[i + dcol] = newCell[i + dcol], newCell[i]
#                 return tuple(newCell)
#     return tuple(newCell)

# def cellMovement(cell, drow, dcol, size):
# 	newCell = list(cell)
# 	index = newCell.index(0)
# 	newIndex = index + drow * size + dcol
# 	# print("cell = ",cell)
# 	# print("index = ",index)
# 	# print("newIndex = ",newIndex)
# 	# print("drow = ",drow)
# 	# print("dcol = ",dcol)
# 	if drow != 0:
# 		if newIndex >= 0 and newIndex<size*size:
			# print("cell = ",cell)
			# print("index = ",index)
			# print("newIndex = ",newIndex)
			# print("drow = ",drow)
			# print("dcol = ",dcol)
			# print("newIndex = ",newIndex)
			# print("newCell[newIndex] = ",newCell[newIndex])
			# print("\n")
# 			print("index - size = ",index - size)
# 			print("newCell[index - size] = ",newCell[index - size])
# 			print("\n\n\n\n")
# 			newCell[index], newCell[index - size] = newCell[index - size], newCell[index]
# 			return tuple(newCell)
# 	elif (dcol == -1 and index % size != 0) or (dcol == 1 and (index + 1) % size != 0):
# 		# print("\n\n\n\n")
# 		newCell[index], newCell[newIndex] = newCell[newIndex], newCell[index]
# 		return tuple(newCell)
# 	# print("\n\n\n\n")
# 	return tuple(newCell)

def cellMovement(cell, drow, dcol, size):
	newCell = list(cell)
	index = newCell.index(0)
	newIndex = index + drow * size + dcol
	if (drow != 0 and newIndex >= 0 and newIndex < size * size) or (dcol != 0 and (dcol == -1 and index % size != 0) or (dcol == 1 and (index + 1) % size != 0)):
	# if (newIndex <= size * size - 1 and newIndex >= 0):
		# print("drow = ",drow)
		# print("dcol = ",dcol)
		# print("newIndex = ",newIndex)
		# print("\n")
		# print("cell = ",cell)
		newCell[index], newCell[newIndex] = newCell[newIndex], newCell[index]
		# print("newCell = ",newCell)
		# print ("newCell = ",newCell)

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
		# si c'est un modulo de 100000
		# if (len(opened) % 100000 == 0):
		# 	print("closed = ",len(opened))
		_, moves, cell, parent = heapq.heappop(opened)
		# if (len(opened) < 100):
		# 	print("opened = ",opened)
		if (cell == goal):
			print("FOUND")
			# 0.055 secondes pour un 4x4
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
		# print("\n\n")
		# print("cell = ",cell)
		for drow, dcol in DIRECTIONS:
			# print ("drow = ",drow)
			# print ("dcol = ",dcol)
			# start_time = time.perf_counter()

			newCell = cellMovement(cell,drow,dcol,size) # 1.75 secondes 4x4

			# end_time = time.perf_counter()
			# total_time += end_time - start_time
			# print(f"Temps total d'exécution de la ligne de code spécifique : {total_time:.6f} secondes")

			if  newCell == cell or newCell in hash_close: # utiliser hash_close au lieu de closed
				# print("continue")
				continue
			# else :

				# start_time = time.perf_counter()

			heuristicCost = heuristicFunction(newCell,goal,size) # 0.67 secondes 4x4
				# end_time = time.perf_counter()
				# total_time += end_time - start_time
				# print(f"Temps total d'exécution de la ligne de code spécifique : {total_time:.6f} secondes")

			heapq.heappush(opened,(moves+heuristicCost,moves+1,newCell,cell))
		hash_close[cell] = parent # utiliser hash_close au lieu de closed

	# ajouter le hash du "close" ici
	print(len(hash_close))
	hash_close = hash(frozenset(hash_close.items())) # hasher les items du dictionnaire hash_close
	print("Aster failed for whateverReason")
	return None