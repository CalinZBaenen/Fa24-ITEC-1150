"""
Description:  A simple program which can view, add to, and take from, a
               registry ov users.
Author:       Calin "Katty" Baenen
Date:         24/10/23
"""

# I don't usually like doing "glob imports", but I'm doing it here so I
#  don't have to write the name ov everything I need.
from ui import *

import re





# Messages.
MALFORMED_SYNTAX_MESSAGE = "Malformed syntax : expected username, first-name, and last-name."
NOT_REGISTERED_MESSAGE   = "{} does not appear to be registered."
WELCOME_MESSAGE          = "Welcome to the user-database application!\nType \"help\" for help."

# Regexes.
FIRST_CHAR_REGEX = re.compile(r"\b[A-Z]", re.IGNORECASE)
VULGARITY_REGEX  = re.compile(r"((c|k)(_|-)*o?(_|-)*u?(_|-)*n(_|-)*t(_|-)*r(_|-)*((i|e)+|y+)+|(United[\s\._-]*States?|(\b|_|-)U[\s\._-]*S(\b|_|-))|(Japan|(\b|_|-)J[\s\._-]*P(\b|_|-))|(Sweden|(\b|_|-)S[\s\._]*E(\b|_|-)))|(Canada|(\b|_|-)C[\s\._-]*A(\b|_|-))|(Mexico|(\b|_|-)M[\s\._-]*X(\b|_|-))|(United Kingdom|(\b|_|-)U[\s\._-]*K(\b|_|-))", re.IGNORECASE)





# [I]nput
def get_nonempty_input(prompt:str="") -> str:
	"""
	Gets non-empty input from the user.
	"""
	
	while True:
		out = input(prompt).strip()
		if len(out) > 0:
			return out



# [P]rocessing
def handle_insertion(database:dict[str, tuple[str, str]], uname:str, fname:str, lname:str):
	#  "[...] there must be no reference to countries in the finished program!"?
	#  You got it, boss!
	if VULGARITY_REGEX.search(uname) is not None:
		print("The provided username could not be registered because it contains a forbidden word!")
		return
	
	for user in database:
		if uname.lower() == user.lower():
			print(f"A user with the username {user} – {database[user][0]} {database[user][1]} – already exists!\nUse the \"edit\" command to edit their name.")
			return
	
	fname, lname = capitalize_precise(fname), capitalize_precise(lname)
	
	database[uname] = (fname, lname)
	print(f"{fname} {lname} was registered with the username {uname}.")



# [P]rocessing
def handle_deletion(database:dict[str, tuple[str, str]], uname:str):
	"""
	Takes a database and a username, removing the specified user from the
	database,
	"""
	
	# Get the first and last name from the removed username.
	# I would use the `.get()` method, but I want to preserve
	#  username-casing.
	#
	# Now, you might think that if I tried to fetch the keys ov the map –
	#  maybe did something fancy, like a list comprehension – THEN the
	#  for-loop would not be necessary.
	# ... I made this consideration; however, the drawback is that I can't
	#  access the (matched) username (by simply referring to `user`).
	#
	# Loops are always a programmer's friend, when in doubt.
	for user in database:
		if uname.lower() == user.lower():
			(fname, lname) = database.pop(user)
			print(f"{fname} {lname} ({user}) has been removed.")
			break
	else:
		print(NOT_REGISTERED_MESSAGE.format(uname))



# Handle the command provided by the user.
# In an actual program, you would probably only pass the command and
#  arguments; however, I have no other way for `main` and `handle_command`
#  to dually access the database (that I'm aware ov) without creating a
#  global variable – which I am assuming you don't want us to do,
#  considering we've been learning to put everything into a function or so.
#
# [P]rocessing
def handle_command(database:dict[str, tuple[str, str]], cmd:Command, *args:str):
	match cmd:
		# Delete a user from the database.
		case Command.Delete:
			if len(args) > 0:
				for uname in args:
					handle_deletion(database, uname)
			else:
				handle_deletion(database, get_username())
		
		# Edit an entry.
		case Command.Edit:
			if len(args) == 3:
				handle_edit(database, *args)
			elif len(args) > 0:
				print(MALFORMED_SYNTAX_MESSAGE)
			else:
				print("Enter the username ov the person whose name you wish to edit.")
				handle_edit(database, get_username(), *get_fullname())
		
		# Exit the program.
		case Command.Exit:
			exit(0)
		
		# Prints help.
		case Command.Help:
			for cmd in Command:
				print(f"{cmd}\n\t{description_for(cmd)}")
		
		# Displays the database in a user-friendly way.
		case Command.View:
			print_database(database, *args)
		
		# Add a registry entry for a new user.
		case Command.Add:
			if len(args) == 3:
				handle_insertion(database, *args)
			elif len(args) > 0:
				print(MALFORMED_SYNTAX_MESSAGE)
			else:
				handle_insertion(database, get_username(), *get_fullname())



