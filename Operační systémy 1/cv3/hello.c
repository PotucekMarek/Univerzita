#include <stdlib.h>
#include <stdio.h>

int obvod_o(int a, int b);

int obsah_o(int a, int b);

int obsah_ctverce(int a);

int obvod_trojuhelnika(int a, int b, int c);

int obvod_trojuhelnika2(int a);

int obsah_trojuhelnika2(int a, int b);

int obsah_trojuhelnika3(int a, int va);

int objem_krychle(int a);

unsigned int avg(unsigned int a, unsigned int b, unsigned int c);

int main(int argc, char *argv[]){
    printf("obvod o 3, 4: %d\n", obvod_o(3,4));
    printf("obsah o 3, 4: %d\n", obsah_o(3,4));
    printf("obsah o 3: %d\n", obsah_ctverce(3));
    printf("obvod 3uhelniku o 3, 4, 5: %d\n", obvod_trojuhelnika(3, 4, 5));
    printf("obvod_trojuhelnika2 o 3: %d\n", obvod_trojuhelnika2(3));
    printf("obsah_trojuhelnika2 o 3, 4: %d\n", obsah_trojuhelnika2(3, 4));
    printf("obsah_trojuhelnika3 o 3, 4: %d\n", obsah_trojuhelnika3(3, 4));
    printf("objem_krychle o 3: %d\n", objem_krychle(3));
    printf("prumer tri cisel: %d\n", avg(3,5,1));
    return 0;
}
