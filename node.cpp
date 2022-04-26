#include "node.hpp"

Node::Node(const State& currentState, shared_ptr<Node> parent, int depth) :
_state(currentState), _depth(depth)
{
	_parent = parent;
}

Node::~Node() {

}

void Node::setParent(Node* node) {
	_parent.reset(node);
}

void	Node::setParent(shared_ptr<Node> node) {
	_parent = node;
}

// shared_ptr<Node> Node::getParent() {return _parent;}
const shared_ptr<Node> Node::getParent() const {return _parent;}
const State& Node::getState() const {return _state;}
int		Node::getDepth() const {return _depth;}
