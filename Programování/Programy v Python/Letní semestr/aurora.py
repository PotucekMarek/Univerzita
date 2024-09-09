EMPTY = []

def cons(val, lilist):
    return [val, lilist]

ll1 = (cons(1, cons(2, cons(3, EMPTY))))
ll2 = (cons(4, cons(5, cons(6, EMPTY))))
ll2 = (cons(7, cons(8, cons(5, EMPTY))))

def get_first(lilist):
    return lilist[0]

def get_rest(lilist):
    return lilist[1]

def get_second(lilist):
    return get_first(get_rest(lilist))

def get_third(lilist):
    return get_first(get_rest(get_rest(lilist)))

def length(lilist):
    count = 0
    while lilist != EMPTY:
        count += 1
        lilist = get_rest(lilist)
    return count
count = 0

def length_rec(lilist):
    global count
    if EMPTY != lilist:
        count += 1
        length_rec(get_rest(lilist))
    return count

def lilist_range(n):
    lilist = EMPTY
    for i in range(n):
        lilist = cons(i, lilist)
    return lilist

def reverse(lilist):
    new_lilist = EMPTY
    while EMPTY != lilist:
        first = get_first(lilist)
        new_lilist = cons(first, new_lilist)
        lilist = get_rest(lilist)
    return new_lilist

def is_member(val, lilist):
    while lilist != EMPTY:
        if val == get_first(lilist):
            return True
        else:
            lilist = get_rest(lilist)
            continue
    return False

def is_member_rec(val, lilist):
    if lilist != EMPTY:

        if val == get_first(lilist):
            return True
            
        else:
            return is_member_rec(val, get_rest(lilist))
    else:
        return False

def append(ll1, ll2):
    ll1 = reverse(ll1)
    while ll1 != EMPTY:
        first = get_first(ll1)
        ll2 = cons(first, ll2)
        ll1 = get_rest(ll1)
    return ll2

def is_sorted(lilist):
    while lilist != EMPTY:
        first = get_first(lilist)
        second = get_second(lilist)
        if first >= second:
            return False
        else:
            lilist = get_rest(lilist)
            continue
    return True

#print(get_first(ll1))
#print(get_rest(ll1))
#print(get_second(ll1))
#print(get_third(ll1))
#print(length(ll1))
#print(length_rec(ll1))
#print(lilist_range(3))
#print(reverse(ll1))
#print(is_member(4, ll1))
#print(is_member_rec(2, ll1))
#print(append(ll1, ll2))
#print(is_sorted(ll1))
""""""""""""""""""""""""""""""""""""""""""""""""
def set_first(lilist, val):
    """Nastaví první prvek listu"""
    lilist[0] = val

def set_rest(lilist,rest_ll):
    """Nastaví zbytek listu"""
    lilist[1] = rest_ll

def set_second(lilist, val):
    """Nastaví druhý prvek listu"""
    set_first(get_rest(lilist), val)

def set_third(lilist, val):
    """Nastaví třetí prvek listu"""
    set_first(get_rest(get_rest(lilist)), val)

def nth_rest(lilist, n):
    """Vrátí spojový seznam bez prvních n prvků. Iterativní verze."""
    for i in range(n):
        lilist = get_rest(lilist)
    return lilist
def nth(lilist, n):
    """Vrátí prvek na indexu n spojového seznamu"""
    return get_first(nth_rest(lilist, n))

def is_empty(lilist):
    return lilist == EMPTY

def get_last(lilist):
    """Vrátí poslední neprázdný spojový seznam spojového seznamu."""
    while not is_empty(get_rest(lilist)):
        lilist = get_rest(lilist)
    return cons(get_first(lilist), EMPTY)

def append_value(lilist, val):
    """Přidá nakonec spojového seznamu hodnotu tak, že jej nezmění."""
    if is_empty(lilist):
        return cons(val, EMPTY)
    else:
        append_rest = append_value(get_rest(lilist), val)
        return cons(get_first(lilist), append_rest)

def add_to_end(lilist, val):
    """Přidá nakonec spojového seznamu hodnotu tak, že jej může změnit."""
    if is_empty(lilist):
        return cons(val, EMPTY)
    else:
        tail = cons(val, EMPTY)
        last = get_last(lilist)
        set_rest(last, tail)
        return lilist


#set_second(ll1, 5)
#set_third(ll1, 5)
#print(nth(ll1, 2))
#print(nth_rest(ll1, 2))
#print(nth(ll1, 0))
#print(append_value(ll1, 5))
#print(get_last(ll1))
print(add_to_end(ll1,5))
#print(ll1)