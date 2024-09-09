#1) prázdná tabulka
def make_empty_table():
    return []


# 2 Vrátí řádek tabulky
def get_table_row(table, row_number):
    return table[row_number]                    #vrací řádek tabulky podle indexu(row_number)

#print(get_table_row([[1, 'a'], [2, 'b']], 0))


# 3 Vrátí počet řádků
def get_table_row_count(table):
    return len(table)                           # len -> vrací délku argumentu

#print(get_table_row_count([[1, 'a'], [2, 'b']]))


# 4 Vrátí buňku seznam[index]
def get_row_cell(row, column):
    return row[column]

#print(get_row_cell([1, 'a', True], 1))


# 5 Vrátí počet buněk na řádku
def get_row_cell_count(row):
    return len(row)

#print(get_row_cell_count([1, 'a', True]))


# 6  Vrátí buňku, použít get_table_row get_row_cell
def get_table_cell(table, row_number, column):
    row = get_table_row(table, row_number)      # uloží do proměnné řádek zadané hodnoty(row_number)
    return get_row_cell(row, column)          # funce get_row_cell vrací buňku na základě zadaného sloupce a řádku

#print(get_table_cell([[1, 'a'], [2, 'b']], 1, 1))


# 7  buňky oddělit tabulátorem, použít funkce -> get_row_cell_count(row), get_row_cell(row, column)
def print_row(row):
    for i in range(get_row_cell_count(row)):    # cyklus prochází všechny buňky na jednom řádku
        print(get_row_cell(row, i),end='\t')  # vytiskne jednotlivé buňky na řádku oddělené tabulátorem
                             
#print_row([1, 'a', True])


# 8 vytvoří tabulku, použít funkce -> get_table_row(table, row_number), get_table_row_count(table), print_row(row)
def print_table(table):
    for i in range(get_table_row_count(table)): # cyklus prochází tabulku
        row = get_table_row(table, i)           # do proměnné vloží řádek
        print_row(row)                          # funkce print_row vytiskne buňky oddělené tabulátorem
        print()                                 # odřádkování

#print_table([[1, 'a'], [2, 'b']])

# 9 spojí dva řádky do jednoho
def join_rows(row1, row2):
    return row1 + row2                           # do prázdného seznamu vloží dva řádky
   

#print(join_rows([1, 2], ['a']))

# 10 přidá řádek na konec tabulky
def add_row_to_table(table, row):
    return table + [row]                         # do proměnné vloží tabulku, k ní přičte řádek
    

#print(add_row_to_table([[1, 2], [3, 4]], [5, 6]))

# 11 funkce spojí všechny řádky table1 s table2, použít funkce -> make_empty_table, get_table_row_count ,get_table_row ,join_rows a add_row_to_table¨
def product(table1, table2):
    table = make_empty_table()                                                      # do proměnné vloží prázdný seznam
    for i in range(get_table_row_count(table1)):                                    # cyklus prochází první tabulku
        for j in range(get_table_row_count(table2)):                                # cyklus prochází první tabulku
            row = join_rows(get_table_row(table1, i), get_table_row(table2, j))     # do proměnné vloží dva spojené řádky z první a druhé tabulky                                  
            table = add_row_to_table(table, row)
    return table

#print_table(product([[1, 20], [2, 3], [3, 1]], [['a', True], ['b', False]]))