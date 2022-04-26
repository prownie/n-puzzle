#ifndef STATE_HPP
#define STATE_HPP
#include <exception>
#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>
#include "parser.hpp"

using namespace std;
class State {
private:
	State();
	int*	_grid;
	State* _parent;
	int 	_size;
	Parser* _parser;
public:
	State(int* new_grid, int size, Parser* parser);
	~State();
	State & operator=(State const & rhs);
	State(State const & src);
	int*	getGrid() const;
	int		getSize() const;
	int		indexEmptyTile() const;
	void	moveTile(int a, int b);
	int		getManhattanCost() const;
	int		getHammingCost() const;

	class Bad_arg_number_exception : public std::exception
	{
		virtual const char* what() const throw();
	};
	class Bad_size_arguments : public std::exception
	{
		virtual const char* what() const throw();
	};
};

std::ostream & operator<<(std::ostream& o, State const & b);
bool operator==(const State &a, const State &b);
bool operator!=(const State &a, const State &b);
#endif



/*

 0 1 2
 3 4 5
 6 7 8

0  1  2  3
4  5  6  7
8  9  10 11
12 13 14 15
*/
