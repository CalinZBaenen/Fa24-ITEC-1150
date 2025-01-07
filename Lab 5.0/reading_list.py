"""
Description:  A simple program which can view, add to, and take from, a
               registry ov books.
Author:       Calin "Katty" Baenen
Date:         24/10/30
"""

# I don't usually like doing "glob imports", but I'm doing it here so I
#  don't have to write the name ov everything I need.
from ui import *

import re





# Messages.
NOT_REGISTERED_MESSAGE = "{} does not appear to be registered."
NOT_YESNO_MESSAGE      = "Your input was not a yes or no answer — \"no\" assumed."
WELCOME_MESSAGE        = "Welcome to the readinglist application!\nType \"help\" for help."
BOOKS_MESSAGE          = "{} books by {} are in the list – {}"

# Regexes.
FIRST_CHAR_REGEX = re.compile(r"\b[A-Z]", re.IGNORECASE)
WHITESPACE_REGEX = re.compile(r"\s+")
VULGARITY_REGEX  = re.compile(r"(\b|_|-)u(s|z)e?r(s|z)?(\b|_|-)", re.IGNORECASE)
NO_CAPS_REGEX    = re.compile(r"\b(and|as|at|but|by|for|from|if|in|into|near|nor|o(f|v)|or|so|than|to|upon|with|yet)\b", re.IGNORECASE)





class Name(tuple[str, str]):
	def __format__(self, _):
		return f"{self[0]} {self[1]}"
	
	def lower(self):
		return Name((self[0].lower(), self[1].lower()))

Readinglist = dict[Name, list[str]]





# Backported from Lab 6.0, `text_validator.py`.
# [P]rocessing
def title_caps(s:str) -> str:
	s = WHITESPACE_REGEX.sub(' ', s.lower())
	
	words = s.split()
	i     = 0
	
	for word in words:
		if (NO_CAPS_REGEX.match(word) is None) or i == 0:
			words[i] = word.capitalize()
		i += 1
	
	return ' '.join(words)



# [P]rocessing
def handle_insertion(database:Readinglist, name:Name, title:str):
	#  "[...] there must be no reference to users in the finished program!"?
	#  You got it, boss!
	#
	#  Hey...  wait...  didn't I make this joke already?
	if VULGARITY_REGEX.search(' '.join(name)) is not None or VULGARITY_REGEX.search(title) is not None:
		print("The provided details contain an inappropriate word!\nPlease try to use more appropriate verbiage.")
		return
	
	# Prompt the user to keep or remove previous 
	for author in database:
		if name == author:
			print(BOOKS_MESSAGE.format("One or more", author, "do you wish to replace them?"))
			yn = get_yesno()
			
			if yn is None:
				print(NOT_YESNO_MESSAGE)
				yn = False
			if not yn:
				database[author].append(title)
				return
			
			break
	
	database[name] = list()
	database[name].append(title)
	print(f"The author {name}, with their book, {title}, has been added to the readinglist.")



# [C]onversion
def description_for(cmd:Command):
	match cmd:
		case Command.Delete:
			return "Removes an author's books from the readinglist."
		case Command.Edit:
			return "Correct the title ov a book from a particukar author."
		case Command.Exit:
			return "Exits the program."
		case Command.Help:
			return "Prints the available commands."
		case Command.View:
			return "View all the books in the readinglist."
		case Command.Add:
			return "Adds a book, by a particular author, to the readinglist."



# [P]rocessing
def handle_deletion(database:Readinglist, name:Name):
	"""
	Takes a database and an author's name, removing the specified author,
	and their works, from the readlinglist.
	"""
	
	# Get the first and last name from the removed username.
	# I would use the `.get()` method, but I want to preserve
	#  username-casing.
	for author in database:
		if name == author:
			if len(database[author]) > 1:
				print(BOOKS_MESSAGE.format("Multiple", author, "are you sure you want to delete them?"))
				yn = get_yesno()
				
				if yn is None:
					print(NOT_YESNO_MESSAGE)
					yn = False
				if not yn:
					return
				
				database.pop(author)
				print(f"{author}, and their books, have been removed.")
			break
	else:
		print(NOT_REGISTERED_MESSAGE.format(name))



