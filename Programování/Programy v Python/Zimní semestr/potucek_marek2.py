a = 10
b = 3
x = a

def posloupnost_cykly(a, b):
    count = 0                       # 1 přiřazení
    while a >= 0:                   # cyklus se provede (a-b)krát pro řádky 8 až 10
        print(a)                    
        count += 1
        a -= b
    if a < 0:                       # 1 porovnání
        a += b                      # 1 přiřazení
    for i in range(count-1):        # cyklus se provede (a-b)krát pro řádky 14 a 15
        a += b                      
        print(a)                 

posloupnost_cykly(a,b)                   

# časová složitost:THÉTA(5*(a-b) + 5) -> nevyskytují se ve funkci žádné vnořené cykly
# čas. složitost v nejhorším případě bude lineární

print()


def posloupnost(a,b):
    if a >= 0:                            
        print(a)                    
        posloupnost(a-b, b)
        global x
        if a < x:
            a += b
            print(a)

posloupnost(a,b)

print()

from random import randint
ARRAY_LENGHT = 5
array = [randint(0,10) for i in range(ARRAY_LENGHT)]

def jsou_ruzna(array):
    for i in range(len(array)-2):           # vnější cyklus provede se n-krát
        for j in range(len(array)-2):       # vnořený cyklus, provede řádky 49-52 n-krát
            if i == j:                      
                continue                
            if array[i] == array[j]:   
                return False           
    return True                             

print(jsou_ruzna(array))

# jelikož se jedná o funkci s vnořeným cyklem, můžeme konstanty zanedbat, pak je časová složitost kvadratická THÉTA(nˇ2)