#!/usr/bin/python
import sys, random, argparse
from math import sqrt 

#Swap elements function
def swapElements(list, pos1, pos2):
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list



# for(int i =0; i<len(puzzle);i++) {
#     int indexInGoal = indexOfNombreInGoal(puzzle[i])
#     if puzzle[i] == 0
#         continue;
#     for (int j = i+1<len(puzzle);j++) {
#         for (int z = indexInGoal; z>=0;z--) {
#             if(puzzle[z] == puzzle[j]){
#                 inversions++
#                 break;
#             }
#         }
#     }
# }


# #check if puzzle is solvable
# def isSolvable(list, args):
# 	inversions = 0
# 	for i in range(int(args.input)*int(args.input)-1):
# 		for j in range(i+1,int(args.input)*int(args.input)):
# 			if list[i] > list[j]:
# 				inversions +=1
# 	# print("Number of inversions = " + str(inversions))
# 	if inversions % 2 == 0:
# 		return True
# 	else:
# 		return False

# def isListSolvable(list):
# 	inversions = 0
# 	puzzleSize = int(sqrt(len(list)))
# 	for i in range(puzzleSize*puzzleSize-1):
# 		for j in range(i+1,puzzleSize*puzzleSize):
# 			if list[i] > list[j]:
# 				inversions +=1
# 	return inversions

def isSolvable(list, args):
	goal = (1,2,3,8,0,4,7,6,5)
	# print(goal)
	# list = (0,2,3,1,6,4,8,7,5)
	i = 0
	inversions = 0
	while i < len(list):
		indexInGoal = goal.index(list[i])
		if list[i] == 0:
			i += 1
			continue
		j = i + 1
		while j < len(list):
			z = indexInGoal
			if list[j] == 0:
				j += 1
				continue
			while z >= 0:
				if list[z] == 0:
					z -= 1
					continue
				if goal[z] == list[j]:
					inversions += 1
					break
				z -= 1
			# print("inversions = " + str(inversions))
			# print("list[i] = " + str(list[i]))
			j += 1
		i += 1
	if inversions % 2 == 0:
		return True
	else:
		return False

def isListSolvable(list):
	goal = (1,2,3,8,0,4,7,6,5)
	# print(goal)
	# list = (0,2,3,1,6,4,8,7,5)
	i = 0
	inversions = 0
	while i < len(list):
		indexInGoal = goal.index(list[i])
		if list[i] == 0:
			i += 1
			continue
		j = i + 1
		while j < len(list):
			z = indexInGoal
			if list[j] == 0:
				j += 1
				continue
			while z >= 0:
				if list[z] == 0:
					z -= 1
					continue
				if goal[z] == list[j]:
					inversions += 1
					break
				z -= 1
			# print("inversions = " + str(inversions))
			# print("list[i] = " + str(list[i]))
			j += 1
		i += 1
	print(list)
	print("Number of inversions = " + str(inversions))
	return inversions

		
#initialize the NPuzzle
def generatePuzzle(args):
	puzzle = list(range(0,int(args.input)*int(args.input)))
	for i in range(1000):
			puzzle = swapElements(puzzle, random.randint(0,int(args.input)*int(args.input)-1), random.randint(0,int(args.input)*int(args.input)-1))
	if args.unsolvable:
		while isSolvable(puzzle, args):
			puzzle = swapElements(puzzle, random.randint(0,int(args.input)*int(args.input)-1), random.randint(0,int(args.input)*int(args.input)-1))
	if args.solvable:
		while not isSolvable(puzzle, args):
			puzzle = swapElements(puzzle, random.randint(0,int(args.input)*int(args.input)-1), random.randint(0,int(args.input)*int(args.input)-1))

	with open(str(args.input)+"-puzzle.txt", "w") as f:
		for i in range(int(args.input)*int(args.input)):
				if (i+1)%int(args.input)==0 and i!=int(args.input)*int(args.input)-1:
					f.write("%s \n" % puzzle[i])
				else:
					f.write("%s " % puzzle[i])
	if isSolvable(puzzle, args):
		print("This puzzle is solvable")
	else:
		print("This puzzle is not solvable")
	f.close()

	#open and read the file after the appending:
	f = open(str(args.input)+"-puzzle.txt", "r")
	# print(f.read())

#generate the goal from a random grid of N size
def generateGoal(grid):
	lastNumber=1
	up = down = left = right = 0
	size = int(sqrt(len(grid)))
	goalGrid = []
	goal2DGrid = [ [0]*size for i in range(size)]
	while (lastNumber <= size*size):
		for u in range(left, size-right):
			goal2DGrid[up][u] = lastNumber
			lastNumber+=1
		up+=1
		for r in range(up, size-down):
			goal2DGrid[r][size-right-1] = lastNumber
			lastNumber+=1
		right+=1
		for d in range(size-right-1,left-1,-1):
			goal2DGrid[size-down-1][d] = lastNumber
			lastNumber+=1
		down+=1
		for l in range(size-down-1,up-1,-1):
			goal2DGrid[l][left] = lastNumber
			lastNumber+=1
		left+=1
	
	for line in goal2DGrid:
		for number in line:
			if number == size*size:
				number=0
			goalGrid.append(number)
	return tuple(goalGrid)

#parser
if __name__ == "__main__":
	parser =argparse.ArgumentParser()
	parser.add_argument("input", type=int, help="size of the square, smaller than 100, but greater than 3")
	parser.add_argument("-s","--solvable", action="store_true", default=False, help="generate puzzle which can be resolved ")
	parser.add_argument("-us","--unsolvable", action="store_true", default=False, help="generate puzzle which can't be resolved")
	args = parser.parse_args()

	if args.solvable and args.unsolvable:
		print("I can't make a Schrodinger puzzle . .")
		exit()
	if args.input < 3 or args.input > 100:
		print("Wrong size parameter")
		exit()
	generatePuzzle(args)