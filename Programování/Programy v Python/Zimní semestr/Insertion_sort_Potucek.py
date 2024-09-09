from random import randint
ARRAY_LENGHT = 100

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

swap_ins = 0
comparison_ins = 0
array = [randint(0,999) for i in range(ARRAY_LENGHT)]
print("Nesetříděné pole:",array)
insertion_sort(array)
print(array) 
print('Number of swaps is:', swap_ins)
print('Number of comparisons is:', comparison_ins)