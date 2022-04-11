#include "node.hpp"

Node::Node(int** new_grid, int size) {
	if (!new_grid)
		throw Node::Bad_arg_number_exception();
	if (size <= 0)
		throw Node::Bad_size_arguments();
	/*	if	(_password.empty())
		throw Node::Empty_password_exception();*/
}

Node::~Node() {

}

Node & Node::operator=(Node const & rhs) {
	if (this == &rhs)
		return (*this);
	_grid = rhs._grid;
	_h_score = rhs._h_score;
	_parent = rhs._parent;
	_size = rhs._size;
	return (*this);
}

Node::Node(Node const & src) {
	_grid = src._grid;
	_h_score = src._h_score;
	_parent = src._parent;
	_size = src._size;
}

int		Node::getScore() const {return _h_score;}
int**	Node::getGrid() const {return _grid;}
int		Node::getSize() const { return _size;}

char const * Node::Bad_arg_number_exception::what( void ) const throw()
{
	return "Wrong arg number";
}

char const * Node::Bad_size_arguments::what( void ) const throw()
{
	return "Network data must be written with the format host:port:password";
}

std::ostream & operator<<(std::ostream & o, Node const & a)
{
	int size = a.getSize();
	int** grid = a.getGrid();
	o << "------Node------" << std::endl;
	for (int i=0;i<size;i++) {
		o << "| ";
		for (int j=0;j<size;j++) {
			o << grid[i][j] << "|";
			if (j < size)
				o << " ";
		}
		o << std::endl;
	}
	o << "Score: " << a.getScore() << std::endl;
	o << "----------------" << std::endl;
	return o;
}
