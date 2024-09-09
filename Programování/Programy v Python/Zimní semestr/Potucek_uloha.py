# úloha za 15 bodů, vypracoval Potůček Marek, 12.11.

string = '2*3+6/3-2'                # zadá uživatel 

NUMBER_DISTANCE = 48                # velikost čísel v ascii

string += '-'                       # pomocný znak na vykonání poslední operace(libovolný), ukončí se cyklus
digit = 0
result = 0
last_operation = '+'                # přičte výsledek(0) k prvnímu číslu, tím se vyvaruji opakujícímu se kódu

for i in range(len(string)):        # cyklus, prochází string

    if ord(string[i])>= NUMBER_DISTANCE: # pokud je znak číslo
        char = ord(string[i])       # do proměnné uložím hodnotu znaku z ascii
        char -= NUMBER_DISTANCE     # odečtu NUMBER_DISTANCE a dostanu číslo
        digit *= 10                 # u prvního projití bude digit 0, pak se bude zvyšovat na základě počtu cifer
        digit += char               # u prvního projití se do 0 přidá char

    else:                           # pokud znak není číslo, vykoná se operace, kterou vložím do výsledku 
        if last_operation == '+':   
            result += digit
        
        elif last_operation == '*':
            result *= digit

        elif last_operation == '/':
            result //= digit

        else:
            result -= digit

        last_operation = string[i]  # do proměnné last_operation vložím aktuální operaci
        digit = 0                   # vynuluji číslo

print(result)