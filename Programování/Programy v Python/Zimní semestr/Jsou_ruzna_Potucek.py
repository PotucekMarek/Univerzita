from random import randint
ARRAY_LENGHT = 5

def jsou_ruzna(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                continue
            if array[i] == array[j]:  
                return False
    return True                

array = [randint(0,5) for i in range(ARRAY_LENGHT)]

print(jsou_ruzna(array))