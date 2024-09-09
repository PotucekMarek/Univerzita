def posloupnost(a,b):
    if a >= 0:
        print(a)
        posloupnost(a-b, b)
        global x
        if a < x:
            a += b
            print(a)
x = 10
a = x
posloupnost(a,3)