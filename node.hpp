#ifndef NODE_HPP
#define NODE_HPP
#include <exception>
#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>

class Node {
private:
	Node();
	int** _grid;
	int		_h_score;
	Node* _parent;
	int 	_size;
public:
	Node(int** new_grid, int size);
	~Node();
	Node & operator=(Node const & rhs);
	Node(Node const & src);
	int		getScore() const;
	int** getGrid() const;
	int		getSize() const;
	class Bad_arg_number_exception : public std::exception
	{
		virtual const char* what() const throw();
	};
	class Bad_size_arguments : public std::exception
	{
		virtual const char* what() const throw();
	};
};

std::ostream & operator<<(std::ostream& o, Node const & b);

#endif
