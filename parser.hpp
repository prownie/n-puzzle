#ifndef PARSER_HPP
#define PARSER_HPP
#include <exception>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <stdio.h>
class Parser {
private:
	Parser();
	int** 			_grid;
	int					_ac;
	std::string _filename;
	int					_size;
	Parser & operator=(Parser const & rhs);

public:
	Parser(int ac, char** av);
	~Parser();
	Parser(Parser const & src);
	int		getScore() const;
	int** getGrid() const;
	int		getSize() const;
	class Bad_arg_number_exception : public std::exception
	{
		virtual const char* what() const throw();
	};
};
#endif
