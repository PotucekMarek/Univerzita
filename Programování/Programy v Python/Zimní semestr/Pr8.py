# 1-3) rekurzivně vynásobit 2 čísla + iterace
def add(m, n):
    result = 0
    for i in range(m):
        result += n
    return result

def add2(m, n):
    if m == 1:
        return n
    else:
        return add2(m-1, n) + n

def add3(m, n):
    return add_iter(m, n, 0)

def add_iter(m, n, it):
    if m == 0:
        return it
    else:
        return add_iter(m - 1, n, it + n)


print(add(5,6))
print(add2(5,6))
print(add3(5,6))

# 4-8) rekurze spočítá m-tou mocninu n DODĚLAT :)
def power(m,n):
    result = 1
    for i in range(m):
        result *= n
    return result

def power2(m, n):
    if m == 1:
        return n
    else:
        return power2(m-1, n) * n

def power3(m, n):
    return power_iter(m,n,1)

def power_iter(m,n,it):
    if m == 0:
        return it
    else:
        return power_iter(m - 1, n, it * n)

print(power(3,3))
print(power2(3,3))
print(power3(3,3))
