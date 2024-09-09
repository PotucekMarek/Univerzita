# 1. zápočtová úloha | Marek Potůček | první skupina | vytvořeno 29.3.2021 | 2. verze
EMPTY = []

def cons(value, lilist):
    """Vytvoří nový spojový seznam, kde první prek bude value a zbytek lilist."""
    return [value, lilist]

def get_first(lilist):
    """Vrátí první prvek neprázdného spojového seznamu."""
    return lilist[0]

def get_rest(lilist):
    """Vrátí zbytek neprázdného spojového seznamu."""
    return lilist[1]

def set_first(lilist, value):
    """Nastaví první prvek spojového seznamu."""
    lilist[0] = value

def set_rest(lilist, rest_ll):
    """Nastaví zbytek spojového seznamu."""
    lilist[1] = rest_ll

def is_empty(lilist):
    """Rozhodne, zda je spojový seznam prázdný."""
    return lilist == EMPTY

def get_second(lilist):
    """Vrátí druhý prvek spojového seznamu."""
    return get_first(get_rest(lilist))


def multiple_remove(lilist, n):
    """Odstraní ze spojového seznamu všechny násobky zadaného čísla n tak, že spojový seznam nezmění."""
    if is_empty(lilist):
        return EMPTY
    else:
        if (get_first(lilist) % n) == 0:
            return multiple_remove(get_rest(lilist), n)
        else:
            return cons(get_first(lilist), multiple_remove(get_rest(lilist), n))


ll1 = cons(1, cons(2, cons(3, cons(4, cons(5, cons(6, cons(7, EMPTY)))))))
print(multiple_remove(ll1, 3))
print(multiple_remove(ll1, 2))


def multiple_delete(lilist, n):
    """Odstraní ze spojového seznamu všechna sudá čísla. Seznam lilist může změnit."""
    if is_empty(lilist):
        return EMPTY
    else:
        rest_result = multiple_delete(get_rest(lilist), n)
        if (get_first(lilist)%n) == 0:
            return rest_result
        else:
            set_rest(lilist, rest_result)
        return lilist
"""
ll1 = cons(1, cons(2, cons(3, cons(4, cons(5, cons(6, cons(7, EMPTY)))))))
print(ll1)
multiple_delete(ll1, 2)
print(ll1)
multiple_delete(ll1, 3)
print(ll1)
#multiple_delete(ll1, 1) nefunkční
#print(ll1)
"""