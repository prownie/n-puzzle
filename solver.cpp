#include "solver.hpp"

Solver::Solver(Parser original_grid) {
	(void) original_grid;
}

Solver::~Solver() {

}

void Solver::run(){}

char const * Solver::Bad_arg_number_exception::what( void ) const throw()
{
	return "Wrong arg number";
}

char const * Solver::Bad_size_arguments::what( void ) const throw()
{
	return "Network data must be written with the format host:port:password";
}