# [P]rocessing
def handle_command(database:Readinglist, cmd:Command, *args:str):
	match cmd:
		# Delete a user from the database.
		case Command.Delete:
			# NOTE:  Add options for deleting author and book separately.
			handle_deletion(database, get_fullname())
		
		# Edit an entry.
		case Command.Edit:
			# NOTE:  Update code.
			handle_edit(database, get_fullname(), get_title())
		
		# Exit the program.
		case Command.Exit:
			exit(0)
		
		# Prints help.
		case Command.Help:
			for cmd in Command:
				print(f"{cmd}\n\t{description_for(cmd)}")
		
		# Displays the database in a user-friendly way.
		case Command.View:
			print_database(database)
		
		# Add a registry entry for a new user.
		case Command.Add:
			handle_insertion(database, get_fullname(), get_title())



# Prints the database.
# [O]utput
def print_database(database:Readinglist):
	# Display the usernames.
	for author in database:
		print(f"{author[0]} {author[1]}:")
		for title in database[author]:
			print(f"\t{title}")



# [I]nput
def get_fullname() -> Name:
	"""
	Gets a twopart name from the user.
	"""
	
	prompt = "Name"
	fname  = None
	lname  = None
	
	while True:
		names = list(filter(lambda s: len(s) > 0, get_nonempty(f"{prompt}: ").split()))
		no    = len(names)
		
		match no:
			# Both names provided at once!
			case 2:
				fname, lname = names[0], names[1]
				break
			
			# One name at a time. — Slow and steady!
			case 1:
				if fname is None:
					fname = names[0]
					prompt = "Last name"
					continue
				elif lname is None:
					lname = names[0]
				
				break
			
			# INFORMATION OVERLOAD!!!
			case l:
				print(f"Too many ({l}) names were provided – please only choose two.")
	
	fname, lname = capitalize_precise(fname), capitalize_precise(lname)
	return Name((fname, lname))



# [I]nput
def get_title() -> str:
	"""
	Gets the title ov a book.
	"""
	
	return title_caps(input("Book title: ").strip())



# [P]rocessing
def capitalize_precise(s:str) -> str:
	"""
	Capitalizes the first character ov a string, similar to
	`str.capitalize()`; however, non-word-characters are not included, so
	they may precede the first letter, while still allowing it to be
	capitalized.
	"""
	
	try:
		# Get the index ov the string's first (word) character.
		fch = FIRST_CHAR_REGEX.search(s).start()
		
		# Replaces the first (word) character with a capital
		builder = list(s.lower())
		builder[fch] = builder[fch].capitalize()
		s = "".join(builder)
	except:
		pass
	
	return s



# Edits the title ov a book by a particular author.
# [P]rocessing
def handle_edit(database:Readinglist, name:Name, title:str):
	"""
	Edits the title ov a book by particular author, or creates a new user
	if they did not previously exist.
	"""
	
	if VULGARITY_REGEX.search(title) is not None:
		print("Vulgarity can not be edited in!")
		return
	
	for author in database:
		if name == author:
			match len(database[author]):
				case 1:
					print(f"name={name}, author={author}, equal={name==author}, books={database[author]}")
					
					database[author][0] = title
					break
				
				# Offer the user a selection if there is more than one book
				#  registered to a particular author.
				case x if x > 1:
					print(f"name={name}, author={author}, equal={name==author}, books={database[author]}")
					
					print("There is more than one book under this author's name.")
					i = 0
					# I would use `title`... but name-shadowing doesn't
					#  seem to work as expected, which can cause some
					#  very nasty bugs, as I have personally experienced...
					for bookname in database[author]:
						print(f"\t{i}: {bookname}")
						i += 1
					
					edit_idx = get_int("Which book's title would you like to edit? ", max=i-1)
					database[author][edit_idx] = title
					break
	else:
		print(NOT_REGISTERED_MESSAGE.format(name))
			




# [M]ain
def main():
	try:
		print(WELCOME_MESSAGE)
		
		library = {
			Name(("Kyell", "Gold")): ["Waterways"],
			Name(("Calin", "Baenen")): ["An Impossible to Obtain User Manual for This Program  ;)"],
			Name(("Khaled", "Hosseini")): ["The Kite Runner"]
		}
		
		while True:
			# `get_command` acts as my [I]nput function.
			(cmd, args) = get_command()
			
			handle_command(library, cmd, *args)
	
	# Stop the pesky KeyboardInterrupt exception from causing that
	#  gigantic error message.
	except KeyboardInterrupt:
		print("\r\nProgram exited via input-apparatus.")

if __name__ == "__main__":
	main()

'''
Erik:
    Great work.
'''