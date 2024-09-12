test: potucekm-test-01.o potucekm-01.o
	gcc -o test potucekm-test-01.o potucekm-01.o

potucekm-test-01.o: potucekm-test-01.c
	gcc -c potucekm-test-01.c

potucekm-01.o: potucekm-01.asm
	nasm -f elf64 -g potucekm-01.asm