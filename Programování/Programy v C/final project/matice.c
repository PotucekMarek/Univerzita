#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "matice.h"

//_CRT_SECURE_NO_WARNINGS

matice inicializace(int m, int n) {
    matice mat;
    mat.m = m;
    mat.n = n;
    mat.data = (float**)malloc(m * sizeof(float*));
    if (mat.data == NULL) {
        chyba = CHYBA_ALOKACE;
        return mat;
    }
    else {
        for (int i = 0; i <= m-1; i++) {
            mat.data[i] = (float*)calloc(n, sizeof(float));
            if (mat.data[i] == NULL) {
                chyba = CHYBA_ALOKACE;
                return mat;
                }
        }
        chyba = BEZ_CHYBY;
        return mat;
    }
}

void nastav_prvek(matice mat, int i, int j, float hodnota) {
    if (i >= 0 && j >= 0 && i < mat.m && j < mat.n) {
        mat.data[i][j] = hodnota;
        chyba = BEZ_CHYBY;
    }
    else {
        chyba = CHYBA_JINA;
    }
}

matice nulova(int m, int n) {
    matice mat = inicializace(m, n);
    if (chyba != BEZ_CHYBY) {
        return mat;
    }
    chyba = BEZ_CHYBY;
    return mat;
}

matice jednotkova(int m, int n) {
    matice mat = inicializace(m, n);
    if (chyba != BEZ_CHYBY) {
        return mat;
    }
    else {
        for (int i = 0; i < mat.m; i++) {
            for (int j = 0; j < mat.n; j++) {
                if (j == i) {
                    mat.data[i][j] = 1;
                }
            }
        }
        chyba = BEZ_CHYBY;
        return mat;
    }
}

void odstran(matice mat) {
    for (int i = 0; i < mat.m; i++) {
        free(mat.data[i]);
        mat.data[i] = NULL;
        if (mat.data[i] != NULL) {
            chyba = CHYBA_JINA;
        }
    }
    free(mat.data);
    mat.data = NULL;
    chyba = BEZ_CHYBY;
    if (mat.data != NULL) {
        chyba = CHYBA_JINA;
    }
}

void vypis(matice mat) {
    if (mat.data == NULL) {
        chyba = CHYBA_TYPU;
    }
    else {
        for (int i = 0; i < mat.m; i++) {
            for (int j = 0; j < mat.n; j++) {
                printf("%f ", mat.data[i][j]);
            }
            printf("\n");
        }
        chyba = BEZ_CHYBY;
    }
}

int velikost(matice mat, int dimenze) {
    switch (dimenze)
    {
    case 1:
        chyba = BEZ_CHYBY;
        return mat.m;
    case 2:
        chyba = BEZ_CHYBY;
        return mat.n;
    }
    chyba = CHYBA_JINA;
    return 0;
}

float prvek(matice mat, int i, int j) {
    if (i >= 0 && j >= 0 && i < mat.m && j < mat.n) {
        chyba = BEZ_CHYBY;
        return mat.data[i][j];
    }
    else {
        chyba = CHYBA_ALOKACE;
        return 0;
    }
}

matice plus(matice mat1, matice mat2) {
    if (mat1.m != mat2.m && mat1.n != mat2.n) {
    chyba = CHYBA_TYPU;
    return mat1;
    }
    matice newmat = inicializace(mat1.m, mat1.n);
    if (chyba != BEZ_CHYBY) {
        return mat1;
    }
    else if (mat1.data == NULL || mat2.data == NULL) {
        chyba = CHYBA_ALOKACE;
        return mat1;
    } 
    else {
        for (int i = 0; i < mat1.m; i++) {
            for (int j = 0; j < mat1.n; j++) {
                nastav_prvek(newmat, i, j, (prvek(mat1, i, j) + (prvek(mat2, i, j))));
            }
        }
        chyba = BEZ_CHYBY;
        return newmat;
    }
}

matice minus(matice mat1, matice mat2) {
    if (mat1.m != mat2.m && mat1.n != mat2.n) {
    chyba = CHYBA_TYPU;
    return mat1;
    }
    matice newmat = inicializace(mat1.m, mat1.n);
    if (chyba != BEZ_CHYBY) {
        return mat1;
    }

    else if (mat1.data == NULL || mat2.data == NULL) {
        chyba = CHYBA_ALOKACE;
        return mat1;
    }
    else {
        for (int i = 0; i < mat1.m; i++) {
            for (int j = 0; j < mat1.n; j++) {
                nastav_prvek(newmat, i, j, (prvek(mat1, i, j) - (prvek(mat2, i, j))));
            }
        }
        chyba = BEZ_CHYBY;
    }
    return newmat;
}

