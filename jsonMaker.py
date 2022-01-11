"""
To-Do
After being read, be able to edit each entry
Add new attribute (will be for the null attribute)

"""

import json


digimonCounter = 1

class DigimonList:
	def __init__(self):
		self.digimonList = []

	def getDigimonList(self):
		return self.digimonList

	def printDigimonList(self):
		if self.length() == 0:
			print("Empty list.")
		else:
			for i in range(self.length()):
				print(str(i) + ":\t" + self.digimonList[i].toString())

	def delete(self, toDelete):
		self.digimonList.pop(toDelete)
		i = toDelete
		for i in range(len(self.digimonList)):
			self.digimonList[i].setCardNumber(self.digimonList[i].getCardNumber() - 1)
		global digimonCounter
		digimonCounter -= 1

	def insert(self):
		name = input("Name?")
		rarity = input("Rarity?")
		self.digimonList.append(Digimon(name, rarity))

	def length(self):
		return len(self.digimonList)



class Digimon:
	def __init__(self, name, rarity):
		self.name = name 
		self.rarity = rarity
		global digimonCounter
		self.cardNumber = digimonCounter
		digimonCounter += 1

	def setName(self, newName):
		self.name = newName

	def setRarity(self, newRarity):
		self.rarity = newRarity

	def setCardNumber(self, newCardNumber):
		self.cardNumber = newCardNumber

	def getName(self):
		return self.name 

	def getRarity(self):
		return self.rarity

	def getCardNumber(self):
		return self.cardNumber

	def toString(self):
		return "Name: " + self.name + "\tRarity: " + self.rarity + "\tCardNumber: " + str(self.cardNumber)

	def toJSONObject(self):
		return "{\"cardNumber\": " + str(self.cardNumber) + ",\"name\": \"" + self.name + "\",\"rarity\": \"" + self.rarity + "\"},\n"

	def digimonEditMenu(self):
		print(self.toString())
		print("Edit Digimon:")
		print("0: Edit name")
		print("1: Edit rarity")
		print("2: Edit number")
		command = input()
		if command == '0':
			self.name = input("New Name:")
		elif command == '1':
			self.rarity = input("New Rarity:")
		elif command == '2':
			self.cardNumber = int(input("New CardNumber"))
		return self




def editNumberCommand():
	print("digimonCounter is " + str(digimonCounter))
	editNumberCommand = input("What number should digimonCounter be set to?")
	check = input("Are you sure you want it to be " + str(editNumberCommand))
	while check == 'no':
		print("digimonCounter is " + str(digimonCounter))
		editNumberCommand = input("What number should digimonCounter be set to?")
		check = input("Are you sure you want it to be " + str(editNumberCommand))


def clearScreen():
	for i in range(20):
		print()


def readJSON():
	fileName = input(" set name: ")
	fileName = "/mnt/c/Users/ryanm/Documents/Coding/DigimonJSON/" + fileName + ".json"
	verifyFile = open(fileName)
	a = verifyFile.read()
	b = json.loads(a)
	dList = DigimonList()
	for item in b.values():
		for data in item:
			dList.digimonList.append(Digimon(data["name"], data["rarity"]))

	for item in dList.digimonList:
		print(item.toString())

def main():
	dList = DigimonList()
	while True:
		print("Main Menu:")
		print("0: Print currentList")
		print("1: Print digimonCounter")
		print("2: Edit digimonCounter")
		print("3: Insert Digimon")
		print("4: Edit Digimon")
		print("q: Quit")
		print("r: Read")

		command = input()
		if command == '0':
			clearScreen()
			dList.printDigimonList()
		elif command == '1':
			clearScreen()
			print(digimonCounter)
		elif command == '2':
			clearScreen()
			editNumberCommand()
		elif command == '3':
			clearScreen()
			dList.insert()
		elif command == '4':
			clearScreen()
			dList.printDigimonList()
			index = int(input("Which entry would you like to edit?"))
			if 0 <= index and dList.length() > index:
				dList.digimonList[index].digimonEditMenu()
		elif command == 'q':
			break
		elif command == 'r':
			readJSON()

	return dList 

def digimonListToJSONString(dList):
	toReturn = "{\n\t\"data\":\n\t[\n\t\t"
	for item in dList.digimonList:
		toReturn += item.toJSONObject()
	toReturn += "\t]\n}"
	return toReturn		

toJson = main()
jsonString = digimonListToJSONString(toJson)
"""
fileName = input("Input set name: ")
fileName = "/mnt/c/Users/ryanm/Documents/Coding/DigimonJSON/" + fileName + ".json"
print(fileName)
try:
	verifyFile = open(fileName, "r")
except FileNotFoundError:
	print("File not found")
	
f = open(fileName, "a")
f.write(jsonString)
"""