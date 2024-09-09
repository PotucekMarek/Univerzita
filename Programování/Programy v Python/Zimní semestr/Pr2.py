# 1)
x = 0

if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)

# 2)
x = 10

if x <= 2:
     print(5)
elif x == 3 and 4:
    print(4)
elif x == 5 and 6:
    print(3)
elif x == 7 and 8:
    print(2)
else:
    print(1)

# 3) Zařaďte 3 čísla podle velikosti
a = 1
b = 20
c = 28

if a > b and a > c:
    print(a)
    if b > c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
    
elif b > a and b > c:
    print(b)
    if a > c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)

elif c > a and c > b:
    print(c)
    if a > b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)

# 4) 
a = 6
b = 12
c = 7

if (a + b > c) and (a + c > b) and (b + c > a):
    print('ano')
else:
    print('no')

# 5)
a = 10
b = 20
c = 30
d = 40

if (d - c) == a:
    if (c - b) == a:
        if( b - a) == a:
            print('ano')
else:
    print('ne')

 # 6)
a = 60
b = 20
c = 100

if a + b + c == 180:
    if (a == 90) or (b == 90) or (c == 90):
        print('pravouhly')
    elif (a > 90) or (b > 90) or (c > 90):
        print('tupouhly')
    else:
        print('ostry')
else:
    print('neni trojuhelnik')

# 7)
a = 25
b = 20
c = 15
d = 10
x = -5 # diferencial

if (a + x == b) and (b + x == c) and (c + x == d):
    print(True)
else:
    print(False)
