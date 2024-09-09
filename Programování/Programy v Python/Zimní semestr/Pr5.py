# 1) reverse
string = 'oko'
reverse = ''

for i in range(len(string)):
    reverse = string[i] + reverse
print(reverse)

# 2) palindrom
string = 'kobylamamalybok'
reverse = ''

for i in range(len(string)):
    reverse = string[i] + reverse
is_palindrom = string == reverse
print(is_palindrom)

# 3) převod malých písmen na velká
string = 'python'
upper = ''
result = ''
for i in range(len(string)):
    upper = ord(string[i]) - 32
    result += chr(upper)
print(result)

# 4) převod řetězce na číslo
string = '131'
number = 0
digit = 0
result = 0

for i in range(len(string)):
    number = string[i]
    digit = ord(number) - 48
    result *= 10
    result += digit
print(result)

# 5) převod čísla na řetězec
number = 100
string = ''
n = number

while n > 0:
    digit = n % 10
    n //= 10
    char = chr(digit + 48)
    string = char + string

print(string)

# 6) odstranit mezery
string = 'cibule ananas brokolice   jablko'
norm_string = ''

for i in range(len(string)):
    char = string[i]
    ord_char = ord(char)
    if ord('a') <= ord_char and ord_char <= ord('z'):
        norm_string += chr(ord_char)
print(norm_string)

# 7) odstranit mezery a velka písmena
string = 'Kobyla ma maly bok'
norm_string = ''

for i in range(len(string)):
    char = string[i]
    ord_char = ord(char)
    if ord('A') <= ord(char) and ord(char) <= ord('Z'):
        ord_char += 32
    if ord('a') <= ord_char and ord_char <= ord('z'):
        norm_string += chr(ord_char)
print(norm_string)

# 7) slova z věty pod sebe
string = 'cibule ananas ahoj'
word = ''

for i in range(len(string)):
    char = string[i]
    if char == ' ':
        print(word)
        word = ''
    else:
        word += char
if word != '':
    print(word)

# 8) odstraní víc mezer ve větě
string = 'kobyla   ma        maly  bok'
word = ''
result = ''

for i in range(len(string)):
    char = string[i]
    if char != ' ':
        word += char
    elif word != '':
        if result != '':
            result += ' '
        result += word
        word = ''
if word != '':
    result += ' ' + word 
    print(result)

# 9) indexy zadaného znaku //nefuguje
string = 'pštros a pštrosice šli do pštrosičárny'
index = 'p'

for i in range(len(string)):
    char = string[i]
    if char == 'p':
        count = string[i]
        print(count)
