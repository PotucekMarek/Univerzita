# Vypracoval Marek Potůček 18.10.2020

n = 654921408673376804129456 #palindrom
t = n 
ir = 0

# cyklus kde se z t odebírá poslední číslo a přidává do ir dokud t>0
while t > 0:
    n1 = t % 10
    ir = ir * 10 + n1
    t //= 10

# podmínka zda je zadané číslo rovno ir
if (n == ir):
    print('yes, number is palindrom')

else: 
    print('no, number is not palindrom')