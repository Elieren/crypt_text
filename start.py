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

print(Fore.GREEN + banner + Style.RESET_ALL)

a = str(input(Fore.GREEN + "(S) - Scrambler, (D) - Decoder, (C) - Create key: " + Style.RESET_ALL))

a = a.upper()

if a == "S":
	from key import KEY

	baza = list()

	baza = KEY

	text = str(input(": "))

	text = text.upper()

	text2 = list(text)

	cod = ""

	for x in text2:
	#--------------------------------------------------------- RU ------------------
		if "А" in x:
			cod = cod + f"{baza[0]}"
		elif "Б" in x:
			cod = cod + f"{baza[1]}"
		elif "В" in x:
			cod = cod + f"{baza[2]}"
		elif "Г" in x:
			cod = cod + f"{baza[3]}"
		elif "Д" in x:
			cod = cod + f"{baza[4]}"
		elif "Е" in x:
			cod = cod + f"{baza[5]}"
		elif "Ё" in x:
			cod = cod + f"{baza[6]}"
		elif "Ж" in x:
			cod = cod + f"{baza[7]}"
		elif "З" in x:
			cod = cod + f"{baza[8]}"
		elif "И" in x:
			cod = cod + f"{baza[9]}"
		elif "Й" in x:
			cod = cod + f"{baza[10]}"
		elif "К" in x:
			cod = cod + f"{baza[11]}"
		elif "Л" in x:
			cod = cod + f"{baza[12]}"
		elif "М" in x:
			cod = cod + f"{baza[13]}"
		elif "Н" in x:
			cod = cod + f"{baza[14]}"
		elif "О" in x:
			cod = cod + f"{baza[15]}"
		elif "П" in x:
			cod = cod + f"{baza[16]}"
		elif "Р" in x:
			cod = cod + f"{baza[17]}"
		elif "С" in x:
			cod = cod + f"{baza[18]}"
		elif "Т" in x:
			cod = cod + f"{baza[19]}"
		elif "У" in x:
			cod = cod + f"{baza[20]}"
		elif "Ф" in x:
			cod = cod + f"{baza[21]}"
		elif "Х" in x:
			cod = cod + f"{baza[22]}"
		elif "Ц" in x:
			cod = cod + f"{baza[23]}"
		elif "Ч" in x:
			cod = cod + f"{baza[24]}"
		elif "Ш" in x:
			cod = cod + f"{baza[25]}"
		elif "Щ" in x:
			cod = cod + f"{baza[26]}"
		elif "Ъ" in x:
			cod = cod + f"{baza[27]}"
		elif "Ы" in x:
			cod = cod + f"{baza[28]}"
		elif "Ь" in x:
			cod = cod + f"{baza[29]}"
		elif "Э" in x:
			cod = cod + f"{baza[30]}"
		elif "Ю" in x:
			cod = cod + f"{baza[31]}"
		elif "Я" in x:
			cod = cod + f"{baza[32]}"
	#------------------------------------------------------------------ ENG -------------------
		elif "A" in x:
			cod = cod + f"{baza[33]}"
		elif "B" in x:
			cod = cod + f"{baza[34]}"
		elif "C" in x:
			cod = cod + f"{baza[35]}"
		elif "D" in x:
			cod = cod + f"{baza[36]}"
		elif "E" in x:
			cod = cod + f"{baza[37]}"
		elif "F" in x:
			cod = cod + f"{baza[38]}"
		elif "G" in x:
			cod = cod + f"{baza[39]}"
		elif "H" in x:
			cod = cod + f"{baza[40]}"
		elif "I" in x:
			cod = cod + f"{baza[41]}"
		elif "J" in x:
			cod = cod + f"{baza[42]}"
		elif "K" in x:
			cod = cod + f"{baza[43]}"
		elif "L" in x:
			cod = cod + f"{baza[44]}"
		elif "M" in x:
			cod = cod + f"{baza[45]}"
		elif "N" in x:
			cod = cod + f"{baza[46]}"
		elif "O" in x:
			cod = cod + f"{baza[47]}"
		elif "P" in x:
			cod = cod + f"{baza[48]}"
		elif "Q" in x:
			cod = cod + f"{baza[49]}"
		elif "R" in x:
			cod = cod + f"{baza[50]}"
		elif "S" in x:
			cod = cod + f"{baza[51]}"
		elif "T" in x:
			cod = cod + f"{baza[52]}"
		elif "U" in x:
			cod = cod + f"{baza[53]}"
		elif "V" in x:
			cod = cod + f"{baza[54]}"
		elif "W" in x:
			cod = cod + f"{baza[55]}"
		elif "X" in x:
			cod = cod + f"{baza[56]}"
		elif "Y" in x:
			cod = cod + f"{baza[57]}"
		elif "Z" in x:
			cod = cod + f"{baza[58]}"

	#------------------------------------------------------------------ ЦЫФРЫ -----------------
		elif "1" in x:
			cod = cod + f"{baza[59]}"
		elif "2" in x:
			cod = cod + f"{baza[60]}"
		elif "3" in x:
			cod = cod + f"{baza[61]}"
		elif "4" in x:
			cod = cod + f"{baza[62]}"
		elif "5" in x:
			cod = cod + f"{baza[63]}"
		elif "6" in x:
			cod = cod + f"{baza[64]}"
		elif "7" in x:
			cod = cod + f"{baza[65]}"
		elif "8" in x:
			cod = cod + f"{baza[66]}"
		elif "9" in x:
			cod = cod + f"{baza[67]}"
		elif "0" in x:
			cod = cod + f"{baza[68]}"
	#----------------------------------------------------------------- PROBEL ------------------
		elif " " in x:
			cod = cod + f"{baza[69]}"
	#----------------------------------------------------------------- ZNAKI -------------------
		elif "," in x:
			cod = cod + f"{baza[70]}"
		elif "." in x:
			cod = cod + f"{baza[71]}"
		elif "!" in x:
			cod = cod + f"{baza[72]}"
		elif "?" in x:
			cod = cod + f"{baza[73]}"
		elif '"' in x:
			cod = cod + f"{baza[74]}"
		elif "@" in x:
			cod = cod + f"{baza[75]}"
		elif "№" in x:
			cod = cod + f"{baza[76]}"
		elif "#" in x:
			cod = cod + f"{baza[78]}"
		elif "$" in x:
			cod = cod + f"{baza[79]}"
		elif ";" in x:
			cod = cod + f"{baza[80]}"
		elif "%" in x:
			cod = cod + f"{baza[81]}"
		elif "^" in x:
			cod = cod + f"{baza[82]}"
		elif ":" in x:
			cod = cod + f"{baza[83]}"
		elif "&" in x:
			cod = cod + f"{baza[84]}"
		elif "*" in x:
			cod = cod + f"{baza[85]}"
		elif "(" in x:
			cod = cod + f"{baza[86]}"
		elif ")" in x:
			cod = cod + f"{baza[87]}"
		elif "-" in x:
			cod = cod + f"{baza[88]}"
		elif "_" in x:
			cod = cod + f"{baza[89]}"
		elif "+" in x:
			cod = cod + f"{baza[90]}"
		elif "=" in x:
			cod = cod + f"{baza[91]}"
		elif "{" in x:
			cod = cod + f"{baza[92]}"
		elif "}" in x:
			cod = cod + f"{baza[93]}"
		elif "[" in x:
			cod = cod + f"{baza[94]}"
		elif "]" in x:
			cod = cod + f"{baza[95]}"
		elif "'" in x:
			cod = cod + f"{baza[96]}"
		elif ":" in x:
			cod = cod + f"{baza[97]}"
		elif ">" in x:
			cod = cod + f"{baza[98]}"
		elif "<" in x:
			cod = cod + f"{baza[99]}"
		elif "/" in x:
			cod = cod + f"{baza[100]}"
		else:
			pass

	low = len(cod)
	low = str(low)
	cod = cod + "|"

	for x in low:
		if "1" in x:
			cod = cod + f"{baza[59]}"
		elif "2" in x:
			cod = cod + f"{baza[60]}"
		elif "3" in x:
			cod = cod + f"{baza[61]}"
		elif "4" in x:
			cod = cod + f"{baza[62]}"
		elif "5" in x:
			cod = cod + f"{baza[63]}"
		elif "6" in x:
			cod = cod + f"{baza[64]}"
		elif "7" in x:
			cod = cod + f"{baza[65]}"
		elif "8" in x:
			cod = cod + f"{baza[66]}"
		elif "9" in x:
			cod = cod + f"{baza[67]}"
		elif "0" in x:
			cod = cod + f"{baza[68]}"
		else:
			pass


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

	my_st = text
	key = my_st.split("|")

	lop = len(key[0])
	lor = (key[0])

	lof = (key[1])
	n = 5
	text5 = [lof[i:i+n] for i in range(0, len(lof), n)]

	for x in text5:
		if f"{baza[59]}" in x:
			cop = cop + '1'
		elif f"{baza[60]}" in x:
			cop = cop + '2'
		elif f"{baza[61]}" in x:
			cop = cop + '3'
		elif f"{baza[62]}" in x:
			cop = cop + '4'
		elif f"{baza[63]}" in x:
			cop = cop + '5'
		elif f"{baza[64]}" in x:
			cop = cop + '6'
		elif f"{baza[65]}" in x:
			cop = cop + '7'
		elif f"{baza[66]}" in x:
			cop = cop + '8'
		elif f"{baza[67]}" in x:
			cop = cop + '9'
		elif f"{baza[68]}" in x:
			cop = cop + '0'
		else:
			pass
	lop = str(lop)

	if lop == cop:
		n = 5
		text2 = [lor[i:i+n] for i in range(0, len(lor), n)]

		for x in text2:
		#--------------------------------------------------------- RU ------------------
			if f"{baza[0]}" in x:
				cod = cod + "А" 
			elif f"{baza[1]}" in x:
				cod = cod + "Б"
			elif f"{baza[2]}" in x:
				cod = cod + "В"
			elif f"{baza[3]}" in x:
				cod = cod + "Г"
			elif f"{baza[4]}" in x:
				cod = cod + "Д"
			elif f"{baza[5]}" in x:
				cod = cod + "Е"
			elif f"{baza[6]}" in x:
				cod = cod + "Ё"
			elif f"{baza[7]}" in x:
				cod = cod + "Ж"
			elif f"{baza[8]}" in x:
				cod = cod + "З"
			elif f"{baza[9]}" in x:
				cod = cod + "И"
			elif f"{baza[10]}" in x:
				cod = cod + "Й"
			elif f"{baza[11]}" in x:
				cod = cod + "К"
			elif f"{baza[12]}" in x:
				cod = cod + "Л"
			elif f"{baza[13]}" in x:
				cod = cod + "М"
			elif f"{baza[14]}" in x:
				cod = cod + "Н"
			elif f"{baza[15]}" in x:
				cod = cod + "О"
			elif f"{baza[16]}" in x:
				cod = cod + "П"
			elif f"{baza[17]}" in x:
				cod = cod + "Р"
			elif f"{baza[18]}" in x:
				cod = cod + "С"
			elif f"{baza[19]}" in x:
				cod = cod + "Т"
			elif f"{baza[20]}" in x:
				cod = cod + "У"
			elif f"{baza[21]}" in x:
				cod = cod + "Ф"
			elif f"{baza[22]}" in x:
				cod = cod + "Х"
			elif f"{baza[23]}" in x:
				cod = cod + "Ц"
			elif f"{baza[24]}" in x:
				cod = cod + "Ч"
			elif f"{baza[25]}" in x:
				cod = cod + "Ш"
			elif f"{baza[26]}" in x:
				cod = cod + "Щ"
			elif f"{baza[27]}" in x:
				cod = cod + "Ъ"
			elif f"{baza[28]}" in x:
				cod = cod + "Ы"
			elif f"{baza[29]}" in x:
				cod = cod + "Ь"
			elif f"{baza[30]}" in x:
				cod = cod + "Э"
			elif f"{baza[31]}" in x:
				cod = cod + "Ю"
			elif f"{baza[32]}" in x:
				cod = cod + "Я"
		#------------------------------------------------------------------ ENG -------------------
			elif f"{baza[33]}" in x:
				cod = cod + "A"
			elif f"{baza[34]}" in x:
				cod = cod + "B"
			elif f"{baza[35]}" in x:
				cod = cod + "C"
			elif f"{baza[36]}" in x:
				cod = cod + "D"
			elif f"{baza[37]}" in x:
				cod = cod + "E"
			elif f"{baza[38]}" in x:
				cod = cod + "F"
			elif f"{baza[39]}" in x:
				cod = cod + "G"
			elif f"{baza[40]}" in x:
				cod = cod + "H"
			elif f"{baza[41]}" in x:
				cod = cod + "I"
			elif f"{baza[42]}" in x:
				cod = cod + "J"
			elif f"{baza[43]}" in x:
				cod = cod + "K"
			elif f"{baza[44]}" in x:
				cod = cod + "L"
			elif f"{baza[45]}" in x:
				cod = cod + "M"
			elif f"{baza[46]}" in x:
				cod = cod + "N"
			elif f"{baza[47]}" in x:
				cod = cod + "O"
			elif f"{baza[48]}" in x:
				cod = cod + "P"
			elif f"{baza[49]}" in x:
				cod = cod + "Q"
			elif f"{baza[50]}" in x:
				cod = cod + "R"
			elif f"{baza[51]}" in x:
				cod = cod + "S"
			elif f"{baza[52]}" in x:
				cod = cod + "T"
			elif f"{baza[53]}" in x:
				cod = cod + "U"
			elif f"{baza[54]}" in x:
				cod = cod + "V"
			elif f"{baza[55]}" in x:
				cod = cod + "W"
			elif f"{baza[56]}" in x:
				cod = cod + "X"
			elif f"{baza[57]}" in x:
				cod = cod + "Y"
			elif f"{baza[58]}" in x:
				cod = cod + "Z"

		#------------------------------------------------------------------ ЦЫФРЫ -----------------
			elif f"{baza[59]}" in x:
				cod = cod + "1"
			elif f"{baza[60]}" in x:
				cod = cod + "2"
			elif f"{baza[61]}" in x:
				cod = cod + "3"
			elif f"{baza[62]}" in x:
				cod = cod + "4"
			elif f"{baza[63]}" in x:
				cod = cod + "5"
			elif f"{baza[64]}" in x:
				cod = cod + "6"
			elif f"{baza[65]}" in x:
				cod = cod + "7"
			elif f"{baza[66]}" in x:
				cod = cod + "8"
			elif f"{baza[67]}" in x:
				cod = cod + "9"
			elif f"{baza[68]}" in x:
				cod = cod + "0"
		#----------------------------------------------------------------- PROBEL ------------------
			elif f"{baza[69]}" in x:
				cod = cod + " "
		#----------------------------------------------------------------- ZNAKI -------------------
			elif f"{baza[70]}" in x:
				cod = cod + ","
			elif f"{baza[71]}" in x:
				cod = cod + "."
			elif f"{baza[72]}" in x:
				cod = cod + "!"
			elif f"{baza[73]}" in x:
				cod = cod + "?"
			elif f"{baza[74]}" in x:
				cod = cod + '"'
			elif f"{baza[75]}" in x:
				cod = cod + "@"
			elif f"{baza[76]}" in x:
				cod = cod + "№"
			elif f"{baza[78]}" in x:
				cod = cod + "#"
			elif f"{baza[79]}" in x:
				cod = cod + "$"
			elif f"{baza[80]}" in x:
				cod = cod + ";"
			elif f"{baza[81]}" in x:
				cod = cod + "%"
			elif f"{baza[82]}" in x:
				cod = cod + "^"
			elif f"{baza[83]}" in x:
				cod = cod + ":"
			elif f"{baza[84]}" in x:
				cod = cod + "&"
			elif f"{baza[85]}" in x:
				cod = cod + "*"
			elif f"{baza[86]}" in x:
				cod = cod + "("
			elif f"{baza[87]}" in x:
				cod = cod + ")"
			elif f"{baza[88]}" in x:
				cod = cod + "-"
			elif f"{baza[89]}" in x:
				cod = cod + "_"
			elif f"{baza[90]}" in x:
				cod = cod + "+"
			elif f"{baza[91]}" in x:
				cod = cod + "="
			elif f"{baza[92]}" in x:
				cod = cod + "{"
			elif f"{baza[93]}" in x:
				cod = cod + "}"
			elif f"{baza[94]}" in x:
				cod = cod + "["
			elif f"{baza[95]}" in x:
				cod = cod + "]"
			elif f"{baza[96]}" in x:
				cod = cod + "'"
			elif f"{baza[97]}" in x:
				cod = cod + ":"
			elif f"{baza[98]}" in x:
				cod = cod + ">"
			elif f"{baza[99]}" in x:
				cod = cod + "<"
			elif f"{baza[100]}" in x:
				cod = cod + "/"
			else:
				os.system("clear")
				os.system("cls")
				cod = ""
				break
	else:
		print(Fore.RED + "ERROR" + Style.RESET_ALL)
elif a == "C":
	a = 1
	g = list()
	length = 5

	while a < 102:
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
