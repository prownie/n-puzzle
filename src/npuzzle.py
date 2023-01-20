import sys, argparse, heapq
from parser import parseArguments
from generateNPuzzle import generateGoal
from aStar import aStar
# from printAnswer import printResult
from printAnswer import ResultPrinter
if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog='Npuzzle Solver')
	parser.add_argument("input", type=str, help="input puzzle file, or specify a size if you want a random generated puzzle")
	parser.add_argument("-s", "--solvable", action="store_true", default=False, help="Forces generation of a solvable puzzle. Overrides -u.")
	parser.add_argument("-u", "--unsolvable", action="store_true", default=False, help="Forces generation of an unsolvable puzzle")
	parser.add_argument("-MD", "--ManhattanDistance", action="store_true", default=True, help="Use ManhattanDistance heuristic")
	parser.add_argument("-MDLC", "--ManhattanDistanceLinearConflict", action="store_true", default=False, help="Use ManhattanDistance heuristic coupled with Linear Conflict")
	parser.add_argument("-MT", "--MisplacedTiles", action="store_true", default=False, help="Use MisplacedTiles heuristic")
	args = parser.parse_args()

	# goal and puzzleParsed are stored as Tuples, to be usable in dictionnary
	puzzleParsed = parseArguments(args)
	goal = generateGoal(puzzleParsed)
	# goal = (1,2,3,4,5,6,7,8,0)
	
	path = aStar(puzzleParsed, goal, "ManhattanDistance")
	for toto in path:
		print(toto)
	# printResult(path)
	ResultPrinter(path)
