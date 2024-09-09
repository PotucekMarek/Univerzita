# 1) palindrom
n = 654921408673376804129456
t = n
ir = 0 # porovnání

while n > 0:
    n1 = n % 10
    ir = ir * 10 + n1
    n //= 10

if (t == ir):
    print('yes, number is palindrom')

else: 
    print('no, number is not palindrom')

# 2) ciferný součet
n = 1235999
result = 0
counter = n

while n > 0:
    counter = n % 10
    n //= 10 
    result += counter
print(result) 

# 3) cifrace ciferného součtu
n = 1235
result = 0
counter = n
result_cif = 0

while n > 0:
    counter = n % 10
    n //= 10 
    result += counter
if result > 10:
    while result > 0:
        counter = result % 10
        result //= 10
        result_cif += counter 
    print(result_cif)
else:
    print(result)    

# 4b.) cifrace ciferného součtu
n = 1235
result = 0
counter = n
result_cif = 0
result_cif2 = 0


while n > 0:
    counter = n % 10
    n //= 10 
    result += counter
if result > 10:
    while result > 0:
        counter = result % 10
        result //= 10
        result_cif += counter 
    if result >= 10:
        while result_cif > 0:
            counter = result_cif % 10
            result_cif //= 10
            result_cif2 += counter 
        print(result_cif2)
    else:
        print(result_cif)
else:
    print(result)

# 4) reverse
n = 1230

while n > 0:
    count = n
    count %= 10 
    print(count, end='')
    n //= 10

# 5) tisk všech n-ciferných
n = 2
count = 1
it = 1

# všechny n
while n > 0:
    count *= 10
    n -= 1

# pouze pro n-cifry
while it != 0:
    it = count - 1
    it -= 10
    count -= 1 
    print(it)

# 6) kolikaciferné je n
n = 33333
count = 0
it = 0

while n > 0:
    it += n // 10
    if it or True:
        count += 1
    n //= 10
print(count)

# 7) euklidův algo
n = 30
t = 24
it = 0
while t != 0:
    it = n % t
    n = t
    t = it
print(n)
