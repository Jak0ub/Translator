import getpass
import hashlib
import time
import os
import sys
import platform
import random
#proměnné
logged_as = ""
uspech = False
nic = False
spravne = 0
chyby = 0
logged = False
#konec proměnných a definice
def main():
	print(r'''    
   _       _               _     
  (_)     | |             | |    
   _  __ _| | _____  _   _| |__  
  | |/ _` | |/ / _ \| | | | '_ \ 
  | | (_| |   < (_) | |_| | |_) |
  | |\__,_|_|\_\___/ \__,_|_.__/ 
 _/ |                            
|__/                            
''')
def kontrola():
	try:
		with open("credentials.txt", "r", encoding="utf-8") as file:
			radky = file.readlines()
	except FileNotFoundError:
		with open("credentials.txt", "w", encoding="utf-8") as file:
			file.write("8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918:e7cf3ef4f17c3999a94f2c6f612e8a888e5b1026878e4e19398b23bd38ec221a,")
			nic = True
			radky = []
	if len(radky) == 0:
		with open("credentials.txt", "w", encoding="utf-8") as file:
			file.write("8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918:e7cf3ef4f17c3999a94f2c6f612e8a888e5b1026878e4e19398b23bd38ec221a,")

#Konec definic a kontrola systému
platform_system = platform.system()
if platform_system == "Windows":
	def cisto():
		os.system("cls")
else:
	def cisto():
		os.system("clear")
#Konec Detekce systému a kontrola slovíček
try:
	with open("words_configFile.txt", "r", encoding="utf-8") as file:
		radky = file.readlines()
except FileNotFoundError:
	f = open("words_configFile.txt", "a")
	f.close()
