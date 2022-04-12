#include "node.hpp"
#include "parser.hpp"
#include "solver.hpp"

int main(int ac, char** av) {
	try {
		Parser parsed_file(ac, av);
		Solver app(parsed_file);
		app.run();
	}
	catch (const std::exception& e) {
		std::cerr << e.what() << std::endl;
		return EXIT_FAILURE;
	}
	return EXIT_SUCCESS;
}
