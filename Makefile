# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rpichon <rpichon@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/09 13:51:45 by rpichon           #+#    #+#              #
#    Updated: 2021/03/04 16:17:41 by rpichon          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #


SRCS		= 		main.cpp node.cpp parser.cpp solver.cpp
OBJS		= 		${SRCS:.c=.o}
NAME		= 		npuzzle
RM			= 		rm -f
FLAGS 		= 		-Wall -Wextra -Werror
#FLAGS		=		-g3 -fsanitize=address -Wall -Wextra -Werror -pthread

# **************************************************************************** #
#								REGLES									       #
# **************************************************************************** #

all:							$(NAME)

%.o: %.c
								clang++ $(FLAGS) -c $< -o $@

$(NAME):				$(OBJS) Makefile
								clang++ $(FLAGS) $(OBJS) -o $(NAME)
								@echo "\n\033[0;32m[npuzzle OK] \033[0m \033\n"

clean:
								@echo "\033[0;32m[OK] \033[0m \033[0;33m Object files deleted:\033[0m"
								@$(RM) *.o

fclean:					clean
								@echo "\033[0;32m[OK] \033[0m \033[0;33m Object files  + exedeleted:\033[0m"
								@$(RM) $(NAME)

cleanPuzzles:
								$(RM) *Puzzle.txt

re:								fclean all

.PHONY: 					clean fclean
