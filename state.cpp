#include "state.hpp"

State::State(int* new_grid, int size, Parser* parser): _size(size), _parser(parser)  {
	if (!new_grid)
		throw State::Bad_arg_number_exception();
	if (size <= 0)
		throw State::Bad_size_arguments();
	_grid = new_grid;
}

State::~State() {

}

State & State::operator=(State const & rhs) {
	if (this == &rhs)
		return (*this);
	_grid = rhs._grid;
	_parent = rhs._parent;
	_size = rhs._size;
	_parser = rhs._parser;
	return (*this);
}

State::State(State const & src) {
	_grid = src._grid;
	_parent = src._parent;
	_size = src._size;
	_parser = src._parser;
}

int*	State::getGrid() const {return _grid;}
int		State::getSize() const { return _size;}
int		State::indexEmptyTile() const {
	for (int i = 0; i < _size * _size ; i++) {
		if (_grid[i] == 0)
			return i;
	}
	return _size * _size; //shouldn't happen
}
void	State::moveTile(int a, int b) {
	int tmp = _grid[a];
	_grid[a] = _grid[b];
	_grid[b] = tmp;
}

int		State::getManhattanCost()const {
	int manCost = 0;
	for (int  i = 0; i < _size * _size; i++) {
		int num = _grid[i];
		int indexNumGoal = _parser->getIndexOfXInGoal(num);
		if (num == 0)
			continue;
		manCost += abs(i / _size - indexNumGoal / _size) + abs(i % _size - indexNumGoal % _size);
	}
	return manCost;
}

int State::getHammingCost() const {
	int hamCost = 0;
	int* goal = _parser->getGoal();
	for (int i = 0; i < _size * _size; i++) {
		if (_grid[i] != goal[i])
			hamCost++;
	}
	return hamCost;
}

char const * State::Bad_arg_number_exception::what( void ) const throw()
{
	return "Wrong arg number";
}

char const * State::Bad_size_arguments::what( void ) const throw()
{
	return "Network data must be written with the format host:port:password";
}

std::ostream & operator<<(std::ostream & o, State const & a)
{
	int size = a.getSize();
	int* grid = a.getGrid();
	o << "------State------" << std::endl;
	for (int i = 0; i < size * size; i++)
		o << grid[i] << "|";
	o << endl;
	o << "Score: " << a.getManhattanCost() << std::endl;
	o << "----------------" << std::endl;
	return o;
}

bool operator==(const State &a, const State &b){
	if (memcmp(a.getGrid(), b.getGrid(), sizeof(a) / sizeof(int)) == 0)
		return true;
	else
		return false;
}

bool operator!=(const State &a, const State &b){
	if (memcmp(a.getGrid(), b.getGrid(), sizeof(a) / sizeof(int)) == 0)
		return false;
	else
		return true;
}
