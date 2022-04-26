#ifndef NODE_HPP
#define NODE_HPP
#include <exception>
#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>
#include "state.hpp"

using namespace std;
class Node {
private:
	Node();
	State	_state;
	shared_ptr<Node> _parent;
	int	_depth;
	Node & operator=(Node const & rhs);
	Node(Node const & src);
public:
	Node(const State& currentStage, shared_ptr<Node> parent, int depth = 0);
	~Node();
	void	setParent(Node* node);
	void	setParent(shared_ptr<Node> node);
	const shared_ptr<Node> getParent();
	const shared_ptr<Node> getParent() const;
	const State& getState() const;
	int getDepth() const;
};

#endif
