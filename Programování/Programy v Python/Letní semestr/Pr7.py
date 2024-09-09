def load_file(name):
    file = open(name)
    try:
        try:
            return file.read()
        finally:
            file.close()
    except:
        raise RuntimeError("Nelze načíst data souboru.")

#load_file("matrix.txt")
x=open('C:\Users\Marek\OneDrive - Univerzita Palackého v Olomouci\Python\Letní semestr\matrix.txt')
x.open