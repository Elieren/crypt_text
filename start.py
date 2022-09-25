import colorama
from colorama import Fore, Style
import os
import random
import string

banner = """
███████╗ ██████╗██████╗  █████╗ ███╗   ███╗██████╗ ██╗     ███████╗██████╗      █████╗ ███╗   ██╗██████╗     ██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗    ██╔══██╗████╗  ██║██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
███████╗██║     ██████╔╝███████║██╔████╔██║██████╔╝██║     █████╗  ██████╔╝    ███████║██╔██╗ ██║██║  ██║    ██║  ██║█████╗  ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
╚════██║██║     ██╔══██╗██╔══██║██║╚██╔╝██║██╔══██╗██║     ██╔══╝  ██╔══██╗    ██╔══██║██║╚██╗██║██║  ██║    ██║  ██║██╔══╝  ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║  ██║██║ ╚═╝ ██║██████╔╝███████╗███████╗██║  ██║    ██║  ██║██║ ╚████║██████╔╝    ██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝     ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

print(Fore.GREEN + banner)
print(dev + Style.RESET_ALL)

a = str(input(Fore.GREEN + "(S) - Scrambler, (D) - Decoder, (C) - Create key: " + Style.RESET_ALL))

a = a.upper()

rus = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З",
     "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

eng = ["A", "B", "C", "D", "E", "F", "G",
       "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

probel = [" "]

znaki = [",", ".", "!", "?", '"', "@", "№",
         "#", "$", ";", "%", "^", ":", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "'", ">", "<", "/", "\\"]

over = rus + eng + numbers + probel + znaki

if a == "S":
	from key import KEY

	baza = list()

	baza = KEY

	text = str(input(": "))

	text = text.upper()

	text2 = list(text)

	cod = ""

	for x in text2:
		nom = 0
		for r in rus:
			if x in r:
				cod = cod + f"{baza[nom]}"
			else:
				pass
			nom += 1
		for e in eng:
			if x in e:
				cod = cod + f"{baza[nom]}"
			else:
				pass
			nom += 1
		for n in numbers:
			if x in n:
				cod = cod + f"{baza[nom]}"
			else:
				pass
			nom += 1
		for p in probel:
			if x in p:
				cod = cod + f"{baza[nom]}"
			else:
				pass
			nom += 1
		for z in znaki:
			if x in z:
				cod = cod + f"{baza[nom]}"
			else:
				pass
			nom += 1


	low = len(cod)
	low = str(low)
	cod = cod + "|"

	for x in low:
		nom = 59
		for n in numbers:
			if x in n:
				cod = cod + f"{baza[nom]}"
			else:
				pass
			nom += 1


elif a == "D":
	from key import KEY

	baza = list()

	baza = KEY

	text2 = list()
	ty = ""
	text = ""
	c = 0
	cod = ""
	cop = ''

	text = str(input(": "))
	key = text.split("|")

	lop = len(key[0])
	lor = (key[0])

	lof = (key[1])
	n = 5
	text5 = [lof[i:i+n] for i in range(0, len(lof), n)]

	for x in text5:
		nom = 0
		for b in baza:
			if b in x:
				cop = cop + f"{over[nom]}"
			else:
				pass
			nom += 1
	lop = str(lop)

	if lop == cop:
		n = 5
		text2 = [lor[i:i+n] for i in range(0, len(lor), n)]

		for x in text2:
			nom = 0
			for b in baza:
				if b in x:
					cod = cod + f"{over[nom]}"
				else:
					pass
				nom += 1
	else:
		print(Fore.RED + "ERROR" + Style.RESET_ALL)

elif a == "C":
	a = 1
	g = list()
	length = 5

	while a < 101:
	    letters_and_digits = string.ascii_letters + string.digits
	    rand_string = ''.join(random.sample(letters_and_digits, length))
	    g.append(rand_string)
	    a += 1

	print(g)
	f = open('key.py','w')  # открытие в режиме записи
	f.write('KEY = ')
	f.write('[')
	for x in g:
	    f.write(f"'{x}',")  # запись x в файл
	f.write(']')
	f.close()
	cod = "Key generated"

print("\n")
print(Fore.GREEN + ": ", cod + Style.RESET_ALL)
