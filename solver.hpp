#ifndef SOLVER_HPP
#define SOLVER_HPP
#include <exception>
#include <string>
#include <iostream>
#include "parser.hpp"

class Solver {
private:
	Solver();
	int** _grid;
	int		_ac;
	char** _av;
	Solver & operator=(Solver const & rhs);
	Solver(Solver const & src);
public:
	Solver(Parser original_grid);
	~Solver();
	int		getScore() const;
	int** getGrid() const;
	int		getSize() const;
	void	run();
	class Bad_arg_number_exception : public std::exception
	{
		virtual const char* what() const throw();
	};
	class Bad_size_arguments : public std::exception
	{
		virtual const char* what() const throw();
	};
};
#endif
