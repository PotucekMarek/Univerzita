from typing import ValuesView


EMPTY_LIST = []


def deep_copy_matrix_data(data):
    copy = EMPTY_LIST
    for r in data:
        copy += [r[:]]
    return copy

class Matrix:
    def __init__(self):
        self.data = [[1]]
        self.rows = EMPTY_LIST
        self.columns = EMPTY_LIST

    def get_data(self):
        return self.set_data

    def set_data(self, value):
        columns = len(value[0])
        for r in value:
            if len(r) != columns:
                raise ValueError("Pokazils to, heč :P")
        self.data = deep_copy_matrix_data(value)
        return self
    
    def print_matrix(self):
        print(self.data)
        return self
    
    def get_columns(self):
        return len(self.data[0])
    
    def get_rows(self):
        return len(self.data)
    

    
class Methods:
    def __init__(self):
        pass

m1 = Matrix()
m1.set_data([[1,2,3], [3,2,4]])
m1.print_matrix()
m2 = Matrix()
m2.set_data([[5,6,9], [2,3,8]])
m2.print_matrix()