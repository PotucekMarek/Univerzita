#include <stdio.h>

int main()
{
    char retezec[21];
    int i;
    printf("Zadejte retezec: ");
    scanf("%20s", retezec);

    printf("Puvodni retezec byl: ");
    printf("%s", retezec);

    for (i = 0; i < 21; i++)
    {
        if ((retezec[i] >= 'a')&&(retezec[i] <= 'z'))
        {
            retezec[i] = retezec[i] + 'A' - 'a'; // -32 meni maly znak na velky, pomoci ASCII tabulky
        }
    }

    printf("\nNovy retezec je: ");
    printf("%s", retezec);
    return 0;
}
