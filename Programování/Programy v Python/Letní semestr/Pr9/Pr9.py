def power2(n):
    """Funkce pro druhou mocninu."""
    return n*n

def char_to_number(char):
    """Převede znak na číslo."""
    return int(char)

def number_to_char(number):
    return str(number)

def power_numbers(entry, new):
    """Vloží umocněná čísla do nového souboru."""
    entry_file = open(entry, "r")
    try:
        new_file = open(new, "w")
        try:
            line = entry_file.readline() 
            while line != '':
                number = power2(char_to_number(line))
                new_file.write(number_to_char(number))
                new_file.write("\n")
                line = entry_file.readline()
        finally:
            new_file.close()
    finally:
        entry_file.close()

def error_check(entry, new):
    """Zkontroluje, zda se v zadaných souborech vyskytují chyby."""
    error = 0
    power_numbers(entry, new)
    try:
        entry_file = entry.open()
    except RuntimeError:
        error = 1
        print("Špatně zadaný název souboru.")
    try:
        new_file = new.open()
        try:
            line = new_file.readline()
        except TypeError:
            error = 1
            print("Chyba typu." + line)
        except ValueError:
            error = 1
            print("Chyba hodnoty." + line)
        finally:
            new.file.close()
    finally:
        if error == 0:
            print("Funkce se ukončila správně.")
        else:
            print("Funkce skončila chybou.")
        entry_file.close()

entry_file = input("Zadejte zdrojový soubor: ")
new_file = input("Zadejte název cílového souboru: ")

power_numbers(entry_file, new_file)
#error_check(entry_file, new_file)