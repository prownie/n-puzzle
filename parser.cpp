#include "parser.hpp"

Parser::Parser(int ac, char** av) : _ac(ac), _rowCount(0) {

	if (_ac != 2)
		throw invalid_argument("Wrong arg number, use ./npuzzle [Filename|SquareSize]");
	 _filename = string (av[1]);
	//2 case, either full filename, or number
	//first case : only a number
	ifstream file;
	string currentLine;
	if (_filename.find_first_not_of("0123456789") == string::npos) {
		stringstream ss;
		_size = stoi(_filename);
		ss << _size << "-puzzle.txt";
		file.open(ss.str());
		if (!file)
			throw invalid_argument("File '"+ss.str() + "' not found");
		else {
			while (getline(file, currentLine)) {
				if (currentLine.find_first_not_of(" \n") != string::npos) {
					_parsedgrid.push_back(currentLine+"\n");
					_rowCount++;
				}
			}
		}
	}
	else {
		file.open(_filename);
		if (!file)
			throw invalid_argument("File '"+_filename + "' not found");
		else {
			while (getline(file, currentLine)) {
				if (currentLine.find_first_not_of(" \n") != string::npos) {
					_parsedgrid.push_back(currentLine+"\n");
					_rowCount++;
				}
			}
			_size = _rowCount;
		}
	}
	checkNumSpaceOnly();
	checkGrid();
	generateGoal();
	printGrid(_grid);
	cout << "-------------" << endl;
	printGrid(_goal);
}

Parser::~Parser() {

}

void	Parser::printGrid(int** toDisplay) {
	int normalizeCout = 0;
	int max = _size * _size -1;
	while (max != 0) {
		max /= 10;
	normalizeCout++;
	}
	for (int i =0; i<_rowCount;i++) {
		for(int j=0;j<_rowCount;j++) {
			cout << setw(normalizeCout) << toDisplay[i][j] << "|";
		}
		cout << endl;
	}
}

void	Parser::generateGoal() {
	int lastNumber = 1;
	int up = 0,down = 0,left = 0,right = 0;
	while (lastNumber <= _size * _size) {
		for (int u = left; u < _size - right; u++)
			_goal[up][u] = lastNumber++;
		up++;
		for (int r = up; r < _size - down; r++)
			_goal[r][_size - right - 1] = lastNumber++;
		right++;
		for (int d = _size - right - 1; d >= left; d--)
			_goal[_size - down - 1][d] = lastNumber++;
		down++;
		for (int l = _size - down - 1; l >= up; l--)
			_goal[l][left] = lastNumber++;
		left++;
	}
	for (int i =0; i<_rowCount;i++) {
		for(int j=0;j<_rowCount;j++) {
			if (_goal[i][j] == _size * _size)
			_goal[i][j] = 0;
		}
	}
}

void	Parser::checkNumSpaceOnly() {
	vector<string>::iterator it;
	string::size_type index;
	for (it = _parsedgrid.begin(); it != _parsedgrid.end(); ++it) {
		index = it->find_first_not_of("0123456789 \n");
		if (index != string::npos) {
			cout << index << endl;
			throw invalid_argument("Non numeric/space char found.");
		}
	}
}

void	Parser::checkGrid() {
	_grid = new int*[_rowCount];
	_goal = new int*[_rowCount];
	int nbOfNumber =0;
	stringstream currentLine;
	for (int i =0;i < _rowCount ; i++) {
		nbOfNumber = countNumbers(_parsedgrid[i]);
		currentLine << _parsedgrid[i];
		if (nbOfNumber != _rowCount)
			throw invalid_argument("Not a square, wrong number of rows/columns");
		_grid[i] = new int[nbOfNumber];
		_goal[i] = new int[nbOfNumber];
		for (int j =0; j<nbOfNumber; j++) {
			currentLine >> _grid[i][j];
		}
	}
	if (_size != 0 && _rowCount != _size)
		throw invalid_argument("Wrong number of rows");
}

int	Parser::countNumbers(string const& str) {
	stringstream stream(str);
	return distance(istream_iterator<string>(stream), istream_iterator<string>());
}

Parser::Parser(Parser const & src) {
	_grid = src._grid;
	_ac = src._ac;
	_filename = src._filename;
}

// char const * Parser::File_not_found_exception::what( void ) const throw()
// {
// 	return "File '" + _size*_size-1 + "Puzzle.txt' not found";
// }
