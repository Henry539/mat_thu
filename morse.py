morse_dict1 = {".-": "A", "-...": 'B', "-.-.": 'C', '-..': 'D', '.': 'E', "..-.": "F", '--.': 'G', '....': 'H',
               '..': 'I', ".---": 'J', "-.-": "K", ".-..": "L", "--": 'M', "-.": 'N', "---": 'O', ".--.": 'P',
               "--.-": "Q", ".-.": "R", "...": 'S', "-": 'T', "..-": 'U', "...-": 'V', ".--": 'W', "-..-": 'X',
               "-.--": 'Y', "--..": 'Z', ".--.-": 'Â', "-..-.": 'Ê', "---.": 'Ô', "/": ' '}

morse_dict2 = {"A": ".-", 'B': "-...", 'C': "-.-.", 'D': '-..', 'E': '.', "F": "..-.", 'G': '--.', 'H': '....',
               'I': '..', 'J': ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
               "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
               "Y": "-.--", "Z": "--..", "Â": ".--.-", "Ê": "-..-.", "Ô": "---.", " ": '/'}


def morse1():
    matThu = input('MT: ').split()
    list_morse = [x for x in morse_dict1.keys()]

    bachVan = []
    for tu in matThu:
        if tu in list_morse:
            bachVan.append(morse_dict1[tu])

    result = ''.join(bachVan)
    return result


def morse2():
    matThu = list(map(str, input('MT: ').upper()))
    list_morse = [x for x in morse_dict2.keys()]

    bachVan = []
    for tu in matThu:
        if tu in list_morse:
            bachVan.append(morse_dict2[tu])

    result = ' '.join(bachVan)
    return result


choose = input('1-morse or 2-matthu: ')
result = ""
string = "xox"
while True:
    if string == "":
        break
    string = ""
    if choose == '1':
        string += morse1()
    elif choose == '2':
        string += morse2()
    result += string
    print(string)

print("BACH VAN LA: ", result)
input("THANK YOU")
