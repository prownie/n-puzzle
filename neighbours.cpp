#include "neighbours.hpp"

Neighbours::Neighbours(int size): _size(size) {
	createGraphOfNeighbours();
}

Neighbours::~Neighbours() {

}

void	Neighbours::createGraphOfNeighbours() {
	for (int i = 0; i < _size * _size; i++) {
		vector<int> neighbours;
		if (i/_size > 0)//up neighbour
			neighbours.push_back(i - _size);
		if (i % _size != 0)//left neighbour
			neighbours.push_back(i-1);
		if ((i + 1) % _size != 0)//right neighbour
			neighbours.push_back(i+1);
		if ((i + _size) < _size * _size) // bottom neighbour
			neighbours.push_back(i + _size);
		_neighbourMapIndexes.insert(make_pair(i,neighbours));
	}
}

const vector<int>& Neighbours::getNeighbours(int id) const {
	map<int, vector<int> >::const_iterator it(_neighbourMapIndexes.find(id));
	if (it != _neighbourMapIndexes.end())
		return it->second;
	static vector<int> v;
	return v;
}
