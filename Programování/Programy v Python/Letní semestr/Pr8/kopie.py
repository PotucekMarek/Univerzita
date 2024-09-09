while True:
  counter = 0
  counter_two = 0

  def open_source_file(file):
      """Otevře zdrojovou složku"""
      return open(file)

  def open_target_file(file):
      """Otevře cílovou složku"""
      return open(file, 'w')   

  def close_file(file):
      """Zavře složku"""
      file.close()

  def transform_line(line):
      """Převod řádku"""
      global counter
      line = line.splitlines()
      boole = line[0].isdigit()
      if not boole:
        counter += 1
        return False
      transform_number = line[0]
      transform_number = int(transform_number)
      return transform_number

  def powering_number(number, file_to):
        global counter_two
        if number > 0:
            number = number ** 2
            file_to.write(str(number) + "\n")
            counter_two += 1
        return number

  def power_numbers(source, target):
      """Zapíše do souboru target pouze čísla, která splňují predikát."""
      global counter
      global counter_two
      try:
        input_file = open_source_file(source)
      except FileNotFoundError:
        counter += 1
        print("Složka, kterou jste zadal neexistuje")
        raise RuntimeError("Složka, kterou jste zadal neexistuje.")
        # return False
      except:
        counter += 1
        raise RuntimeError('Nelze načíst obsah souboru ' + source)
        # return False
      try:
          try:
            output_file = open_target_file(target)
            try:
              line = input_file.readline()
              print(line)
            except TypeError:
              raise RuntimeError('Chyba typu')
            except ValueError:            
              raise RuntimeError('Chyba hodnoty')
            except:
              raise RuntimeError("Chybí přípona, nebo něco jiného.")
            try:
              while line != '':
                  try:
                    number = transform_line(line)
                    print(number)
                    if number == False:
                          return False
                  except ValueError:
                    counter += 1
                    raise RuntimeError('Chyba hodnoty')
                  except ValueError:
                    counter += 1
                    raise TypeError('Chyba typu')
                  except:
                    raise RuntimeError("Chyba.")
                  try:
                    if number > 0:
                        number = number ** 2
                        output_file.write(str(number) + "\n")
                        counter_two += 1
                  except:
                    counter += 1
                    raise RuntimeError('Chyba v přiřazení hodnoty.')
                  line = input_file.readline() 
            except:
              counter += 1
              print("Chyba v zapsání před uložením proměnné")
              return False
          except:
            counter += 1
            print("Při otevírání složky došlo k chybě.")
            return False
          finally:
              close_file(output_file)
      finally:
        if counter == 0:
          print("---> Program skončil úspěšně.")
          close_file(input_file)
        if (counter != 0) or (counter_two == 0):
          print("---> Program skončil neúspěšně!")

  # V případě, že budete chtít vyzkoušet funkcční verzi zavolejte Soubor s název numbers2.txt a když budete chtít vyzkoušet špatný test, tak zavolejte soubor s názvem txt.txt.
  print("Budete zadávat zdrojový a cílový soubor.")
  print('.')
  print('.')
  print('.')
  print('\v')
  try:
    source_file = input('Zdrojový soubor s příponou .txt: ')
    target_file = input('Cílový soubor s příponou .txt: ')
  except NameError:
    print("Variable x is not defined")
  except:
    print("Something else went wrong")
  power_numbers(source_file, target_file)