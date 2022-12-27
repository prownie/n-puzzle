import sys, string, math, heapq
from generateNPuzzle import generatePuzzle, isListSolvable

def checkInputValidity(file):
	allowed = set(string.digits + ' ' + '\n')
	maxNumberSeen = 0
	#check for valid characters in file
	if (not(set(file) <= allowed)):
		print("input file should only contains digits and spaces")
		sys.exit(1)
	splittedLines = list(filter(None,file.split('\n')))
	parsedNumbers = []
	for line in splittedLines:
		for number in list(filter(None,line.split(' '))):
			if int(number) > maxNumberSeen:
				maxNumberSeen = int(number)
			parsedNumbers.append(int(number))
	NPuzzleSize = math.isqrt(len(parsedNumbers))
	#check if N * N puzzle
	if NPuzzleSize * NPuzzleSize != len(parsedNumbers):
		print("Wrong format file, it needs to have N lines of N numbers")
		sys.exit(1)
	for line in splittedLines:
		#if wrong number of numbers on non empty line
		if len(list(filter(None,line.split(' ')))) != NPuzzleSize and len(list(filter(None,line.split(' ')))) != 0:
			print("Wrong line detected, should have %s numbers, on line\n" % NPuzzleSize, line)
			sys.exit(1)
	setParsedNumbers = set(parsedNumbers)
	if maxNumberSeen >= NPuzzleSize*NPuzzleSize:
		print("Wrong number detecter, numbers should go from 1 to N*N-1, including a 0")
		sys.exit(1)
	if (len(setParsedNumbers) != len(parsedNumbers)):
		print("Bad puzzle input, Duplicate numbers found !")
		sys.exit(1)
	if (isListSolvable(parsedNumbers) % 2 != 0):
		print("Puzzle not solvable, %s iterations required (need to be even)" % isListSolvable(parsedNumbers))
		sys.exit(1)
	return tuple(parsedNumbers)

def parseArguments(args):
	if args.solvable and args.unsolvable:
		print ("Can't be both solvable AND unsolvable, you have to choose!")
		sys.exit(1)

	if (args.input.isdigit()):
		if int(args.input) < 3:
			print ("Can't generate a puzzle with size lower than 3. It says so in the help.")
			sys.exit(1)
		else:
			generatePuzzle(args)
			args.input = str(args.input)+"-puzzle.txt"
			
	# file = open(args.input)
	try:
		file = open(args.input)
		return checkInputValidity(file.read())
	except FileNotFoundError:
		print("Input file not found")
		sys.exit(1)