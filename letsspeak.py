letters = input('Give text to translate to leetspeak: ')
letters = letters.upper()

translation = ''

for char in letters:
    if char == "A":
        translation += '4'
    elif char == "E":
        translation += '3'
    elif char == "G":
        translation += '6'
    elif char == "I":
        translation += '1'
    elif char == "O":
        translation += '0'
    elif char == "S":
        translation += '5'
    elif char == "T":
        translation += '7'
    else:
        translation += char
print(translation)