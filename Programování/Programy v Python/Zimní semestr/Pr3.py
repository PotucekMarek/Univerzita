# 1)
n = 5

for i in range(n):
    k = i + 1
    divisor_counter = 0
    for j in range(k):
        l = j + 1
        if k % l == 0:
            divisor_counter += 1
            prime = divisor_counter == 2
    if prime:
        print(k)

# 2)
n = 5
a = 1
d = 3

for i in range(n):
    k = i + 1
    result = a + 3 * k
    if result:
        print(result)

# 3)
n = 5
a = 1
d = 3

for i in range(n):
    k = i + 1
    result = a + d * k
print(result)

# 4)
a = 9
b = 3

if a > b:
    for i in range(b):
        k = i + 1
        if a % k == 0:
            result = a // k
    print(result)

else:
     for i in range(a):
        k = i + 1
        if b % k == 0:
            result = b // k
     print(result)

# 5)
a = 21
b = 2
counter = 0

for i in range(b):
    k = i + 1
    if a % k == 0:
         counter += 1 

if counter > 1:
    print(False)
else:
    print(True)

# 6) factorial
n = 6
result = 1

for i in range(n):
    k = i + 1
    result *= k
print(result)

# 7) fib
n = 2
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

# 8) geometrická posloupnost
n = 5
a = 4
q = 2

for i in range(n):
    print(a)
    a *= q

# 9) geometrická posloupnost součet
n = 5
a = 4
q = 2
s = 0

for i in range(n):
    s += a 
    a *= q
print(s)

