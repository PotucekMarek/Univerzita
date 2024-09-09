# 1)
n = 5

for i in range(n):
    k = i + 1
    for j in range(k):
        print('*', end='')
    print()
print()

# 2)
n = 5

for i in range(n):
    for j in range(n):
        print('*', end='')
    print()
print()

# 3)
n = 5

for i in range(n):
    print('*', end='')
print()

for i in range(n - 2):
    k = i
    print('*',((n - 4) * ' '),'*')

for i in range(n):
    print('*', end='')
print()
print()
    
# 4)

n = 6

for i in range(n):
    print('',end=' ')

for i in range(n):
    print('', end='')
    i = i + 1
    for j in range(i):
        print((2 * '*'), end='')
    print()
print()