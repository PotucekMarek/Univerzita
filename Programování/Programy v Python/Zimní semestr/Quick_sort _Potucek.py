from random import randint
ARRAY_LENGHT = 100


def quick_sort (array, p, r):
    global comparison
    comparison += 1
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)

def partition (array, p, r):
    global swap
    global comparison
    x = array[r]
    i = p - 1
    for j in range(p, r):
        comparison += 1
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]   
    array[i + 1], array[r] = array[r], array[i + 1]
    swap += 1
    return i + 1

comparison = 0
swap = 0

array = [randint(0,999) for i in range(ARRAY_LENGHT)]
print("Zadané pole:", array)
p = 0
r = len(array)-1
quick_sort(array, p, r)
print("Setříděné:",array)
print('Number of swaps is:', swap)
print('Number of comparisons is:', comparison)

# Potůček Marek