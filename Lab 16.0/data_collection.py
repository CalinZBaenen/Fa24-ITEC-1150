"""
Description:  A simple contact-list management program.
Author:       Calin "Katty" Baenen
Date:         24/11/25
"""
import pyinputplus as pyip
import csv
import os
import re

from typing import TypedDict, TextIO





WHITESPACE_REGEX = re.compile(r"\s+")
NEWLINES_REGEX   = re.compile(r"(\r?\n)+")
PHONE_REGEX      = re.compile(r"(\+?\d)?(\s+|-)?(\(\d{3}\)|\d{3})(\s+|-)?\d{3}(\s+|-)?\d{4}")
NAME_REGEX       = re.compile(r"[A-Z-]+((\s+([A-Z]\.|[A-Z-]+))?\s+[A-Z-]+)?", re.IGNORECASE)





class Contact(TypedDict):
	"""
	`Contact` represents someone that a user knows, containing key
	contact-information about them.
	"""
	number:str
	email:str
	name:str





# [I]nput
def get_contact_info() -> tuple[str, str, str]:
	"""
	Gets the contact information for a particular user in the order: name,
	email, phonenumber.
	"""
	return Contact({
		("name", input_name()),
		("email", pyip.inputEmail("Enter contact email: ")),
		("number", input_phone())
	})



def handle_insertion(database:list[Contact], contact:Contact):
	"""
	Inserts a `Contact` into a contact-list.
	"""
	name = contact["name"].casefold()
	# Check if a similarly named contact exists and offer the user to
	#  replace the contact if so.
	for known in database:
		if known["name"].casefold() == name:
			print(f"You are trying to add another contact with the name {contact['name']}")
			if pyip.inputYesNo("Would you like to replace the previous contact?") == "yes":
				database.remove(known)
				database.append(contact)
			break
	else:
		database.append(contact)



# [P]rocessing
def export_contacts(database:list[Contact], file:TextIO):
	file.truncate(0)
	file.seek(0)
	
	res = ""
	for contact in database:
		res += f"{contact['name']},{contact['email']},{contact['number']}\n"
	
	file.write(res.strip())



# [P]rocessing
def import_contacts(database:list[Contact], file:TextIO):
	"""
	Import a list ov contacts from a CSV string describing each contact to
	be added.
	"""
	# Create contact-list from CSV data, then handle each insertion.
	new_contacts = list(csv.reader(file))
	for contact in new_contacts:
		handle_insertion(database, Contact({"name": contact[0], "email": contact[1], "number": contact[2]}))



# [O]utput
def print_database(database:list[Contact]):
	# Calculate the greatest length ov information's type.
	lname = 0
	lema  = 0
	lpn   = 0
	for contact in database:
		# Name.
		l = len(contact["name"])
		if l > lname:
			lname = l
		
		# Email address.
		l = len(contact["email"])
		if l > lema:
			lema = l
		
		# Phonenumber.
		l = len(contact["number"])
		if l > lpn:
			lpn = l
	
	# Print each contact with correct spacing.
	for contact in database:
		print(f"{contact['name']: <{lname}} | {contact['email']: <{lema}} | {contact['number']: >{lpn}}")



# [P]rocessing
def input_phone():
	"""
	Get a phonenumber from the user.
	"""
	while True:
		n = input("Enter contact phonenumber: ").strip()
		if not PHONE_REGEX.match(n) is None:
			return WHITESPACE_REGEX.sub('-', n)
		print("The provided input was not recognized as a phonenumber. — Please try again.")



# [P]rocessing
def input_name():
	while True:
		n = input("Enter contact name: ").strip()
		if not NAME_REGEX.match(n) is None:
			return WHITESPACE_REGEX.sub(' ', n)
		print("The provided input was not recognized as a name. — Please try again.")





# [M]ain
def main() -> int:
	print("Welcome to Contact-List Creation Program!\nType for \"help\" for help.")
	
	database = list()
	clf      = os.fdopen(os.open("contacts.csv", os.O_CREAT | os.O_RDWR), "r+")
	
	import_contacts(database, clf)
	
	try:
		# Get commands from the user.
		while True:
			cmd = input("> ").strip().casefold()
			
			match cmd:
				# Get help.
				case "help" | '?' | '1':
					print("1. help\n2. add\n3. view\n4. exit")
				
				# Add a user to the contact-list.
				case "add" | '+' | '2':
					handle_insertion(database, get_contact_info())
				
				# View the database.
				case "view" | '3':
					print_database(database)
				
				# Exit the program.
				case "exit" | '4':
					break
	except KeyboardInterrupt:
		pass
	
	export_contacts(database, clf)
	return 0

if __name__ == "__main__":
	exit(main())

'''
Erik:
    Fun as always!
'''