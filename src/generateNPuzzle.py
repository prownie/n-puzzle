#!/usr/bin/python
import sys, random, argparse
from math import sqrt 

#Swap elements function
def swapElements(list, pos1, pos2):
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list



def isSolvable(list, args):
    goal = generateGoal(list)
    inversions = 0
    for i in range(len(list)):
        index_i = goal.index(list[i])
        for j in range(i+1, len(list)):
            index_j = goal.index(list[j])
            if index_i > index_j and list[i] != 0 and list[j] != 0:
                inversions += 1
    # print("Number of inversions = " + str(inversions))
    if inversions % 2 == 0:
        return True
    else:
        return False

def isListSolvable(list):
    goal = generateGoal(list)
    inversions = 0
    for i in range(len(list)):
        index_i = goal.index(list[i])
        for j in range(i+1, len(list)):
            index_j = goal.index(list[j])
            if index_i > index_j and list[i] != 0 and list[j] != 0:
                inversions += 1
    # print("Number of inversions = " + str(inversions))
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