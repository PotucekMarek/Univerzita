# 1) fahrenheit to celsius
f = 50
c = 5 * (f - 32) / 9
print('Teplota je:', c, '°C')

# 2)
c = 10
f = 9 * c / 5 + 32
print ('Teplota je:', f, '°F')

# 3) Fib
n = 10
a = 0
b = 1

for i in range(n):
    print(a, end=' ')
    t = a
    a = b
    b += t
print()

# 4) součet n čísel 1/1+1/2+1/3+1/4...
n = 5
a = 0
b = 1

for i in range(n):
    a += 1/b
    b += 1 
print(a)

# 5) přibližná hodnota pi // nefunguje
n = 10
a = 1/1
b = 1
for i in range(n):
    b -= a
    a += 1/1+2
    b += a
    a += 1/2
    print(b)