# Prints the database.
# [O]utput
def print_database(database:dict[str, tuple[str, str]], *args:str):
	# Helper variables.
	print_by_user = False
	un_args       = []
	args          = [arg.lower() for arg in args]
	
	# Get the users in the database as a list, then sort them if it is
	#  requested.
	users = [user for user in database]
	if "sort" in args:
		users.sort()
	
	# Determine whether or not to use print-by-user.
	for arg in args:
		if arg in [user.lower() for user in users]:
			print_by_user = True
			un_args.append(arg)
	
	# Only use the suggested usernames with print-by-user.
	if print_by_user:
		users = list(filter(lambda username: username.lower() in args, users))
	
	# Get the length ov the longest name so that content can be properly
	#  aligned.
	lngst_name_len = 0
	for user in users:
		if len(user) > lngst_name_len:
			lngst_name_len = len(user)
	
	# Display the usernames.
	print("Usernames:")
	for user in users:
		print(f"\t{user:<{lngst_name_len}}", end="")
		if "show-names" in args:
			print(f" : {database[user][0]} {database[user][1]}", end="")
		print()



# [I]nput
def get_fullname() -> tuple[str, str]:
	"""
	Gets a twopart name from the user.
	"""
	
	prompt = "Name"
	fname  = None
	lname  = None
	
	while True:
		names = list(filter(lambda s: len(s) > 0, get_nonempty_input(f"{prompt}: ").split()))
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
	
	return (fname, lname)



# [I]nput
def get_username() -> str:
	"""
	Gets a username, replacing any spaces with underscores.
	"""
	
	return re.sub(r"\s", '_', get_nonempty_input("Username: "))



# This was made as a program-specific function due to the program-specfic
#  due to the program-specific descriptions.
def description_for(cmd:Command):
	match cmd:
		case Command.Delete:
			return "Deletes an entry. — Usernames can be provided as arguments to this command."
		case Command.Edit:
			return "Edits an entry. — Supports three-argument syntax."
		case Command.Exit:
			return "Exits the program."
		case Command.Help:
			return "A command that, contrary to popular belief, is valid, and prints the available commands."
		case Command.View:
			return "View all entries that exist. — Optionally, takes two optional arguments, \"show-names\" and \"sort\", as well as any number ov usernames."
		case Command.Add:
			return "Adds an entry. — Supports three-argument syntax."



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
		builder = list(s)
		builder[fch] = builder[fch].capitalize()
		s = "".join(builder)
	except:
		pass
	
	return s



# Edits the name ov a particular user.
# [P]rocessing
def handle_edit(database:dict[str, tuple[str, str]], uname:str, fname:str, lname:str):
	"""
	Edits the name associated with a given user, or creates a new user if
	they did not previously exist.
	"""
	
	for user in database:
		if uname.lower() == user.lower():
			fname, lname = capitalize_precise(fname), capitalize_precise(lname)
			
			(ofname, olname) = database[user]
			database[user] = (fname, lname)
			print(f"{user}'s name was changed from {ofname} {olname} to {fname} {lname}")
			break
	else:
		# Inform the user that this user has not been registered, then
		#  prompt them to decide whether or not they wish to create a new
		#  user with these credentials.
		print(NOT_REGISTERED_MESSAGE.format(uname))
		print(f"Would you like to create a user, {uname}, with the name {fname} {lname}?")
		
		# Ask the user if they want to create a new user with these
		#  credentials.
		yn = get_nonempty_input("[Y / N] ").lower()
		if yn == 'y' or yn == "yes":
			handle_insertion(database, uname, fname, lname)
		elif not (yn == 'n' or yn == "no"):
			print("Your input was not a yes or no answer — \"no\" assumed.")





# [M]ain
def main():
	try:
		print(WELCOME_MESSAGE)
		
		database = {
			"KattyTheEnby": ("Calin", "Baenen"),
			"dreya": ("Adrea", "Baenen"),
			"m3mda": ("Matthew", "Kraus")
		}
		
		while True:
			# `get_command` acts as my [I]nput function.
			(cmd, args) = get_command()
			
			handle_command(database, cmd, *args)
	
	# Stop the pesky KeyboardInterrupt exception from causing that
	#  gigantic error message.
	except KeyboardInterrupt:
		print("\r\nProgram exited via input-apparatus.")

if __name__ == "__main__":
	main()

'''
Erik:
    Outstanding!
'''