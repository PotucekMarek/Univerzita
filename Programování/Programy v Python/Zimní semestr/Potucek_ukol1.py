from random import randint

# Insertion sort
def insertion_sort(array):
    global swap_ins
    global comparison_ins
    for j in range(len(array)):
        t = array[j]
        i = j - 1
        comparison_ins += 1
        while 0 <= i and t < array[i]:
            array[i + 1] = array[i]
            swap_ins += 1
            comparison_ins += 1
            i -= 1
        array[i + 1] = t

# Heap sort
def left(i):
    l = 2 * i + 1
    return l

def right(i):
    r = 2 * i + 2
    return r

def max_heapify (array, i, heapsize):
    global swap_heap
    global comparison_heap
    l = left(i)
    r = right(i)

    comparison_heap += 1
    if (l <= heapsize - 1) and (array[l] > array[i]):
        largest = l
    else:
        largest = i

    comparison_heap += 1
    if (r <= heapsize - 1) and (array[r] > array[largest]):
        largest = r

    comparison_heap += 1
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        swap_heap += 1
        max_heapify(array, largest, heapsize)

def build_max_heap(array, heapsize):
    for i in range((heapsize//2) , -1, -1):
        max_heapify(array, i, heapsize)

def heap_sort(array, heapsize):
    build_max_heap(array, heapsize)
    for i in range(heapsize - 1, 0, -1): 
        t = array[0]
        array[0] = array[i]
        array[i] = t
        heapsize -= 1
        max_heapify(array, 0, heapsize) 

# Quick sort

def quick_sort (array, p, r):
    global comparison_quick
    comparison_quick += 1
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)

def partition (array, p, r):
    global swap_quick   
    global comparison_quick
    x = array[r]
    i = p - 1
    for j in range(p, r):
        comparison_quick += 1
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i] 
            swap_quick += 1  
    array[i + 1], array[r] = array[r], array[i + 1]
    swap_quick += 1
    return i + 1


print("###Porovnání###")
print("Alg / Pole\t10\t100\t1000\t10000")

# insertion sort pro velikost pole 10
swap_ins = 0
comparison_ins = 0
ARRAY_LENGHT = 10
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
insertion_sort(array)
print("Insertion sort:\t",comparison_ins, end='\t')

# insertion sort pro velikost pole 100
comparison_ins = 0
ARRAY_LENGHT = 100
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
insertion_sort(array)
print(comparison_ins,end="\t")

# insertion sort pro velikost pole 1000
comparison_ins = 0
ARRAY_LENGHT = 1000
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
insertion_sort(array)
print(comparison_ins,end="\t")

# insertion sort pro velikost pole 10000
ARRAY_LENGHT = 10000
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
insertion_sort(array)
print(comparison_ins)

# heap sort pro velikost pole 10
swap_heap = 0
comparison_heap = 0
ARRAY_LENGHT = 10
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
heap_sort(array, ARRAY_LENGHT)
print("Heap sort: \t",comparison_heap, end='\t')

# heap sort pro velikost pole 100
comparison_heap = 0
ARRAY_LENGHT = 100
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
heap_sort(array, ARRAY_LENGHT)
print(comparison_heap,end="\t")

# heap sort pro velikost pole 1000
comparison_heap = 0
ARRAY_LENGHT = 1000
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
heap_sort(array, ARRAY_LENGHT)
print(comparison_heap,end="\t")

# heap sort pro velikost pole 10000
comparison_heap = 0
ARRAY_LENGHT = 10000
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
heap_sort(array, ARRAY_LENGHT)
print(comparison_heap)

# quick sort pro velikost pole 10
swap_quick = 0
comparison_quick = 0
ARRAY_LENGHT = 10
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
p = 0
r = ARRAY_LENGHT-1
quick_sort(array, p, r)
print("Quick sort: \t",comparison_quick, end='\t')

# quick sort pro velikost pole 100
comparison_quick = 0
ARRAY_LENGHT = 100
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
p = 0
r = ARRAY_LENGHT-1
quick_sort(array, p, r)
print(comparison_quick,end="\t")

# quick sort pro velikost pole 1000
comparison_quick = 0
ARRAY_LENGHT = 1000
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
p = 0
r = ARRAY_LENGHT-1
quick_sort(array, p, r)
print(comparison_quick,end="\t")

# quick sort pro velikost pole 10000
comparison_quick = 0
ARRAY_LENGHT = 10000
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
p = 0
r = ARRAY_LENGHT-1
quick_sort(array, p, r)
print(comparison_quick)

# přesuny
print()
print("###Přesuny###")
print("Alg / Pole\t10\t100\t1000\t10000")

# insertion sort o velikosti pole 10 pro přesuny
swap_ins = 0
ARRAY_LENGHT = 10
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
insertion_sort(array)
print("Insertion sort:\t",swap_ins, end='\t')

# insertion sort o velikosti pole 100 pro přesuny
swap_ins = 0
ARRAY_LENGHT = 100
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
insertion_sort(array)
print(swap_ins,end="\t")

# insertion sort o velikosti pole 1000 pro přesuny
swap_ins = 0
ARRAY_LENGHT = 1000
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
insertion_sort(array)
print(swap_ins,end="\t")

# insertion sort o velikosti pole 10000 pro přesuny
ARRAY_LENGHT = 10000
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
insertion_sort(array)
print(swap_ins)

# heap sort o velikosti pole 10 pro přesuny
swap_heap = 0
ARRAY_LENGHT = 10
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
heap_sort(array, ARRAY_LENGHT)
print("Heap sort: \t",swap_heap, end='\t')

# heap sort o velikosti pole 100 pro přesuny
swap_heap = 0
ARRAY_LENGHT = 100
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
heap_sort(array, ARRAY_LENGHT)
print(swap_heap,end="\t")

# heap sort o velikosti pole 1000 pro přesuny
swap_heap = 0
ARRAY_LENGHT = 1000
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
heap_sort(array, ARRAY_LENGHT)
print(swap_heap,end="\t")

# heap sort o velikosti pole 10000 pro přesuny
swap_heap = 0
ARRAY_LENGHT = 10000
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
heap_sort(array, ARRAY_LENGHT)
print(swap_heap)

# quick sort o velikosti pole 10 pro přesuny
swap_quick = 0
ARRAY_LENGHT = 10
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
p = 0
r = ARRAY_LENGHT-1
quick_sort(array, p, r)
print("Quick sort: \t",swap_quick, end='\t')

# quick sort o velikosti pole 100 pro přesuny
swap_quick = 0
ARRAY_LENGHT = 100
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
p = 0
r = ARRAY_LENGHT-1
quick_sort(array, p, r)
print(swap_quick,end="\t")

# quick sort o velikosti pole 1000 pro přesuny
swap_quick = 0
ARRAY_LENGHT = 1000
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
p = 0
r = ARRAY_LENGHT-1
quick_sort(array, p, r)
print(swap_quick,end="\t")

# quick sort o velikosti pole 10000 pro přesuny
swap_quick = 0
ARRAY_LENGHT = 10000
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
p = 0
r = ARRAY_LENGHT-1
quick_sort(array, p, r)
print(swap_quick)