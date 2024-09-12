hello: hello.o demo.o
	gcc -o hello hello.o demo.o

hello.o: hello.c
	gcc -c hello.c

demo.o: demo.asm
	nasm -f elf64 demo.asm

rem: hello.o
	rm hello.o