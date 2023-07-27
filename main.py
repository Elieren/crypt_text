from colorama import Fore, Style
import random
import string
try:
    from key import KEY
except Exception:
    pass


class Encode():
    def __init__(self):
        self.__rus = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З",
                      "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р",
                      "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ",
                      "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

        self.__eng = ["A", "B", "C", "D", "E", "F", "G",
                      "H", "I", "J", "K", "L", "M", "N",
                      "O", "P", "Q", "R", "S", "T", "U",
                      "V", "W", "X", "Y", "Z"]

        self.__numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        self.__probel = [" "]

        self.__znaki = [",", ".", "!", "?", '"', "@", "№", "#", "$",
                        ";", "%", "^", ":", "&", "*", "(", ")", "-",
                        "_", "+", "=", "{", "}", "[", "]", "'", ">",
                        "<", "/", "\\"]

        for i in [self.__rus, self.__eng]:
            temporary = []
            for x in i:
                temporary.append(x.lower())
            i.extend(temporary)

        self.__full = self.__rus + self.__eng + self.__numbers + \
            self.__probel + self.__znaki

        try:
            self.__baza = KEY
        except Exception:
            pass

    def __encodeing(self):
        for i in self.__text_list:
            for x, z in enumerate(self.__full):
                if i in z:
                    self.__encode_text += f"{self.__baza[x]}"
                else:
                    pass

    def __decoding(self):
        self.__decode_key = [self.__key[i:i + self.__length_key]
                             for i in range(0, len(self.__key),
                             self.__length_key)]

        for i in self.__decode_key:
            for x, b in enumerate(self.__baza):
                if b in i:
                    self.__decode_len += f"{self.__full[x]}"

                else:
                    pass
        if self.__len_text == self.__decode_len:
            self.__decode_text_key = [self.__code_text[i:i + self.__length_key]
                                      for i in range(0, len(self.__code_text),
                                      self.__length_key)]

            for i in self.__decode_text_key:
                for x, b in enumerate(self.__baza):
                    if b in i:
                        self.__decode_text += f"{self.__full[x]}"
                    else:
                        pass
        else:
            self.__decode_text = "Error. The key doesn't fit."

    def encode(self, text):
        self.__text = str(text)
        self.__text_list = list(self.__text)

        self.__encode_text = ''

        self.__encodeing()

        text_len = str(len(self.__encode_text))
        self.__encode_text += '|'

        for i in text_len:
            x = 118
            for n in self.__full[118:128]:
                if i in n:
                    self.__encode_text += f'{self.__baza[x]}'
                else:
                    pass
                x += 1

        return self.__encode_text

    def decode(self, text, length_key):
        self.__text = str(text).split('|')
        self.__length_key = length_key
        self.__code_text = self.__text[0]
        self.__len_text = str(len(self.__text[0]))
        self.__key = self.__text[1]

        self.__decode_len = ''
        self.__decode_text = ''

        self.__decoding()

        return self.__decode_text

    def create_key(self):
        key = []
        length = 5

        for i in range(163):
            letters_and_digits = string.ascii_letters + string.digits
            rand_string = ''.join(random.sample(letters_and_digits, length))
            key.append(rand_string)

        f = open('key.py', 'w')  # открытие в режиме записи
        f.write('KEY = ')
        f.write('[')
        for i in key:
            f.write(f"'{i}',")  # запись x в файл
        f.write(']')
        f.close()


banner = """
███████╗ ██████╗██████╗  █████╗ ███╗   ███╗██████╗ ██╗     ███████╗██████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗
███████╗██║     ██████╔╝███████║██╔████╔██║██████╔╝██║     █████╗  ██████╔╝
╚════██║██║     ██╔══██╗██╔══██║██║╚██╔╝██║██╔══██╗██║     ██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║  ██║██║ ╚═╝ ██║██████╔╝███████╗███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
"""

print(Fore.GREEN + banner)

var = str(input(Fore.GREEN + "(S) - Scrambler, (D) - Decoder, \
(C) - Create key: " + Style.RESET_ALL))

var = var.upper()

encoding = Encode()

if var == 'S':
    text = input(': ')
    encode_text = encoding.encode(text)
    print(encode_text)

elif var == 'D':
    text = input(': ')
    decode_text = encoding.decode(text, 5)
    print(decode_text)

elif var == 'C':
    encoding.create_key()
