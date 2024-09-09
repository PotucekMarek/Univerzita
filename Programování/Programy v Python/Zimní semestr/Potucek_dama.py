def get_element(num_row, num_column):
    if ((8 * num_row) + num_column) % 2 == 0:
        return 0
    elif num_row < 3:
        return 1
    elif num_row > 4:
        return 2
    else:
        return 0

def make_row(num_row) :
    row = []
    for num_column in range(8):
        element = get_element(num_row, num_column)
        row = row + [element]
    return row

def make_board():
    board = []
    for num_row in range(8):
        row = make_row(num_row)
        board = board + [row]
    return board
    
print(make_board())