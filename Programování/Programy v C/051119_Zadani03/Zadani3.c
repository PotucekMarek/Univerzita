#include <stdio.h>

int main()
{
    char retezec[] = "oko";
    int i
    int delka = 0

    printf("Predikat palindromu '%s'", retezec);

    while (retezec[delka]) //zjisteni delky retezce, ktery uzivatel zadal
    {
        delka++;
    }

    for (i = 0; i < (delka/2); i++)
    {
        if (retezec[i] != retezec[delka-1-i])
        {
            printf("\nNeni palindrom");
            return 0;
        }
    }

    printf("\nJe palindrom");
    return 0;
}
