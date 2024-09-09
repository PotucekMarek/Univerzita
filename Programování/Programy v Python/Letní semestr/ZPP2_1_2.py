# 2. zápočtová úloha | Marek Potůček | první skupina | vytvořeno 18.4.2021 | 3.verze
def power2(n):
  """Funkce pro druhou mocninu."""
  return n*n

def char_to_number(line):
  """Převede znak na číslo."""
  return int(line)

def number_to_char(line):
  """Převede číslo na znak."""
  return str(line)

def file_number_map_square(source, target):
  """Vloží umocněná čísla do nového souboru."""
  source_file = open(source)
  try:
    target_file = open(target, "w")
    try:
      line = source_file.readline() 
      while line != '':
        number = power2(char_to_number(line))
        target_file.write(number_to_char(number))
        target_file.write("\n")
        line = source_file.readline()
    finally:
      target_file.close()
  finally:
    source_file.close()

try:
  source = input("Zadejte název zdrojového souboru: ")
  target = input("Zadejte název cílového souboru: ")
  file_number_map_square(source, target)
except TypeError as e:
  print("Chyba typu.", e)
except ValueError as e:
  print("Zdrojový soubor musí obsahovat pouze čísla.", e)
except FileNotFoundError as e:
  print("Zadal jste špatný soubor.", e)
except RuntimeError as e:
  print("Jiná chyba:", e)
else:
  print("Program skončil v pořádku.")