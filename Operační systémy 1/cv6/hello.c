#include <stdlib.h>
#include <stdio.h>

void print_row(int n, char c);
void print_rect(int rows, int cols);
unsigned int factorial(unsigned int n);
char *my_strdup(char *s);
unsigned int fib(unsigned short n);

void printi(int n) {
    printf("%i\n", n);
}

int main(int argc, char *argv[]) {
    print_row(5, 'x');

    print_rect(3, 4);

    printf("Factorial of 5 is %u\n", factorial(5));

    char *original = "Hello, world!";
    char *copy = my_strdup(original);
    printf("Original: %s, Copy: %s\n", original, copy);
    free(copy);

    printf("Fibonacci of 10 is %u\n", fib(10));

    return 0;
}