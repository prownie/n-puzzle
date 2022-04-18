#!/usr/bin/python
import sys, random, argparse

#Swap elements function
def swapElements(list, pos1, pos2):
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list

#check if puzzle is solvable
def isSolvable(list):
	inversions = 0
	for i in range(args.size*args.size-1):
		for j in range(i+1,args.size*args.size):
			if list[i] > list[j]:
				inversions +=1
	if inversions % 2 == 0:
		return True
	else:
		return False

#parser
parser =argparse.ArgumentParser()
parser.add_argument("size", type=int, help="size of the square, smaller than 100, but greater than 3")
parser.add_argument("-s","--solvable", action="store_true", default=False, help="generate puzzle which can be resolved ")
parser.add_argument("-us","--unsolvable", action="store_true", default=False, help="generate puzzle which can't be resolved")
args = parser.parse_args()

if args.solvable and args.unsolvable:
	print("I can't make a Schrodinger puzzle . .")
	exit()
if args.size < 3 or args.size > 100:
	print("Wrong size parameter")
	exit()

#initialize the NPuzzle
puzzle = list(range(0,args.size*args.size))
for i in range(1000):
		puzzle = swapElements(puzzle, random.randint(0,args.size*args.size-1), random.randint(0,args.size*args.size-1))
if args.unsolvable:
	while isSolvable(puzzle):
		puzzle = swapElements(puzzle, random.randint(0,args.size*args.size-1), random.randint(0,args.size*args.size-1))
if args.solvable:
	while not isSolvable(puzzle):
		puzzle = swapElements(puzzle, random.randint(0,args.size*args.size-1), random.randint(0,args.size*args.size-1))

with open(str(args.size)+"-puzzle.txt", "w") as f:
	for i in range(args.size*args.size):
			if (i+1)%args.size==0 and i!=args.size*args.size-1:
				f.write("%s \n" % puzzle[i])
			else:
				f.write("%s " % puzzle[i])


if isSolvable(puzzle):
	print("This puzzle is solvable")
else:
	print("This puzzle is not solvable")
f.close()

#open and read the file after the appending:
f = open(str(args.size)+"-puzzle.txt", "r")
print(f.read())
