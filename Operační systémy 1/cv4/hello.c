#include <stdlib.h>
#include <stdio.h>

int signum(int x);

char max2c(char a, char b);

//unsigned short min3us(unsigned short a, unsigned short b, unsigned short c);

int mocnina(int n, unsigned int m);

int main(int argc, char *argv[]){
    int x = 42;
    int result_sgn = signum(x);
    printf("Signum cisla %d je %d\n", x, result_sgn);

    char a = 'A';
    char b = 'B';
    int result_max = max2c(a, b);
    printf("nejvetsi hodnota znaku %c a %c je %d\n", a, b, result_max);

    //unsigned short d = 5;
    //unsigned short e = 6;
    //unsigned short f = 10;
    //unsigned short result_min = min3us(d,e,f);
    //printf("nejmensi hodnota cisel %d, %d a %d je %d\n", d,e, f, result_min);

    int n = 2;
    unsigned int m = 5;
    int result_moc = mocnina(n, m);
    printf("vysledek %d na %d je: %d\n", n, m, result_moc);
    return 0;
}
