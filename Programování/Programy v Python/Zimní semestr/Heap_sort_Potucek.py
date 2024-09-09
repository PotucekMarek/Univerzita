from random import randint
ARRAY_LENGHT = 10

def left(i):
    l = 2 * i + 1
    return l

def right(i):
    r = 2 * i + 2
    return r

def max_heapify (array, i, heapsize):
    global swaps
    global comparison
    l = left(i)
    r = right(i)

    comparison += 1
    if (l <= heapsize - 1) and (array[l] > array[i]):
        largest = l
    else:
        largest = i

    comparison += 1
    if (r <= heapsize - 1) and (array[r] > array[largest]):
        largest = r

    comparison += 1
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        swaps += 1
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

swaps = 0
comparison = 0
array = [randint(0,999) for i in range(ARRAY_LENGHT)]

heap_sort(array, ARRAY_LENGHT)
print(array)
print('Number of swaps is:', swaps)
print('Number of comparisons is:', comparison)