#ifndef NEIGHBOURS_HPP
#define NEIGHBOURS_HPP
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;
class Neighbours {
private:
	Neighbours & operator=(Neighbours const & rhs);
	Neighbours(Neighbours const & src);
	map<int, vector<int> > _neighbourMapIndexes;
	const vector<int>& getNeighbours(int id) const;
	void	createGraphOfNeighbours();
	int		_size;
public:
	Neighbours(int size);
	~Neighbours();
};

std::ostream & operator<<(ostream& o, Neighbours const & b);
bool operator==(const Neighbours &a, const Neighbours &b);
bool operator!=(const Neighbours &a, const Neighbours &b);
#endif


/*
0  1  2  3
4  5  6  7
8  9  10 11
12 13 14 15

0: 1 4
1: 0 2 5
2: 1 3 6
3: 2 7
4: 0 5 8
5: 1 4 6 9
6: 2 5 7 10
7: 3 6 11
8:
9:
10:
11:
12:
13:
14:
15:
*/
