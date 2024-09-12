#include <stdlib.h>
#include <stdio.h>

void swap(int *a, int *b);
void division(unsigned int x, unsigned int y, unsigned int *result, unsigned int *remainder);
void countdown(int *values);
void nasobky(short *multiples, short n);
int minimum(int count, int *values);
unsigned int my_strlen(char *s);
void my_strcat(char *dest, char *src);

int main(int argc, char *argv[]) {
    int a = 5, b = 69;
    unsigned int result, remainder;
    int values[10];
    short multiples[10];
    char str1[100] = "Hello, ";
    char str2[100] = "World!";
    
    printf("Funkce swap prohodi cisla %d a %d ", a, b);
    swap(&a, &b);
    printf("na cisla %d a %d.\n", a, b);

    division(10, 3, &result, &remainder);
    printf("Division 10 / 3 = %u, remainder = %u\n", result, remainder);

    countdown(values);
    printf("Countdown: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", values[i]);
    }
    printf("\n");

    nasobky(multiples, 5);
    printf("Multiples of 5: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", multiples[i]);
    }
    printf("\n");

    int arr[] = {5, -3, 9, 0, 2, -7, 10};
    printf("Minimum in array: %d\n", minimum(7, arr));

    printf("Length of string 'Hello, World!': %u\n", my_strlen("Hello, World!"));

    my_strcat(str1, str2);
    printf("Concatenated string: %s\n", str1);

    return 0;
}