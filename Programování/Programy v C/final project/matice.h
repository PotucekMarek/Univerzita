#ifndef MATICE_H
#define MATICE_H
#include <stdio.h>
#include <stdlib.h>

#define BEZ_CHYBY 0
#define CHYBA_ALOKACE 1
#define CHYBA_OTEVRENI 2
#define CHYBA_ZAVRENI 3
#define CHYBA_TYPU 4
#define CHYBA_JINA 5
#define VELIKOST_RADKU 10

int chyba;

typedef struct {
	int m;
	int n;
	float** data;
} matice;

extern float prvek(matice mat, int i, int j);
extern void nastav_prvek(matice mat, int i, int j, float hodnota);
extern void vypis(matice mat);
extern void odstran(matice mat);
extern int velikost(matice mat, int dimenze);
extern matice inicializace(int m, int n);
extern matice nulova(int m, int n);
extern matice jednotkova(int m, int n);
extern matice plus(matice mat1, matice mat2);
extern matice minus(matice mat1, matice mat2);
extern matice transpozice(matice mat);
extern matice nasobeni(matice mat, float skalar);
extern matice krat(matice mat1, matice mat2);
extern matice nacti_ze_souboru(const char* soubor);
extern void uloz_do_souboru(matice mat, const char* soubor);
#endif