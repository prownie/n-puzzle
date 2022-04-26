#include "node.hpp"

using namespace std;

class compareFunctor {
	public:
		bool operator()(const shared_ptr<Node>& node1, const shared_ptr<Node>& node2) const {
			const State& state1 = n1->getState();
			int cost1 = state1.getManhattanCost() + state1.getHammingCost() + n1->getDepth();
			const State& state2 = n2->getState();
			int cost2 = state2.getManhattanCost() + state2.getHammingCost() + n2->getDepth();
		}
	return cost1 < cost2;
}
