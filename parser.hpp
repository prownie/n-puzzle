#ifndef PARSER_HPP
#define PARSER_HPP
#include <exception>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iterator>
#include <iomanip>

using namespace std;
class Parser {
private:
	Parser();
	int** 			_grid;
	int**				_goal;
	vector<string>	_parsedgrid;
	int					_ac;
	string 			_filename;
	int					_rowCount;
	int					_size;
	Parser & operator=(Parser const & rhs);
	void				checkNumSpaceOnly();
	void				checkGrid();
	int					countNumbers(string const& str);
	void	printGrid(int** toDisplay);
	void	generateGoal();
public:
	Parser(int ac, char** av);
	~Parser();
	Parser(Parser const & src);
	int		getScore() const;
	int** getGrid() const;
	int		getSize() const;
};
#endif
