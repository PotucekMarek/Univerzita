#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void format_str(char *output, char *input);
void align_str(char *output, char *input, unsigned int size, int alignment);
void typeset(char *input, unsigned int size, int alignment);

int main() {
    //1
    char *input = "Pomoci *hvezdicek* _prirozene zduraznime *kazde* slovo_ v textu.";
    char output[strlen(input) + 1];

    format_str(output, input);
    
    printf("%s\n", input);
    printf("%s\n", output);


    //2
    char bufl[20] = {0};
    char bufc[20] = {0};
    char bufr[20] = {0};

    char *s = " Ahoj Svete! ";
    align_str(bufl, s, 20, 0);
    align_str(bufc, s, 20, 1);
    align_str(bufr, s, 20, 2);

    printf("'%s'\n", bufc);
    printf("'%s'\n", bufl);
    printf("'%s'\n", bufr);



    //3
    typeset("*Zapoctove ukoly I*\nLS 2023\nV _externim assembleru NASM_\nnaprogramujte nasledujici funkce.\n", 40, 1);
    return 0;
}