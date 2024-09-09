# funkce
# 1) fib
def fib(n):
    a = 0
    b = 1
    for i in range(n):
        t = a
        print(a, end=' ')
        a = b
        b += t
fib(8)
print()

# 2) reverse seznamu
def reverse(n):
    first = 0
    last = len(n) - 1
    while first < last:
        holder = n[first]
        n[first] = n[last] 
        n[last] = holder
        first += 1
        last -= 1
    return n 

print(reverse([2,2,3,5,5]))

# 3) funkce vrátí podseznam v rozmezí f-t
def sublist(array, f, t):
    n = array
    first = n[f]
    last = n[t]
    result = 0
    while first <= last:
        holder = n[first]
        n[result] += holder
        first += 1
    return n
print(sublist([1,2,3,4,5],0,2))

# 4) sečte prvky v seznamu
def list_sum(input_list):
    result = 0
    for i in range(len(input_list)):
        holder = input_list[i]
        result += holder
    return result
print(list_sum([1,2,3]))

# 5) rozhodne zda seznam obsahuje zadaný prvek
def is_in_list(input_list, n):
    for i in range(len(input_list)):
        if n == input_list[i]:
            return True
            break

print(is_in_list([1,2,3], 4))
        
# 6) fib, ale seznam
def fib_list(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        t = a
        result += [a]
        a = b
        b += t
    return result
print(fib_list(10))

# 7) odstraní všechny zadané prvky z listu
def remove_list(input_list, n):
    result = []
    for i in range(len(input_list)):
        element = input_list[i]
        if n != element:
            result += [element]
    return result
print(remove_list([1,2,3,4,5],5))

# 8) fact
def fact(n):
    input_list = []
    for i in range(n):
        input_list += [i + 1]
    result = 1
    for i in range(len(input_list)):
        element = input_list[i]
        result *= element
    
    return result
print(fact(5))
