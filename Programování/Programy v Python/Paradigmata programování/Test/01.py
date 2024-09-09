FIRST_STRUCT_ROW = 3
FIRST_STRUCT_COLUMN = 4

SECOND_STRUCT_INDEX = 0
SECOND_STRUCT_ROW_NEXT_INDEX = 1
SECOND_STRUCT_COLUMN_NEXT_INDEX = 2

THIRD_STRUCT_NEXT_VALUE_INDEX = 3


Def create_first_struct(values, m, n):
    Matrix = [None, m, n, [], []]
    Matrix[FIRST_STRUCT_ROW].extend(create_second_struct(
        Matrix, m, SECOND_STRUCT_ROW_NEXT_INDEX, values))
    Matrix[FIRST_STRUCT_COLUMN].extend(create_second_struct(
        Matrix, n, SECOND_STRUCT_COLUMN_NEXT_INDEX, values))

    Return matrix


Def create_second_struct(matrix, row_column_count, struct_next_index, values):

    For index in range(row_column_count):
        If index < row_column_count – 1:
            If index == 0:
                Second_struct = [index, [], []]
            Else:
                Second_struct[struct_next_index].extend([index, [], []])
        Else:
            If struct_next_index == 1:
                Second_struct[struct_next_index].extend(
                    [index, matrix, []])
            Else:
                Second_struct[struct_next_index].extend(
                    [index, [], matrix])

    Return second_struct


Def create_third_struct(values, row_index, column_index, m):
    Third_struct = []

    For value_index in range(len(values)):
        If values[value_index] != 0:
            Third_struct.extend(
                [values[value_index], row_index, column_index, [], []])
        Elif values[check_next_columns_for_value(values, value_index, m)] == 0:
            Pass
        Else:
            Index = values[check_next_columns_for_value(
                Values, value_index, m)]
            Third_struct[THIRD_STRUCT_NEXT_VALUE_INDEX].extend(
                [values[index], row_index, column_index, [], []])

    Return third_struct


Def make_third_struct(values, m, n):
    “””[hodnota, rowIndex, columnIndex, nextRow, nextColumn]”””

    Structures = []
    Value_index = 0
    For row in range(m):
        For column in range(n):
            Third_struct = [values[value_index], row, column, [], []]
            Value_index += 1
            Structures += [third_struct]
    Return structures


Struct = make_third_struct([0, 1, 0, 0, 2, 3, 0, 0, 4], 3, 3)
        
Def connect_third_structures(structures, m, n):
    “””spojí 3. Struktuy do sebe”””
    NEXT_ROW = 3
    NEXT_COLUMN = 4
    Third_struct_columns = []
    Third_struct = []
    Index = 0

    For row in range(m):
        For column in range(n):
            If index == 0:
                Third_struct_columns = structures[index]
                Third_struct = structures[index]
            Else:
                Third_struct_columns[NEXT_COLUMN].extend(third_struct[index]) 
            Index += 1    
        Third_struct[NEXT_ROW].extend(third_struct_columns)
    Return third_struct

#print(connect_third_structures(struct, 3, 3))
Print(struct)

Def check_next_columns_for_value(values, values_column_index, step):
    Column_index = values_column_index
    While values_column_index < len(values):
        If values[values_column_index] != 0:
            Return values_column_index
        Values_column_index += step
    Return column_index


Values = [0, 1, 0, 0, 2, 3, 0, 0, 4]
Second_struct = create_second_struct([None, 2, 2, [], []], 2, 2, values )
Third_struct = create_third_struct(values, 0, 1, 3)


#print([1, 0, 1, [[2, 1, 1, [], []]], []])
#print(third_struct)


Matrix = create_first_struct([0, 1, 0, 2], 2, 2)
Print(“[None, 2, 2, [0, [1, [...], []], []], [0, [], [1, [], [...]]]]”)
Print(matrix)
