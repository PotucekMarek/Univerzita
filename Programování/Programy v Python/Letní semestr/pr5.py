# Spojové seznamy a jejich změna

# Prázdný spojový seznam je pouze hodnota EMPTY.
EMPTY = []

# Neprázdný spojový seznam určuje první prvek a zbytek. Zbytek je opět spojový seznam.
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

"""
ll1 = cons(1, EMPTY)
print(ll1)
set_first(ll1, 2)
print(ll1)
set_rest(ll1, cons(3, EMPTY))
print(ll1)
"""

# z minulého semináře
def nth_rest(lilist, n):
    """Vrátí spojový seznam bez prvních n prvků. Iterativní verze."""
    for i in range(n):
        lilist = get_rest(lilist)
    return lilist

# print(nth_rest(ll1, 2))

def nth(lilist, n):
    """Vrátí prvek na indexu n spojového seznamu."""
    ll = nth_rest(lilist, n)
    return get_first(ll)

def is_empty(lilist):
    """Rozhodne, zda je spojový seznam prázdný."""
    return lilist == EMPTY

def get_second(lilist):
    """Vrátí druhý prvek spojového seznamu."""
    return get_first(get_rest(lilist))

# print(get_second(ll1))

def get_third(lilist):
    """Vrátí třetí prvek spojového seznamu."""
    return get_second(get_rest(lilist))

# print(get_third(ll1))

# jednoduché funkce

def set_second(lilist, value):
    """Nastaví druhý prvek spojového seznamu."""
    set_first(get_rest(lilist), value)

"""
ll1 = cons(1, cons(2, cons(3, EMPTY)))
set_second(ll1, 4)
print(ll1)
"""

def set_third(lilist, value):
    """Nastaví třetí prvek spojového seznamu."""
    set_second(get_rest(lilist), value)

"""
ll1 = cons(1, cons(2, cons(3, EMPTY)))
set_third(ll1, 4)
print(ll1)
"""

# Přidání hodnoty na konec
def append_value(lilist, val):
    """Přidá nakonec spojového seznamu hodnotu tak, že jej nezmění."""
    if is_empty(lilist):
        return cons(val, EMPTY)
    else:
        append_rest = append_value(get_rest(lilist), val)
        return cons(get_first(lilist), append_rest)

"""
ll1 = cons(1, cons(2, EMPTY))
print(ll1)
ll2 = append_value(ll1, 3)
print(ll1) # [1, [2, []]]
print(ll2) # [1, [2, [3, []]]]
"""

def get_last(lilist):
    """Vrátí poslední neprázdný spojový seznam spojového seznamu."""
    while not is_empty(get_rest(lilist)):
        lilist = get_rest(lilist)
    return lilist

"""
print(get_last(cons(1, cons(2, cons(3, EMPTY))))) # [3, []]
"""

def add_to_end(lilist, val):
    """Přidá na konec spojového seznamu hodnotu tak, že jej může změnit."""
    if is_empty(lilist):
        return cons(val, EMPTY)
    else:
        tail = cons(val, EMPTY)
        last = get_last(lilist)
        set_rest(last, tail)
        return lilist

def remove_last(lilist):
    """Odstraní poslední prvek ze spojového seznamu."""
    if is_empty(lilist):
        return EMPTY
    else:
        remove_from_rest = remove_last(get_rest(lilist))
        return cons(get_first(lilist),remove_from_rest)
    
ll1 = cons(1, cons(2, cons(3, EMPTY)))
#print(remove_last(ll1))

def get_butlast(lilist):
    """Vrátí předposlední neprázdný spojový seznam spojového seznamu."""
    while not is_empty(get_rest(get_rest(lilist))):
        lilist = get_rest(lilist)
    return lilist
#print(get_butlast(ll1))

def delete_last(lilist):
    """Odstraní poslední prvek neprázdného spojového seznamu. Může jej změnit."""
    if is_empty(lilist):
        return EMPTY
    else:
        set_rest(get_butlast(lilist), EMPTY)
    return lilist

#print(delete_last(ll1))

# Odstranění prvku na indexu
def remove_nth(lilist, n):
    """Odstraní ze spojového seznamu prvek na indexu n. Nezmění spojový seznam."""
    if n == 0:
        return get_rest(lilist)
    else:
        return cons(get_first(lilist), remove_nth(get_rest(lilist), n-1))

#print(remove_nth(ll1, 1))

def delete(lilist, n):
    """Odstraní ze spojového seznamu prvek na indexu n. Může změnit spojový seznam."""
    if n == 0:
        return get_rest(lilist)
    else:
        x = cons(get_first(lilist), delete(get_rest(lilist), n - 1))
        set_rest(x, EMPTY)
    return lilist

print(delete(ll1, 1))
#nefunkční
lilist = cons(1, cons(2, cons(3, EMPTY)))
print(get_first(lilist) % 2)
# Odstranění prvku na indexu