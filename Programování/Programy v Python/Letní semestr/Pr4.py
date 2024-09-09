EMPTY = []

def cons(val, lilist):
    return [val, lilist]

ll1 = cons(1, cons(2, cons(3, EMPTY)))

def get_first(lilist):
    return lilist[0]

print(get_first(ll1))

def get_rest(lilist):
    return lilist[1]

print(get_rest(ll1))

def is_empty(lilist):
    return EMPTY == lilist

print(is_empty(ll1))

# 1) get_second(lilist)
def get_second(lilist):
    return get_first(get_rest(lilist))

print(get_second(ll1))

# 2) get_third(lilist)
def get_third(lilist):
    return get_first(get_rest(get_rest(lilist)))

print(get_third(ll1))

# 3) nth(lilist, n) n = 0..první prvek
def nth(lilist, n):
    for i in range(n):
        lilist = get_rest(lilist)
    return get_first(lilist)

print(nth(ll1, 1))

# 4) length(lilist) ll1 = 3
def length(lilist):
    n = 0
    while not is_empty(lilist):
        lilist = get_rest(lilist)
        n += 1
    return n

def length_rec(lilist):
    if is_empty(lilist):
        return 0
    else:
        return 1 + length_rec(get_rest(lilist))
print(length(ll1))
print(length_rec(ll1))

# 5) lilist_range(n)) lilist_range(3)= [0, [1, [2, []]]]
def lilist_range(n):
    lilist = EMPTY
    for i in range(n):
        lilist = cons(i, lilist)
    return lilist
#print(lilist_range(5))

# 6) reverse(lilist)
def reverese(lilist):
    result = EMPTY
    while not is_empty(lilist):
        first = get_first(lilist)
        result = cons(first, result)
        lilist = get_rest(lilist)
    return result