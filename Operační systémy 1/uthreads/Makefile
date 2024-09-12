CFLAGS = -g -Wall -O2

uthreads-demo: uthreads.o uthreads-switch.o uthreads-util.o uthreads-demo.o
	$(CC) $(CFLAGS) -o uthreads-demo uthreads.o uthreads-switch.o uthreads-util.o uthreads-demo.o

uthreads-demo.o: uthreads-demo.c
	$(CC) $(CFLAGS) -c uthreads-demo.c

uthreads.o: uthreads.c uthreads.h
	$(CC) $(CFLAGS) -c uthreads.c

uthreads-util.o: uthreads-util.h uthreads-util.c
	$(CC) $(CFLAGS) -c uthreads-util.c


uthreads-switch.o: uthreads-switch.asm
	nasm -felf64 uthreads-switch.asm

clean:
	rm *.o
	rm -f uthreads-demo
