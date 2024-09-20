import getpass
import hashlib
import time
import os
import sys
import platform
import random
#Variables
logged_as = ""
succes = False
nothing = False
right = 0
errors = 0
logged = False
#Functions
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
def check():
	try:
		with open("credentials.txt", "r", encoding="utf-8") as file:
			lines = file.readlines()
	except FileNotFoundError:
		with open("credentials.txt", "w", encoding="utf-8") as file:
			file.write("8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918:e7cf3ef4f17c3999a94f2c6f612e8a888e5b1026878e4e19398b23bd38ec221a,") #Deafult Username and Password
			nothing = True
			lines = []
	if len(lines) == 0:
		with open("credentials.txt", "w", encoding="utf-8") as file:
			file.write("8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918:e7cf3ef4f17c3999a94f2c6f612e8a888e5b1026878e4e19398b23bd38ec221a,") #Deafult Username and Password
#System check
platform_system = platform.system()
if platform_system == "Windows":
	def clean():
		os.system("cls")
else:
	def clean():
		os.system("clear")
#File for vocabulary
try:
	with open("words_configFile.txt", "r", encoding="utf-8") as file:
		lines = file.readlines()
except FileNotFoundError:
	f = open("words_configFile.txt", "a")
	f.close()
#loading
clean()
main()
time.sleep(0.6)
clean()
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
clean()
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
clean()
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
clean()
#Main Menu
while True:
	main()
	if logged_as != "":
		print(f"\t\t|Logged as: {logged_as}|")
	if logged_as == "":
		logged_as = "None"
		print("\t\t|Not Logged|")
	if logged_as == "admin":
		choice = input("Enter number of action:\n |1| -> |Add vocabulary|\n |2| -> |Remove Words| \n |3| -> |Start Practicing|\n |4| -> |Search availability of words| \n |5| -> |List current vocabulary| \n |6| -> |Login|\n |7| -> |Register|\n |8| -> |Password change|\n |9| -> |Delete user|\n |10| -> |User score|\n\t")
	else:
		choice = input("Enter number of action:\n |1| -> |Start Practicing|\n |2| -> |List current vocabulary| \n |3| -> |Login|\n |4| -> |User score|\n\t")		
	try:
		choice = int(choice)
	except ValueError:
		print("\t\tEnter number from the menu!")
		time.sleep(1)		
		clean()
		continue		
	if choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 and choice != 7 and choice != 8 and choice != 9 and choice != 10 and logged_as == "admin":
		print("\t\t1-10!")
		time.sleep(1)		
		clean()
		continue
	elif logged_as != "admin" and choice != 1 and choice != 2 and choice != 3 and choice != 4:
		print("\t\t1-4!")
		time.sleep(1)		
		clean()
		continue
	if choice == 1 and logged_as == "admin":
		clean()
		main()
		print("|Q| -> |End Loop|\n")
		while True:
			add = input("Enter word: ")
			if add.lower() == "q":
				clean()				
				break
			add1 = input("Enter word translation: ")
			if add1.lower() == "q":
				clean()				
				break
			with open("words_configFile.txt", "r", encoding="utf-8") as file:
				lines = file.readlines()
				lines.append(f"{add}:{add1},")
			with open("words_configFile.txt", "w", encoding="utf-8") as file:
				file.writelines(lines)
			print("\tEnrolled✔️\n")
	elif choice == 2 and logged_as == "admin":
		while True:
			clean()
			main()
			lines2 = []
			success = False
			print("|Q| -> |End Loop|\n")
			delete = input("Enter word to be deleted: ")
			if delete.lower() == "q":
				clean()	
				break
			with open("words_configFile.txt", "r", encoding="utf-8") as file:
				lines = file.readlines()
				for i in range(len(lines)):
					columns = lines[i].strip().split(",")
					for column in columns:
						slup = column.split(":")
						try:
							one = slup[0]
							two = slup[1]
							if one.lower() == delete.lower() or two.lower() == delete.lower():
								pass
								success = True
							else:
								lines2.append(f"{one}:{two},")
						except IndexError:
							pass
				lines = lines2
			if success == True:
				with open("words_configFile.txt", "w", encoding="utf-8") as file:
					file.writelines(lines2)
				input("\tDeleted✔️\n\t\tEnter to continue")
			else:
				input("\tNot Found✖️\n\t\tEnter to continue")					
	elif choice == 3 and logged_as == "admin" or logged_as != "admin" and choice == 1:
		if logged_as == "None":
			clean()
			main()
			input("You're not logged, Enter to continue")
			clean()
			continue
		clean()
		main()
		print("Word translation:")
		with open("words_configFile.txt", "r", encoding="utf-8") as file:
			lines = file.readlines()
			for line in lines:
				columns = line.strip().split(",")
				numbers = []
				while len(numbers) != len(columns):
					number = random.randint(0, len(columns) - 1)
					if number in numbers:
						pass
					else:
						numbers.append(number)
				for i in range(len(numbers)):
					verify = numbers[i]
					column = columns[verify]
					main2 = column.split(":")
					if len(main2) != 2:
						pass
					else:
						random_ = random.randint(0, 1)
						if random_ == 1:
							secondary = main2[0]
							main2 = main2[1]
						else:
							secondary = main2[1]
							main2 = main2[0]
						quest = input(f"|{main2}|: ")
						if quest.lower() == secondary:
							print("\t✔️")
							right += 1
						else:
							print("\t✖️")
							errors += 1
		if right == 0 and errors == 0:
			clean()
			main()
			input("No words entered, Enter to continue")
			clean()
		else:
			with open("results.txt", "a", encoding="utf-8") as file:
				pass
			with open("results.txt", "r", encoding="utf-8") as file:
				avg = round((100 / (errors + right)) * right, 1) 
				lines = file.readlines()
				info3 = -33
				info2 = 1
				i = 0
				number_important = -1
				line_number = -1
				for line in lines:
					line_number += 1
					words = line.split(",")
					info1 = words[0]
					info22 = words[1]
					info333 = words[2]
					if info1 == logged_as:
						NotFound = True
						while NotFound:
							i += 1
							statement = str(i)
							statement = hashlib.sha256(statement.encode())
							statement = statement.hexdigest()
							if statement == info22:
								info2 = i
								NotFound = False
						info2 = int(info2)
						number_important = line_number
						info2 += 1
						i = 0
						for i in range(1002):
							j = i / 10
							statement = str(j)
							statement = hashlib.sha256(statement.encode())
							statement = statement.hexdigest()
							if statement == info333:
								info3 = j
								break
			avg2 = avg
			if info3 == -33:
				avg = float(avg)
			else:
				avg = round((info3 + avg) / 2, 1)	
			avg = str(avg)
			avg = hashlib.sha256(avg.encode())
			avg = avg.hexdigest()			
			tries = str(info2)
			tries2 = hashlib.sha256(tries.encode())
			tries2 = tries2.hexdigest()
			if number_important != -1:
				lines[number_important] = f"{logged_as},{tries2},{avg},\n"
			else:
				lines.append(f"{logged_as},{tries2},{avg},\n")
			with open("results.txt", "w", encoding="utf-8") as file:
				file.writelines(lines)
			input(f"\n|Correct| -> |{right}|\n|Wrong| -> |{errors}|\n|Success percentage| -> |{avg2}%|")
			right = 0
			errors = 0
			clean()
	elif choice == 4 and logged_as == "admin":
		while True:
			clean()
			main()
			print("|Q| -> |End loop|\n")
			search = input("Search for word... ")
			if search.lower() == "q":
				clean()
				break
			found = False
			while True:
				with open("words_configFile.txt", "r", encoding="utf-8") as file:
					lines = file.readlines()
					for i in range(len(lines)):
						columns = lines[i].strip().split(",")
						for column in columns:
							try:
								first = column.split(":")[0].strip()
								second = column.split(":")[1].strip()
								if first.lower() == search.lower() or second.lower() == search.lower():
									found1 = first
									found2 = second
									found = True
							except IndexError:
								pass
				if found == False:
					input("\tNot Found✖️\n\t\tEnter to continue")
					break
				else:
					input(f"\tFound✔️: |{found1}| -> |{found2}|\n\t\tEnter to continue")
					break
			clean()
	elif choice == 5 and logged_as == "admin" or logged_as != "admin" and choice == 2:
		clean()
		main()
		print("Current vocabulary\n")
		with open("words_configFile.txt", "r", encoding="utf-8") as file:
			lines = file.readlines()
			for i in range(len(lines)):
				columns = lines[i].strip().split(",")
				for column in columns:
					try:
						first = column.split(":")[0].strip()
						second = column.split(":")[1].strip()
						print(f"|{first}| -> |{second}|")
					except IndexError:
						pass
		input("\nEnter to continue")
		clean()
	elif choice == 6 and logged_as == "admin" or logged_as != "admin" and choice == 3:
		succes = False
		quit = False
		clean()	
		main()
		check()
		for i in range(3):
			clean()	
			main()
			print("|Q| -> |End loop|\n")
			print("|Login|")
			entered = input("|Username|: ")
			if entered.lower() == "q":
				clean()
				quit = True
				break
			logged_as = entered
			entered2 = getpass.getpass("|Password|: ")
			entered = hashlib.sha256(entered.encode())
			entered = entered.hexdigest()
			entered2 = hashlib.sha256(entered2.encode())
			entered2 = entered2.hexdigest()
			with open("credentials.txt", "r", encoding="utf-8") as file:
				lines = file.readlines()
				for line in lines:
					columns = line.strip().split(",")
					try:
						for column in columns:
							words = column.split(":")
							uzivatel = words[0]
							password = words[1]
							if entered == uzivatel:
								if entered2 == password:
									succes = True
					except IndexError:
						pass
			if succes == True:
				break
			else:
				input("Wrong credentials, Enter to continue")
				continue
		if quit == True:
			logged_as = ""
		elif succes != True:
			print("Too many false attempts")
			print("terminating...")
			time.sleep(3)
			sys.exit()	
		clean()	
	elif choice == 7 and logged_as == "admin":
		while True:
			succes = False
			clean()
			main()
			check()
			if logged_as != "":
				print("|Q| -> |End loop|\n")
				print("|Register|")
				user = input("|Username|: ")
				if user.lower() == "q":
					break
				user = hashlib.sha256(user.encode())
				user = user.hexdigest()
				with open("credentials.txt", "r", encoding="utf-8") as file:
					lines = file.readlines()
					lines = lines[0].split(",")
					for line in lines:
						first = line.split(":")[0]
						if user == first:
							input("\t|Username already registered, Enter to continue|")
							break
					if user == first:
						continue
				while True:
					pasw = getpass.getpass("|Password|: ")
					pasw2 = getpass.getpass("|Password again|: ")
					if pasw == pasw2:
						break
					else:
						input("\tPasswords do not match, Enter to continue")
						clean()
						main()
						continue
				pasw = hashlib.sha256(pasw.encode())
				pasw = pasw.hexdigest()
				pasw2 = ""
				with open("credentials.txt", "r", encoding="utf-8") as file:
					lines = file.readlines()
					lines.append(f"{user}:{pasw},")
				with open("credentials.txt", "w", encoding="utf-8") as file:
					file.writelines(lines)
				input("Credentials were saved, Enter to continue")
				clean()
		clean()
	elif choice == 8 and logged_as == "admin":
		while True:
			clean()
			main()
			print("|Q| -> |End loop|\n")
			print("|Change Password|")
			main21 = input("|Username|: ")
			if main21.lower() == "q":
				clean()
				break
			main21 = hashlib.sha256(main21.encode())
			main21 = main21.hexdigest()
			with open("credentials.txt", "r", encoding="utf-8") as file:
				lines = file.readlines()
				line = lines[0].split(",")
				important = -1
				mabye22 = ""
				for word in line:
					try:
						important += 1
						mabye = word.split(":")[0]
						mabye2 = word.split(":")[1]
						if mabye == main21:
							mabye22 = mabye2
							important2 = important
							break
					except IndexError:
						pass
			if mabye22 == "":
				input("\n\t|Username not found, Enter to continue|")
				continue
			else:
				main22 = getpass.getpass("|Old Password|: ")
				main22 = hashlib.sha256(main22.encode())
				main22 = main22.hexdigest()
				if main22 != mabye22:
					input("\n\t|Wrong password, Enter to continue|")
					continue
				else:
					while True:
						main23 = getpass.getpass("|New password|: ")
						main24 = getpass.getpass("|Again new password|: ")
						if main23 != main24:
							input("|Passwords do not match, Enter to continue|")
							clean()
							main()
							continue
						else:
							break
					new_password = hashlib.sha256(main23.encode())
					new_password = new_password.hexdigest()
					main24 = new_password
					with open("credentials.txt", "r", encoding="utf-8") as file:
						lines = file.readlines()
						lines = lines[0].split(",")
						if important2 > 0:
							lines[important2] = f",{main21}:{new_password},"
						else:
							lines[important2] = f"{main21}:{new_password},"
					with open("credentials.txt", "w", encoding="utf-8") as file:
						file.writelines(lines)
					print("\t|Password sucesfully changed|")
					time.sleep(1)
					clean()
					break
	elif choice == 9 and logged_as == "admin":
		while True:
			clean()
			main()
			print("|Q| -> |End loop|\n")
			print("|Unregister|")
			main21 = input("|Username|: ")
			if main21 == "admin":
				print("\t|Cannot remove admin!|")
				time.sleep(1)
				clean()
				continue
			elif main21.lower() == "q":
				clean()
				break
			main21 = hashlib.sha256(main21.encode())
			main21 = main21.hexdigest()
			with open("credentials.txt", "r", encoding="utf-8") as file:
				lines = file.readlines()
				line = lines[0].split(",")
				important = -1
				mabye22 = ""
				for word in line:
					try:
						important += 1
						mabye = word.split(":")[0]
						mabye2 = word.split(":")[1]
						if mabye == main21:
							mabye22 = mabye2
							important2 = important
							break
					except IndexError:
						pass
			if mabye22 == "":
				input("\n\t|Username not found, Enter to continue|")
				continue
			else:
				main22 = getpass.getpass("|Password|: ")
				main22 = hashlib.sha256(main22.encode())
				main22 = main22.hexdigest()
				if main22 != mabye22:
					input("\n\t|Wrong password, Enter to continue|")
					continue
				else:
					with open("credentials.txt", "r", encoding="utf-8") as file:
						lines = file.readlines()
						lines = lines[0].split(",")
						cisilka = len(lines)
						lines2 = []
						number = 0
						for okay in lines:
							number += 1
							if okay.split(":")[0] == main21 and okay.split(":")[1] == main22:
								pass
							else:
								if cisilka == number:
									lines2.append(f"{okay}")
								else:
									lines2.append(f"{okay},")
					with open("credentials.txt", "w", encoding="utf-8") as file:
						file.writelines(lines2)	
					print("\t|Username sucesfully deleted|")
					time.sleep(1)
					clean()
					break					
	elif choice == 10 and logged_as == "admin" or logged_as != "admin" and choice == 4:
		clean()
		main()
		try:	
			with open("results.txt", "r", encoding="utf-8") as file:
				lines = file.readlines()
				for line in lines:
					words = line.split(",")
					info1 = words[0].strip()
					info2 = words[1].strip()
					info3 = words[2].strip()
					NotFound = True
					i = 0
					while NotFound:
						i += 1
						statement = str(i)
						statement = hashlib.sha256(statement.encode())
						statement = statement.hexdigest()
						if statement == info2:
							info2 = i
							NotFound = False
					info2 = int(info2)
					i = 0
					for i in range(1001):
						j = i / 10
						statement = str(j)
						statement = hashlib.sha256(statement.encode())
						statement = statement.hexdigest()
						if statement == info3:
							info3 = j
							break
					print(f"|{info1}|\n\t |Tries: {info2}| \n\t |Average success rate| -> |{info3}%|")
					
			input("\n\t\tEnter to continue")
			clean()
		except FileNotFoundError:
			input("No results, Enter to continue")
			clean()				
#Created by Jak0ub on 04.09.2024
#Day 17.9.2024 -> added Average success rate function (New session cookie function is coming)
#Day 18.9.2024 -> added the function of deleting users and editing passwords. Also redesign menu for users and admin. Correction of errors of duplicate names in the register section
#Day 19.9.2024 -> Translated to English, small bugs fixes	