#Konec kontroly a ůvodní načítání	
cisto()
main()
time.sleep(0.6)
cisto()
print(r'''    
   _       _               _     
  (_)     | |             | |    
   _  __ _| | _____  _   _| |__  
  | |/ _` | |/ / _ \| | | | '_ \ 
  | | (_| |   < (_) | |_| | |_) |   _
  | |\__,_|_|\_\___/ \__,_|_.__/   (_) 
 _/ |                            
|__/                             
''')
time.sleep(0.6)
cisto()
print(r'''     
   _       _               _     
  (_)     | |             | |    
   _  __ _| | _____  _   _| |__  
  | |/ _` | |/ / _ \| | | | '_ \ 
  | | (_| |   < (_) | |_| | |_) |   _    _
  | |\__,_|_|\_\___/ \__,_|_.__/   (_)  (_)
 _/ |                            
|__/                            
''')
time.sleep(0.6)
cisto()
print(r'''    
   _       _               _     
  (_)     | |             | |    
   _  __ _| | _____  _   _| |__  
  | |/ _` | |/ / _ \| | | | '_ \ 
  | | (_| |   < (_) | |_| | |_) |   _    _    _
  | |\__,_|_|\_\___/ \__,_|_.__/   (_)  (_)  (_)
 _/ |                            
|__/                             
''')
time.sleep(0.6)
cisto()
#Konec úvodního načtení a main loop
while True:
	main()
	if logged_as != "":
		print(f"\t\t|Přihlášen jako: {logged_as}|")
	if logged_as == "":
		logged_as = "None"
		print("\t\t|Nepřihlášen|")
	if logged_as == "admin":
		choice = input("Zadej číslo akce:\n |1| -> |Přidání slovíček|\n |2| -> |Odebrání slovíček| \n |3| -> |Začít procvičovat|\n |4| -> |Hledání dostupnosti slovíček| \n |5| -> |Vypsání aktuálních slovíček| \n |6| -> |Přihlášení se|\n |7| -> |Registrace|\n |8| -> |Změna Hesla|\n |9| -> |Odebrání uživatele|\n |10| -> |Tabulka Výsledků|\n\t")
	else:
		choice = input("Zadej číslo akce:\n |1| -> |Začít procvičovat|\n |2| -> |Vypsání aktuálních slovíček| \n |3| -> |Přihlášení se|\n |4| -> |Tabulka Výsledků|\n\t")		
	try:
		choice = int(choice)
	except ValueError:
		print("\t\tZadej ČÍSLO z nabídky!")
		time.sleep(1)		
		cisto()
		continue		
	if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 and choice != 7 and choice != 8 and choice != 9 and choice != 10 and logged_as == "admin":
		print("\t\t1-10!")
		time.sleep(1)		
		cisto()
		continue
	elif logged_as != "admin" and choice != 1 and choice != 2 and choice != 3 and choice != 4:
		print("\t\t1-4!")
		time.sleep(1)		
		cisto()
		continue
	if choice == 1 and logged_as == "admin":
		cisto()
		main()
		print("|Q| -> |ukončení loopu|\n")
		while True:
			add = input("Zadej slovo: ")
			if add.lower() == "q":
				cisto()				
				break
			add1 = input("Zadej překlad slova: ")
			if add1.lower() == "q":
				cisto()				
				break
			with open("words_configFile.txt", "r", encoding="utf-8") as file:
				radky = file.readlines()
				radky.append(f"{add}:{add1},")
			with open("words_configFile.txt", "w", encoding="utf-8") as file:
				file.writelines(radky)
			print("\tZapsáno✔️\n")
	elif choice == 2 and logged_as == "admin":
		while True:
			cisto()
			main()
			radky2 = []
			success = False
			print("|Q| -> |ukončení loopu|\n")
			delete = input("Zadej slovo pro odstranění: ")
			if delete.lower() == "q":
				cisto()	
				break
			with open("words_configFile.txt", "r", encoding="utf-8") as file:
				radky = file.readlines()
				for i in range(len(radky)):
					sloupce = radky[i].strip().split(",")
					for sloup in sloupce:
						slup = sloup.split(":")
						try:
							one = slup[0]
							two = slup[1]
							if one.lower() == delete.lower() or two.lower() == delete.lower():
								pass
								success = True
							else:
								radky2.append(f"{one}:{two},")
						except IndexError:
							pass
				radky = radky2
			if success == True:
				with open("words_configFile.txt", "w", encoding="utf-8") as file:
					file.writelines(radky2)
				input("\tSmazáno✔️\n\t\tEnter pro pokračování")
			else:
				input("\tNenalezeno✖️\n\t\tEnter pro pokračování")					
	elif choice == 3 and logged_as == "admin" or logged_as != "admin" and choice == 1:
		if logged_as == "None":
			cisto()
			main()
			input("Nejste přihlášeni!, Enter pro pokračování")
			cisto()
			continue
		cisto()
		main()
		print("překlad slova:")
		with open("words_configFile.txt", "r", encoding="utf-8") as file:
			radky = file.readlines()
			for radek in radky:
				sloupy = radek.strip().split(",")
				cisla = []
				while len(cisla) != len(sloupy):
					cislo = random.randint(0, len(sloupy) - 1)
					if cislo in cisla:
						pass
					else:
						cisla.append(cislo)
				for i in range(len(cisla)):
					verify = cisla[i]
					sloup = sloupy[verify]
					hlavni = sloup.split(":")
					if len(hlavni) != 2:
						pass
					else:
						nahodne = random.randint(0, 1)
						if nahodne == 1:
							vedlejsi = hlavni[0]
							hlavni = hlavni[1]
						else:
							vedlejsi = hlavni[1]
							hlavni = hlavni[0]
						quest = input(f"|{hlavni}|: ")
						if quest.lower() == vedlejsi:
							print("\t✔️")
							spravne += 1
						else:
							print("\t✖️")
							chyby += 1
		if spravne == 0 and chyby == 0:
			cisto()
			main()
			input("Nejsou zadaná slova\n\tEnter pro pokračování")
			cisto()
		else:
			with open("Vysledky.txt", "a", encoding="utf-8") as file:
				pass
			with open("Vysledky.txt", "r", encoding="utf-8") as file:
				prumer = round((100 / (chyby + spravne)) * spravne, 1) 
				radky = file.readlines()
				udaj3 = -33
				udaj2 = 1
				i = 0
				cislo_dulezite = -1
				cislo_radku = -1
				for radek in radky:
					cislo_radku += 1
					slova = radek.split(",")
					udaj1 = slova[0]
					udaj22 = slova[1]
					udaj333 = slova[2]
					if udaj1 == logged_as:
						NotFound = True
						while NotFound:
							i += 1
							pojd = str(i)
							pojd = hashlib.sha256(pojd.encode())
							pojd = pojd.hexdigest()
							if pojd == udaj22:
								udaj2 = i
								NotFound = False
						udaj2 = int(udaj2)
						cislo_dulezite = cislo_radku
						udaj2 += 1
						i = 0
						for i in range(1002):
							j = i / 10
							pojd = str(j)
							pojd = hashlib.sha256(pojd.encode())
							pojd = pojd.hexdigest()
							if pojd == udaj333:
								udaj3 = j
								break
			prumer2 = prumer
			if udaj3 == -33:
				prumer = float(prumer)
			else:
				prumer = round((udaj3 + prumer) / 2, 1)	
			prumer = str(prumer)
			prumer = hashlib.sha256(prumer.encode())
			prumer = prumer.hexdigest()			
			pokusy = str(udaj2)
			pokusy2 = hashlib.sha256(pokusy.encode())
			pokusy2 = pokusy2.hexdigest()
			if cislo_dulezite != -1:
				radky[cislo_dulezite] = f"{logged_as},{pokusy2},{prumer},\n"
			else:
				radky.append(f"{logged_as},{pokusy2},{prumer},\n")
			with open("Vysledky.txt", "w", encoding="utf-8") as file:
				file.writelines(radky)
			input(f"\n|Správně| -> |{spravne}|\n|Chyby| -> |{chyby}|\n|Procentuální úspěšnost| -> |{prumer2}%|")
			spravne = 0
			chyby = 0
			cisto()
	elif choice == 4 and logged_as == "admin":
		while True:
			cisto()
			main()
			print("|Q| -> |ukončení loopu|\n")
			search = input("Vyhledej slovíčko... ")
			if search.lower() == "q":
				cisto()
				break
			nalezeno = False
			while True:
				with open("words_configFile.txt", "r", encoding="utf-8") as file:
					radky = file.readlines()
					for i in range(len(radky)):
						sloupce = radky[i].strip().split(",")
						for sloupec in sloupce:
							try:
								jeden = sloupec.split(":")[0].strip()
								druhej = sloupec.split(":")[1].strip()
								if jeden.lower() == search.lower() or druhej.lower() == search.lower():
									nalezeno1 = jeden
									nalezeno2 = druhej
									nalezeno = True
							except IndexError:
								pass
				if nalezeno == False:
					input("\tNenalezeno✖️\n\t\tEnter pro pokračování")
					break
				else:
					input(f"\tNalezeno✔️: |{nalezeno1}| -> |{nalezeno2}|\n\t\tEnter pro pokračování")
					break
			cisto()
	elif choice == 5 and logged_as == "admin" or logged_as != "admin" and choice == 2:
		cisto()
		main()
		print("Aktuální slovíčka\n")
		with open("words_configFile.txt", "r", encoding="utf-8") as file:
			radky = file.readlines()
			for i in range(len(radky)):
				sloupce = radky[i].strip().split(",")
				for sloupec in sloupce:
					try:
						jeden = sloupec.split(":")[0].strip()
						druhej = sloupec.split(":")[1].strip()
						print(f"|{jeden}| -> |{druhej}|")
					except IndexError:
						pass
		input("\nEnter pro pokračování")
		cisto()
	elif choice == 6 and logged_as == "admin" or logged_as != "admin" and choice == 3:
		uspech = False
		cisto()	
		main()
		kontrola()
		for i in range(3):
			print("|Login|")
			zadano = input("|Uživatelské jméno|: ")
			logged_as = zadano
			zadano2 = getpass.getpass("|Heslo|: ")
			zadano = hashlib.sha256(zadano.encode())
			zadano = zadano.hexdigest()
			zadano2 = hashlib.sha256(zadano2.encode())
			zadano2 = zadano2.hexdigest()
			with open("credentials.txt", "r", encoding="utf-8") as file:
				radky = file.readlines()
				for radek in radky:
					sloupy = radek.strip().split(",")
					try:
						for sloup in sloupy:
							slova = sloup.split(":")
							uzivatel = slova[0]
							password = slova[1]
							if zadano == uzivatel:
								if zadano2 == password:
									uspech = True
					except IndexError:
						pass

			if uspech == True:
				break
			else:
				print("Špatné údaje")
				cisto()
				main()
				continue
		if uspech != True:
			print("Příliš mnoho chybných pokusů")
			print("ukončuji...")
			time.sleep(3)
			sys.exit()	
		cisto()	
	elif choice == 7 and logged_as == "admin":
		while True:
			uspech = False
			cisto()
			main()
			kontrola()
			if logged_as != "":
				print("|Register|")
				user = input("|Uživatelské jméno nebo Q=Ukončení Loopu|: ")
				if user.lower() == "q":
					break
				user = hashlib.sha256(user.encode())
				user = user.hexdigest()
				with open("credentials.txt", "r", encoding="utf-8") as file:
					radky = file.readlines()
					radky = radky[0].split(",")
					for radek in radky:
						jeden = radek.split(":")[0]
						if user == jeden:
							input("\t|Uživatel je již registrovaný!, Enter pro pokračování|")
							break
					if user == jeden:
						continue
				while True:
					pasw = getpass.getpass("|Heslo|: ")
					pasw2 = getpass.getpass("|Heslo znovu|: ")
					if pasw == pasw2:
						break
					else:
						input("\tHesla se neshodují, Enter pro pokračování")
						cisto()
						main()
						continue
				pasw = hashlib.sha256(pasw.encode())
				pasw = pasw.hexdigest()
				pasw2 = ""
				with open("credentials.txt", "r", encoding="utf-8") as file:
					radky = file.readlines()
					radky.append(f"{user}:{pasw},")
				with open("credentials.txt", "w", encoding="utf-8") as file:
					file.writelines(radky)
				input("Údaje byly zapsány, Enter pro pokračování")
				cisto()
			else:
				input("Pro registraci nového uživatele se přihlašte, Enter pro pokračování")
				cisto()
				main()
				for i in range(3):
					print("|Login|")
					zadano = input("|Uživatelské jméno|: ")
					logged_as = zadano
					zadano2 = getpass.getpass("|Heslo|: ")
					zadano = hashlib.sha256(zadano.encode())
					zadano = zadano.hexdigest()
					zadano2 = hashlib.sha256(zadano2.encode())
					zadano2 = zadano2.hexdigest()
					with open("credentials.txt", "r", encoding="utf-8") as file:
						radky = file.readlines()
						for radek in radky:
							sloupy = radek.strip().split(",")
							try:
								for sloup in sloupy:
									slova = sloup.split(":")
									uzivatel = slova[0]
									password = slova[1]
									if zadano == uzivatel:
										if zadano2 == password:
											uspech = True
							except IndexError:
								pass

					if uspech == True:
						print("Přihlášení proběhlo úspěšně!")
						time.sleep(2)
						break
					else:
						print("Špatné údaje")
						cisto()
						main()
						continue
				if uspech != True:
					print("Příliš mnoho chybných pokusů")
					print("ukončuji...")
					time.sleep(3)
					sys.exit()	
		cisto()
	elif choice == 8 and logged_as == "admin":
		while True:
			cisto()
			main()
			hlavni1 = input("|Uživatelské jméno|: ")
			hlavni1 = hashlib.sha256(hlavni1.encode())
			hlavni1 = hlavni1.hexdigest()
			with open("credentials.txt", "r", encoding="utf-8") as file:
				radky = file.readlines()
				radek = radky[0].split(",")
				important = -1
				mozna22 = ""
				for slovo in radek:
					try:
						important += 1
						mozna = slovo.split(":")[0]
						mozna2 = slovo.split(":")[1]
						if mozna == hlavni1:
							mozna22 = mozna2
							important2 = important
							break
					except IndexError:
						pass
			if mozna22 == "":
				input("\n\t|Uživatelské jméno nenalezeno, Enter pro pokračování|")
				continue
			else:
				hlavni2 = getpass.getpass("|Původní heslo|: ")
				hlavni2 = hashlib.sha256(hlavni2.encode())
				hlavni2 = hlavni2.hexdigest()
				if hlavni2 != mozna22:
					input("\n\t|Špatné heslo, Enter pro pokračování|")
					continue
				else:
					while True:
						hlavni3 = getpass.getpass("|Nové heslo|: ")
						hlavni4 = getpass.getpass("|Znovu nové heslo|: ")
						if hlavni3 != hlavni4:
							input("|Hesla se neshodují, Enter pro pokračování|")
							continue
						else:
							break
					nove_heslo = hashlib.sha256(hlavni3.encode())
					nove_heslo = nove_heslo.hexdigest()
					hlavni4 = nove_heslo
					with open("credentials.txt", "r", encoding="utf-8") as file:
						radky = file.readlines()
						radky = radky[0].split(",")
						if important2 > 0:
							radky[important2] = f",{hlavni1}:{nove_heslo},"
						else:
							radky[important2] = f"{hlavni1}:{nove_heslo},"
					with open("credentials.txt", "w", encoding="utf-8") as file:
						file.writelines(radky)
					print("\t|Heslo úspěsně změněno|")
					time.sleep(1)
					cisto()
					break
	elif choice == 9 and logged_as == "admin":
		while True:
			cisto()
			main()
			hlavni1 = input("|Uživatelské jméno (Q pro konec)|: ")
			if hlavni1 == "admin":
				print("\t|Nelze odebrat admina!|")
				time.sleep(1)
				cisto()
				continue
			elif hlavni1.lower() == "q":
				cisto()
				break
			hlavni1 = hashlib.sha256(hlavni1.encode())
			hlavni1 = hlavni1.hexdigest()
			with open("credentials.txt", "r", encoding="utf-8") as file:
				radky = file.readlines()
				radek = radky[0].split(",")
				important = -1
				mozna22 = ""
				for slovo in radek:
					try:
						important += 1
						mozna = slovo.split(":")[0]
						mozna2 = slovo.split(":")[1]
						if mozna == hlavni1:
							mozna22 = mozna2
							important2 = important
							break
					except IndexError:
						pass
			if mozna22 == "":
				input("\n\t|Uživatelské jméno nenalezeno, Enter pro pokračování|")
				continue
			else:
				hlavni2 = getpass.getpass("|Heslo|: ")
				hlavni2 = hashlib.sha256(hlavni2.encode())
				hlavni2 = hlavni2.hexdigest()
				if hlavni2 != mozna22:
					input("\n\t|Špatné heslo, Enter pro pokračování|")
					continue
				else:
					with open("credentials.txt", "r", encoding="utf-8") as file:
						radky = file.readlines()
						radky = radky[0].split(",")
						cisilka = len(radky)
						radky2 = []
						cislo = 0
						for okay in radky:
							cislo += 1
							if okay.split(":")[0] == hlavni1 and okay.split(":")[1] == hlavni2:
								pass
							else:
								if cisilka == cislo:
									radky2.append(f"{okay}")
								else:
									radky2.append(f"{okay},")
					with open("credentials.txt", "w", encoding="utf-8") as file:
						file.writelines(radky2)	
					print("\t|Uživatel úspěšně odebrán|")
					time.sleep(1)
					cisto()
					break					
	elif choice == 10 and logged_as == "admin" or logged_as != "admin" and choice == 4:
		cisto()
		main()
		try:	
			with open("Vysledky.txt", "r", encoding="utf-8") as file:
				radky = file.readlines()
				for radek in radky:
					slova = radek.split(",")
					udaj1 = slova[0].strip()
					udaj2 = slova[1].strip()
					udaj3 = slova[2].strip()
					NotFound = True
					i = 0
					while NotFound:
						i += 1
						pojd = str(i)
						pojd = hashlib.sha256(pojd.encode())
						pojd = pojd.hexdigest()
						if pojd == udaj2:
							udaj2 = i
							NotFound = False
					udaj2 = int(udaj2)
					i = 0
					for i in range(1001):
						j = i / 10
						pojd = str(j)
						pojd = hashlib.sha256(pojd.encode())
						pojd = pojd.hexdigest()
						if pojd == udaj3:
							udaj3 = j
							break
					print(f"|{udaj1}|\n\t |Pokusy: {udaj2}| \n\t |Průměr úspěšnosti| -> |{udaj3}%|")
					
			input("\n\t\tEnter pro pokračování")
			cisto()
		except FileNotFoundError:
			input("Žádné výsledky nejsou k dispozici, Enter pro pokračování")
			cisto()				
#Jak0ub dne 04.09.2024
#Dne 17.9.2024 -> přidána funkce průměru úspěšnosti (Chystá se nová funkce pro session cookie)
#Dne 18.9.2024 -> přidána funkce mazání uživatelů a úpravy hesel. Také redesign menu pro uživatele a admina. Oprava chyby duplicitních jmen v register sekci	
