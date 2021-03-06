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
	int** 			_grid2d;
	int*				_grid;
	int**				_goal2d;
	int*				_goal;
	vector<string>	_parsedgrid;
	int					_ac;
	string 			_filename;
	int					_rowCount;
	int					_size;
	void				checkNumSpaceOnly();
	void				checkGrid();
	void				checkSolvability();
	int					countNumbers(string const& str);
	void	printGrid(int** toDisplay);
	void	generateGoal();

public:
	Parser & operator=(Parser const & rhs);
	Parser(int ac, char** av);
	~Parser();
	Parser(Parser const & src);
	int		getScore() const;
	int** getGrid() const;
	int		getSize() const;
	int		getIndexOfXInGoal(int x) const;
	int*	getGoal() const;
};
#endif
