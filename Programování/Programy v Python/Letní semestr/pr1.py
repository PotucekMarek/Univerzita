def list_map(function, lst):
    result = []
    for el in lst:
        new_el = function(el)
        result += [new_el]
    return result

def succesor(num):
    return num + 1

def square(num):
    return num ** 2

def map_succesor(lst):
    return list_map(succesor, lst)

def map_square(lst):
    return list_map(square, lst)

print(map_square([1,2,3,4,5]))
print(map_succesor([1,2,3,4,5]))

# 1) map_abs

def map_abs(lst):
    return list_map(abs, lst)

print(map_abs([-1,2,5]))

# 2) map_len

def map_len(lst):
    return(list_map(len, lst))

print(map_len([[-1,2,5], [], [3]]))

# 3) map_matrix_suc matrix -> matice, suc -> succesor
# map_matrix_suc([1,2],[0,1]) = [2,3],[1,2]
def row_succesor(lst):
    return list_map(succesor, lst)

def map_matrix_suc(matrix):
    return list_map(row_succesor, matrix)

print(map_matrix_suc([[-1,2,5],[2,5,5]]))


# filters

def list_filter(predicate, lst):
    result = []
    for el in lst:
        if predicate(el):
            result += [el]
    return result

def is_even(num):
    return num % 2 == 0

def is_small(num):
    return num <= 1

def filter_even(lst):
    return list_filter(is_even,lst)

print(filter_even([1,2,3,4,5]))

def filter_small(lst):
    return list_filter(is_small,lst)

print(filter_small([1,2,3,-1,0,-5,5]))

def is_empty(num):
    return num != []

# 4)
def filter_nonempty(lst):
    return list_filter(is_empty,lst)

print(filter_nonempty([[1,2,3],[],[5,2],[]]))

# 5) list_possitive_square(1,3,-3,5) = 1, 9, 25
def is_possitive(num):
    return num > 0

def filter_possitive(lst):
    return list_filter(is_possitive, lst)

def list_possitive_square(lst):
    return (map_square(filter_possitive(lst)))

print(list_possitive_square([1,-2,3,-3]))

# 7) list_sum[1,2,3,4] = 10, list_product[1,2,3,4] = 24 pomocí list_reduce
neutral_sum = 0
neutral_product = 1

def sum_operation(result, el):
    return result + el

def product_operation(result, el):
    return result * el

def list_reduce(operation,neutral, lst):
    result = neutral
    for el in lst:
        result = operation(result, el)
    return result

def list_sum(lst):
    return list_reduce(sum_operation, neutral_sum, lst)

def list_product(lst):
    return list_reduce(product_operation, neutral_product, lst)


print(list_sum([4,3,2,1]))
print(list_product([4,3,2,1]))

