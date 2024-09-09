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

posloupnost_cykly(10,3) 

# časová složitost:THÉTA(5*(a-b) + 5) -> nevyskytují se ve funkci žádné vnořené cykly
# čas. složitost v nejhorším případě bude lineární

print()


def posloupnost(a,b):
  posloupnost_help(a,b,a)           # pomocná funkce

def posloupnost_help(a,b,end):
  if a >= 0:                        # podmínka, dokud a>=0  =>  1 porovnání
    print(a)                        # 1 tisk 
    posloupnost_help(a-b,b,end)     # znovu volaná funkce
    if a != end:                    # podmínka, bude se provádět dokud a == end => 1 porovnání
      a += b                        # 1 přiřazení
      print(a)                      # 1 tisk

posloupnost(10,3)

# časová složitost: THÉTA(5*(a-b)+1) -> ve funkci se nenachází žádné cykly, tudíž bude
# časová složitost v nehorším případě lineární