matice transpozice(matice mat) {
    if (chyba != 0) {
        return mat;
    }
    matice newmat = inicializace(mat.n, mat.m);
    if (mat.data == NULL) {
        chyba = CHYBA_ALOKACE;
        return mat;
    }
    else {
        for (int i = 0; i < mat.m; i++) {
            for (int j = 0; j < mat.n; j++) {
                float skalar = prvek(mat, i, j);
                nastav_prvek(newmat, j, i, skalar);
            }
        }
        chyba = BEZ_CHYBY;
        return newmat;
    }
}

matice nasobeni(matice mat, float skalar) {
    if (chyba != BEZ_CHYBY) {
        return mat;
    }
    matice newmat = inicializace(mat.m, mat.n);
    if (mat.data == NULL) {
        chyba = CHYBA_ALOKACE;
        return mat;
    }
    else {
        for (int i = 0; i < mat.m; i++) {
            for (int j = 0; j < mat.n; j++) {
                float old_skalar = prvek(mat, i, j);
                nastav_prvek(newmat, i, j, (old_skalar * skalar));
            }
        }
        chyba = BEZ_CHYBY;
        return newmat;
    }
}

matice krat(matice mat1, matice mat2) {
    if (chyba != BEZ_CHYBY) {
        return mat1;
    }
    else if (mat1.n != mat2.m) {
        chyba = CHYBA_TYPU;
        return mat1;
    }
    matice newmat = inicializace(mat1.m, mat2.n);
    if (mat1.data == NULL || mat2.data == NULL) {
        chyba = CHYBA_ALOKACE;
        return mat1;
    }
    else {
        for (int i = 0; i < mat1.m; i++) {
            for (int j = 0; j < mat2.n; j++) {
                for (int k = 0; k < mat2.m; k++) {
                    newmat.data[i][j] += mat1.data[i][k] * mat2.data[k][j];
                }
            }
        }
        chyba = BEZ_CHYBY;
        return newmat;
    }
}

void uloz_do_souboru(matice mat, const char* soubor) {
    FILE* fw = fopen(soubor, "w+");
    if (fw == NULL) {
        chyba = CHYBA_OTEVRENI;
    }
    else {
        for (int i = 0; i < mat.m; i++) {
            for (int j = 0; j < mat.n; j++) {
                fprintf(fw, "%f ", mat.data[i][j]);
            }
            fprintf(fw, "\n");
        }
        if (fclose(fw) != 0) {
            chyba = CHYBA_ZAVRENI;
        }
        else {
            chyba = BEZ_CHYBY;
        }
    }
}

matice nacti_ze_souboru(const char* soubor) {
    FILE* fr;
    int radky = 2;
    int sloupce = 1;
    char line[VELIKOST_RADKU];
    float val;
    fr = fopen(soubor, "r");
    if (fr == NULL) {
        chyba = CHYBA_OTEVRENI;
        return nulova(1, 1);
    }
    else {
        if (fr) {
            char c = getc(fr);
            if (c != EOF) {
                while (c != '\n') {
                    if (c == ' ') {
                        sloupce++;
                    }
                    c = getc(fr);
                }
            }
            c = getc(fr);
            while (c != EOF) {
                if (c == '\n') {
                    radky++;
                }
                c = getc(fr);
            }
            fclose(fr);
            fr = fopen(soubor, "r");
            if (fr == NULL) {
                chyba = CHYBA_OTEVRENI;
                return nulova(1, 1);
            }
            else {
                matice mat = inicializace(radky, sloupce);
                int i = 0;
                int j = 0;
                char* token;
                while (fgets(line, VELIKOST_RADKU, fr)) {
                    token = strtok(line, "\n");
                    token = strtok(token, " ");
                    val = atof(token);
                    if (j < sloupce) {
                        nastav_prvek(mat, i, j, val);
                    }
                    else {
                        j = 0;
                        i++;
                        nastav_prvek(mat, i, j, val);
                    }
                    j++;
                }
                chyba = BEZ_CHYBY;
                return mat;
            }
        }
        chyba = CHYBA_JINA;
        return nulova(1, 1);
    }
    fclose(fr);
    if (fclose(fr) != 0) {
        chyba = CHYBA_ZAVRENI;
        return nulova(1, 1);
    }
}
