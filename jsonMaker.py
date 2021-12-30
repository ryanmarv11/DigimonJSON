"""
Things the loop needs to do
Add a new digimon
Edit a digimon by list index
Delete an entry 
Update the card numbers for entries after deletion
Get global number
Edit global number
Print all entries
Print x entries
Add all
Quit

"""


import json

globalNumber = 1


def insert(currentList):
	newEntry = []
	name = input("Name?")
	newEntry.append(name)
	cardNumber = globalNumber
	globalNumber += 1
	name = input("Rarity?")

def editNumberCommand():
	print("globalNumber is " + str(globalNumber))
	editNumberCommand = input("What number should globalNumber be set to?")
	check = input("Are you sure you want it to be " + str(editNumberCommand))
	while check == 'no':
		print("globalNumber is " + str(globalNumber))
		editNumberCommand = input("What number should globalNumber be set to?")
		check = input("Are you sure you want it to be " + str(editNumberCommand))


def main():
	fileName = input("Input set name: ")
	fileName = "/mnt/c/Users/ryanm/Documents/Coding/DigimonJSON/" + fileName + ".json"
	print(fileName)
	try:
		verifyFile = open(fileName, "r")
	except FileNotFoundError:
		print("File not found")
		return

	f = open(fileName, "a")
	f.write("{\n")
	f.write("\t\"data\":\n")
	f.write("[\n")

	size = input("How many cards are in the set?")
	currentList = []
	while True:

		command = input("Input your command: i is for Insert, d is for delete, e is for edit, p is for print, q is for quit")
		if command == 'i':
			insert(currentList)
			break
		elif command == 'edit number':
			editNumberCommand()
		elif command == 'q':
			break




main()