#include <stdio.h>
#define velikost 30

int nejblizsi_vyssi_prvocislo(int prirozene)
{
    int i, j, k, hledany;
    int pole[velikost];

    for(k = 0; k < prirozene; k++) 
    {
        pole[k] = k;
    }

    for(j = 1; j < prirozene;j++)   
    {
        for(i = 0; i < velikost; i++)
        {
            if(pole[i] = j*i)
            {
                pole[i] = 0;
            }
        }
    }

    hledany = prirozene;       
    for(i = 0; hledany < velikost; i++)
    {
        if(pole[i] == 0)
        {
            break;
        }
        if((pole[i] != 0) && (pole[i] > hledany))
        {
            return pole[i];
        }
    }
}

int main()   
{
    int cislo, vysledek;
    printf("Zadejte cislo: ");
    scanf("%i", &cislo);
    printf("\nVase cislo a rozdil od nejblizsiho vetsiho prvocisla je: ");

    vysledek = cislo - nejblizsi_vyssi_prvocislo(cislo);
    printf("%i", vysledek);
}
