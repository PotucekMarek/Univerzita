FIRST_STRUCT_ROW = 3
FIRST_STRUCT_COLUMN = 4

SECOND_STRUCT_INDEX = 0
SECOND_STRUCT_ROW_NEXT_INDEX = 1
SECOND_STRUCT_COLUMN_NEXT_INDEX = 2

THIRD_STRUCT_NEXT_VALUE_INDEX = 3


def create_first_struct(values, m, n):
    matrix = [None, m, n, [], []]
    matrix[FIRST_STRUCT_ROW].extend(create_second_struct(
        matrix, m, SECOND_STRUCT_ROW_NEXT_INDEX, values))
    matrix[FIRST_STRUCT_COLUMN].extend(create_second_struct(
        matrix, n, SECOND_STRUCT_COLUMN_NEXT_INDEX, values))

    return matrix


def create_second_struct(matrix, row_column_count, struct_next_index, values):

    for index in range(row_column_count):
        if index < row_column_count - 1:
            if index == 0:
                second_struct = [index, [], []]
            else:
                second_struct[struct_next_index].extend([index, [], []])
        else:
            if struct_next_index == 1:
                second_struct[struct_next_index].extend(
                    [index, matrix, []])
            else:
                second_struct[struct_next_index].extend(
                    [index, [], matrix])

    return second_struct


def create_third_struct(values, row_index, column_index, m):
    third_struct = []

    for value_index in range(len(values)):
        if values[value_index] != 0:
            third_struct.extend(
                [values[value_index], row_index, column_index, [], []])
        elif values[check_next_columns_for_value(values, value_index, m)] == 0:
            pass
        else:
            index = values[check_next_columns_for_value(
                values, value_index, m)]
            third_struct[THIRD_STRUCT_NEXT_VALUE_INDEX].extend(
                [values[index], row_index, column_index, [], []])

    return third_struct


def make_third_struct(values, m, n):
    """[hodnota, rowIndex, columnIndex, nextRow, nextColumn]"""

    structures = []
    value_index = 0
    for row in range(m):
        for column in range(n):
            third_struct = [values[value_index], row, column, [], []]
            value_index += 1
            structures += [third_struct]
    return structures


struct = make_third_struct([0, 1, 0, 0, 2, 3, 0, 0, 4], 3, 3)
        
def connect_third_structures(structures, m, n):
    """spojí 3. struktuy do sebe"""
    NEXT_ROW = 3
    NEXT_COLUMN = 4
    third_struct_columns = []
    third_struct = []
    index = 0

    for row in range(m):
        for column in range(n):
            if index == 0:
                third_struct_columns = structures[index]
                third_struct = structures[index]
            else:
                third_struct_columns[NEXT_COLUMN].extend(third_struct[index]) 
            index += 1    
        third_struct[NEXT_ROW].extend(third_struct_columns)
    return third_struct

#print(connect_third_structures(struct, 3, 3))
print(struct)

def check_next_columns_for_value(values, values_column_index, step):
    column_index = values_column_index
    while values_column_index < len(values):
        if values[values_column_index] != 0:
            return values_column_index
        values_column_index += step
    return column_index


values = [0, 1, 0, 0, 2, 3, 0, 0, 4]
second_struct = create_second_struct([None, 2, 2, [], []], 2, 2, values )
third_struct = create_third_struct(values, 0, 1, 3)


#print([1, 0, 1, [[2, 1, 1, [], []]], []])
#print(third_struct)


matrix = create_first_struct([0, 1, 0, 2], 2, 2)
print("[None, 2, 2, [0, [1, [...], []], []], [0, [], [1, [], [...]]]]")
print(matrix)
