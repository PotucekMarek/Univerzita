#include <stdio.h>
#define velikost 3

int main()
{
    float pole[velikost];
    int i;
    float v = 0;

    printf("Zadejte hodnoty do pole: "); 
    for (i=0; i < velikost; i++)
    {
        if (i > 0)
        {
            printf("\nZadejte dalsi cislo do pole: ");

        }
        scanf("%f", &pole[i]);
    }

    for (i = 0; i < velikost; i++)   
    {
        v = v+pole[i];
    }
    printf("\nAritmeticky prumer je: %f", v/velikost);     
    return 0;
}
