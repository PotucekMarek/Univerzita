def count_numbers(name):
    file = open(name)
    try:
        line = file.readline()
        count = 0
        while line != "":
            count += int(line)
            line = file.readline()
        print(count)
    finally:
        file.close()

count_numbers("file.txt")