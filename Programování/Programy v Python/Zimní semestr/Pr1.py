# 1)
a = 5
b = 6

print(2*(a+b))
print(a*b)

# 2)
a = 2
print(a**2*6)

# 3)
seconds = 5
minutes = 6
hours = 7
days = 8

result = seconds + minutes * 60 + hours * 60 ** 2 + days * 60 ** 2 * 24
print(result)

# 4)
distance = 5
speed = 299792458
AU = 49597870700 

result = distance * AU // speed
print(result)

# 5)
a = 6
b = 10

result = (a + b) % 2
print(result)

# 6)
a = 7

result = a % 2
print(-result+1)

# 7)
a = 105

result = a % 3 + a % 7 + a % 5
print(result)

# 8)
a = 456
b = 321

result = a * 1000 + b
print(result)

# 9)
a = 456

result = a // 100
print(result)

result2 = a // 10
result2 %= 10
print(result2)

a %= 100
a %= 10
print(a) 

# 10)
a = 456

first = a // 100

b = a % 100
last = b % 10

b = a // 10
mid = b % 10

result = last * 100 + mid * 10 + first

print(result)

# 11)
a = 5555

first = a // 1000

b = a % 1000
second = b // 100

b = a % 100
third = b // 10

last = a % 10

result = (first - last) + (second - third)

print(result)

# 12)
a = 1111

first = a // 1000

b = a % 1000
second = b // 100

b = a % 100
third = b // 10

last = a % 10

result = first * 2 ** 3 + second * 2 ** 2 + third * 2 + last

print(result)

# 13) i have no idea
a = 15

while 0 != a:
     result = a % 2
     a = a // 2
     print(result)
    
# 14)
a = 29

result = a % 3
a = a - result 

print(a)











