#crypt and decrypt.
# -*- coding: utf-8 -*-
import os
import random
def crypt():
	symbols=[".","?","!","/",":",";","+","%"]
	numbers=["1","2","3","4","5","6","7","8","9"]
	letters=["A","B","C","D","E","F","G","I","J","K","L","M","N","O","P","R","S","T","Y","U","V","Y","Z","X"]
	os.system("cls")
	words_to_the_crypt = raw_input("enter the magic words.: ")
	wttc  = words_to_the_crypt
	wtc = wttc.upper()
	listofcrypt=[]
	for i in wtc:
		if i == "A":
			i = "D"
		elif i == "%":
			i = "^"
		elif i == "+":
			i = "-"
		elif i == ";":
			i = "'"	
		elif i == ":":
			i = "="
		elif i == "/":
			i = "*"
		elif i == "!":
			i = "{"
		elif i == "?":
			i = "}"
		elif i == ".":
			i = ","
		elif i == ",":
			i = "."
		elif i == "[":
			i = "]"
		elif i == "]":
			i = "["
		elif i == "0":
			i = "0"
		elif i == "1":
			i = "4"
		elif i == "2":
			i = "5"
		elif i == "3":
			i = "6"
		elif i == "4":
			i = "7"
		elif i == "5":
			i = "8"
		elif i == "6":
			i = "9"
		elif i == "7":
			i = "1"
		elif i == "8":
			i = "2"
		elif i == "9":
			i = "3"											
		elif i == "%":
			i = "^"
		elif i == " ":
			i = "&"
		elif i == "B":
			i = "E"
		elif i == "C":
			i = "F"
		elif i == "D":
			i = "G"
		elif i == "E":
			i = "I"
		elif i == "F":
			i = "J"
		elif i == "G":
			i = "K"
		elif i == "I":
			i = "L"
		elif i == "J":
			i = "M"
		elif i == "K":
			i = "N"
		elif i == "L":
			i = "O"
		elif i == "M":
			i = "P"
		elif i == "N":
			i = "R"
		elif i == "O":
			i = "S"
		elif i == "P":
			i = "T"
		elif i == "R":
			i = "Y"
		elif i == "S":
			i = "U"
		elif i == "T":
			i = "V"
		elif i == "Y":
			i = "A"
		elif i == "U":
			i = "B"
		elif i == "V":
			i = "C"	
		elif i == "Z":
			i = "X"	
		elif i == "X":
			i = "Z"														
		listofcrypt.append(i)
	a = 0
	pasw=[]
	x = len(listofcrypt)
	while a < x:
		randlet = random.choice(letters)
		pasw.append(randlet)
		randnum = random.choice(symbols)
		pasw.append(randnum)
		randlet = random.choice(letters)
		pasw.append(randlet)
		randnum = random.choice(numbers)
		pasw.append(randnum)
		randlet = random.choice(symbols)
		pasw.append(randlet)
		randnum = random.choice(numbers)
		pasw.append(randnum)
		randlet = random.choice(letters)
		pasw.append(randlet)
		randnum = random.choice(numbers)
		pasw.append(randnum)
		a += 1
	end = []
	w = 1
	for q in listofcrypt:
		end.append(pasw[w])
		w += 1
		end.append(pasw[w])
		w += 1
		end.append(pasw[w])
		w += 1
		end.append(pasw[w])
		w += 1
		end.append(q)
	crypted = ''.join(end)
	print("encrypted message.: %s"%crypted)

#done

#enter the magic words.: selam
#encrypted message.: 4T4BU2Z4UI7E9LO8A9MD3O8TP

def decrypt():
	os.system("cls")
	title = raw_input("paste the encrypted title.: ")
	lexn =len(title)
	decrypt=[]
	for i in title:
		decrypt.append(i)
	a = 0
	dd =len(decrypt)
	lol=[]
	while a < dd:
		a += 1
		if a%5==0:
			try:
				lol.append(decrypt[a-1])
			except:
				pass
#		for i in decrypt:
#		a += 1
#		if a%4==0:
#			lol.append(decrypt[a])
#			a+=1
	finish=[]
	for i in lol:
		if i == "D":
			i = "A"
		elif i == "%":
			i = "^"
		elif i == "-":
			i = "+"
		elif i == "'":
			i = ";"	
		elif i == "=":
			i = ":"
		elif i == "*":
			i = "/"
		elif i == "{":
			i = "!"
		elif i == "}":
			i = "?"
		elif i == ",":
			i = "."
		elif i == ".":
			i = ","
		elif i == "]":
			i = "["
		elif i == "[":
			i = "]"
		elif i == "4":
			i = "1"
		elif i == "5":
			i = "2"
		elif i == "0":
			i = "0"
		elif i == "6":
			i = "3"
		elif i == "7":
			i = "4"
		elif i == "8":
			i = "5"
		elif i == "9":
			i = "6"
		elif i == "1":
			i = "7"
		elif i == "2":
			i = "8"
		elif i == "3":
			i = "9"											
		elif i == "%":
			i = "^"
		elif i == "&":
			i = " "
		elif i == "E":
			i = "B"
		elif i == "F":
			i = "C"
		elif i == "G":
			i = "D"
		elif i == "I":
			i = "E"
		elif i == "J":
			i = "F"
		elif i == "K":
			i = "G"
		elif i == "L":
			i = "I"
		elif i == "M":
			i = "J"
		elif i == "N":
			i = "K"
		elif i == "O":
			i = "L"
		elif i == "P":
			i = "M"
		elif i == "R":
			i = "N"
		elif i == "S":
			i = "O"
		elif i == "T":
			i = "P"
		elif i == "Y":
			i = "R"
		elif i == "U":
			i = "S"
		elif i == "V":
			i = "T"
		elif i == "A":
			i = "Y"
		elif i == "B":
			i = "U"
		elif i == "C":
			i = "V"	
		elif i == "X":
			i = "Z"	
		elif i == "Z":
			i = "X"
		finish.append(i)
	decrypted = ''.join(finish)
	print("decrypted message.: %s"%decrypted)

os.system("cls")
print("""
 'W'ords 'T'o 'C'rypt

     1. encrypt.
     2. decrypt.
     3. creator.

  program by bash.""")
choice =raw_input("\n choice ~# ")
if choice == "one" or choice == "One" or choice == "1":
	crypt()
if choice == "two" or choice == "Two" or choice == "2":
	decrypt()
if choice == "three" or choice == "Three" or choice == "3":
	os.system("start www.instagram.com/yigitaydn.py")
	os.system("start www.facebook.com/xwbash")