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

def delete_second(lilist):
    """Odstraní ze spojového seznamu druhý prvek. Mění spojový seznam."""
    set_rest(lilist, get_rest(get_rest(lilist)))

def get_last(lilist):
    """Vrátí poslední neprázdný spojový seznam spojového seznamu."""
    while not is_empty(get_rest(lilist)):
        lilist = get_rest(lilist)
    return lilist

def multiple_delete(lilist, n):
    """Odstraní ze spojového seznamu všechny násobky zadaného čísla n tak, že spojový seznam změní."""
    if is_empty(lilist):
        return EMPTY
    else:
        while not is_empty(lilist):
            current = get_second(lilist)
            if (current % n) == 0:
                delete_second(lilist)
                lilist = get_rest(lilist)
            else:
                lilist = get_rest(lilist)
        return lilist

"""
ll1 = cons(1, cons(2, cons(3, cons(4, cons(5, cons(6, EMPTY))))))
print(ll1)
multiple_delete(ll1, 2)
print(ll1)
multiple_delete(ll1, 5)
print(ll1)
"""

def multiple_delete_rec2(lilist, n):
    """Odstraní ze spojového seznamu všechny násobky zadaného čísla n tak, že spojový seznam změní."""
    if is_empty(lilist):
        return EMPTY
    else:
        if (get_second(lilist) % n) == 0:
            delete_second(lilist)
            return multiple_delete_rec(get_rest(lilist), n)
        else:
            return multiple_delete_rec(get_rest(lilist), n)
    return lilist

"""
def delete_all_multiples(lilist, n):
    Odstraní ze spojového seznamu všechna sudá čísla. Seznam lilist může změnit
    if is_empty(lilist):
        return EMPTY
    else:
        rest_result = delete_all_multiples(get_rest(lilist), n)
        if (get_first(lilist)%n) == 0:
            return rest_result
        else:
            set_rest(lilist, rest_result)
        return lilist


print(ll1)
delete_all_multiples(ll1, 2)
print(ll1)
delete_all_multiples(ll1, 3)
print(ll1)
"""
def multiple_delete(val, lilist):
    """Odstraní ze spojového seznamu všechna sudá čísla. Seznam lilist může změnit."""
    if is_empty(lilist):
        return EMPTY
    else:
        rest_result = multiple_delete(val, get_rest(lilist))
        if (get_first(lilist) % val) == 0:
            return rest_result
        else:
            set_rest(lilist, rest_result)
        return lilist


ll1 = cons(1, cons(2, cons(3, cons(4, cons(5, cons(6, EMPTY))))))
ll1 = multiple_delete(1, ll1)
print(ll1)