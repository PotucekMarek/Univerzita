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