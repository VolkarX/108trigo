#
## EPITECH PROJECT, 2025
## 102architect
## File description:
## Makefile
#

NAME = Build
all	:	$(NAME)

$(NAME):
	cp main.py 108trigo
	chmod +x 108trigo

clean: 
	rm -f *.o
	rm -f *~
	rm -f *Zone.Identifier
	rm -f *.pch
	rm -f utils/*~
	rm -f include/*.pch

fclean: clean
	rm 108trigo

re: fclean all
