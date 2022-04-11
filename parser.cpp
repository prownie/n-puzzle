#include "parser.hpp"

Parser::Parser(int ac, char** av) : _ac(ac), _filename(std::string (av[1])) {
	if (_ac != 2)
		throw Parser::Bad_arg_number_exception();
	//2 case, either full filename, or number
	//first case : only a number
	std::ifstream file;
	if (_filename.find_first_not_of("0123456789") == std::string::npos)
	{
		std::stringstream ss;
		_size = stoi(_filename);
		_size = _size * _size -1;
		ss << _size << "Puzzle.txt";
		file.open(ss.str());
		if (!file) {
			throw std::invalid_argument("File '"+ss.str() + "' not found");
			std::cout << "hey2" << std::endl;
		}
		
	}
}

Parser::~Parser() {

}

Parser::Parser(Parser const & src) {
	_grid = src._grid;
	_ac = src._ac;
	_filename = src._filename;
}

char const * Parser::Bad_arg_number_exception::what( void ) const throw()
{
	return "Wrong arg number, use ./npuzzle [Filename|SquareSize]";
}

// char const * Parser::File_not_found_exception::what( void ) const throw()
// {
// 	return "File '" + _size*_size-1 + "Puzzle.txt' not found";
// }
