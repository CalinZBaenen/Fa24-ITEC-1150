"""
Description:  A simple program which can view, add to, and take from, a
               registry ov users.
Author:       Calin "Katty" Baenen
Date:         24/11/27
"""
import pyinputplus as pyip
from pathlib import Path
from enum import Enum
import re





WHITESPACE_REGEX = re.compile(r"\s+")
RECORD_REGEX     = re.compile(r"^[\w\-@\.<>+]+\s+[\w\-@\.<>+]+(\s+[\w\-@\.<>+]+)?$")





class InvalidRecordException(BaseException):
	"""
	An exception that represents a read ov a bad record.
	"""
	
	offender:str
	
	def __init__(self, offender:str):
		super().__init__()
		self.offender = offender



class LoginStatus(Enum):
	ProcessFailure = 3
	WrongPassword  = 2
	Success        = 0
	NoUser         = 1





# [P]rocessing
def handle_insertion(database:dict[str, str], uname:str, email:str):
	for user in database:
		if uname.lower() == user.lower():
			print(f"A user with the username {user} already exists!\nDo you wish to update their email from {database[user][1]} to {email}?")
			ans:bool = pyip.inputYesNo("[y / N]", default="no", limit=1) == "yes"
			if ans:
				database[user][1] = email
			return
	
	database[uname] = email
	print(f"{uname} was registered with the email address {email}.")



# [P]rocessing
def handle_deletion(database:dict[str, str], uname:str):
	for user in database:
		if uname.lower() == user.lower():
			email = database.pop(user)
			print(f"{user} (with the email address {email}) has been removed.")
			break
	else:
		print(f"{uname} does not appear to be registered.")



# [O]utput
def print_database(database:dict[str, str]):
	lngst_name_len = 0
	for user in database:
		if len(user) > lngst_name_len:
			lngst_name_len = len(user)
	
	for user in database:
		print(f"\t{user:<{lngst_name_len}} : {database[user][0]}")



# [I]nput
def create_users(limit:int=0) -> dict[str, tuple[str, str|None]]:
	print("Add users with a particular email in the format [[username] [email-address] [password?], ...].")
	database = dict()
	commies  = list( filter(lambda s: len(s) > 0, input().strip().split(',')) )
	
	if limit > 0 and len(commies) > limit:
		print(f"Too many records passed!\nOnly the first {limit} users will be considered.")
		commies = commies[:limit]
	
	for commie in commies:
		commie = commie.strip()
		if not RECORD_REGEX.match(commie) is None:
			usri = re.sub(WHITESPACE_REGEX, ' ', commie).split()
			database[usri[0]] = (usri[1], hash_pass(usri[2]) if len(usri) > 2 else None)
		else:
			print("Your input did not match the required input-format.")
	
	return database



# [P]rocessing
def read_records(s:str) -> dict[str, tuple[str, str|None]]:
	database = dict()
	lines    = s.strip().splitlines()
	for line in lines:
		# CommIEs  =  Comma Interspersed Elements  😜
		commies = line.split(',')
		for commie in commies:
			commie = commie.strip()
			if not RECORD_REGEX.match(commie) is None:
				usri = re.sub(WHITESPACE_REGEX, ' ', commie).split()
				database[usri[0]] = (usri[1], usri[2] if len(usri) > 2 else None)
	
	return database



# [P]rocessing
def hash_pass(s:str) -> int:
	grade = sum( [abs( ord(c)-len(s) )*101 for c in s] )
	return abs((~grade * len(s) * 33) & ~(len(s) | 1))



# [P]rocessing
def try_login(database:dict[str, tuple[str, str|None]]) -> tuple[LoginStatus, str]:
	print("Enter the name ov the user you want to log in as and the password to try...")
	print("  [Note: If the account you are trying to log into has no password, type nothing.]")
	
	usrtxt = input().split(' ')
	if len(usrtxt) != 2:
		return (LoginStatus.ProcessFailure, None)
	usrtxt[0], usrtxt[1] = usrtxt[0].strip(), usrtxt[1].strip()
	
	for uname in database:
		if uname.lower() == usrtxt[0].lower():
			# For some reason, this function keeps falsely reporting that
			#  the incorrect password was used (for example, when I create)
			#  an account with the password "Test" and try to log into it.
			#
			# I'm not sure how the "hashes" are ending up different.
			# However, unfortunately, this bug prevents the log-in system
			#  from working.
			if database[uname][1] == hash_pass(usrtxt[1]) or (database[uname][1] is None and usrtxt[1] == ""):
				return (LoginStatus.Success, uname)
			else:
				return (LoginStatus.WrongPassword, uname)
	else:
		return (LoginStatus.NoUser, usrtxt[0])





# [M]ain
def main():
	print("Welcome to Totally Not Recycled User (+ Email) Database Application!\nType \"help\" for help.")
	
	logged_in_as:str|None = None
	path:Path             = Path("user_db.txt")
	dbf                   = None
	
	'''
	Erik:
	    Initialize a text file to store user information with at least one line--there should always be a user 
	    to view. That should happen in the program!
	
	-------------------------
	
	Calin:
	    I didn't know you wanted me to do it programmatically, I just
	     assumed that by "initialize" you, generally, meant "create", to
	     which I did provide an initial `user_db.txt` file.
	    
	    Anywho... I've added a way for a default user to create an account,
	     as well as a layer ov security for other users.
	'''
	if path.exists() and path.is_file():
		dbf = open(path, "r+")
	
	try:
		database = dict()
		if not dbf is None:
			database = read_records(dbf.read())
		else:
			# Yes.
			# This technically satisfies the criteria.
			#
			# You never said the file couldn't be initialized with data from user input.
			print("There do not seem to be any users registered...\n To continue, you will need to make an account.")
			ans = pyip.inputYesNo("Do you wish to proceed? ") == "yes"
			if ans:
				usri = create_users(1)
				dbf  = open(path, "w+")
				
				for uname, info in usri.items():
					database[uname] = info
					logged_in_as = uname
					dbf.write(f"{uname} {info[0]}{f' {info[1]}' if not info[1] is None else ''}")
			else:
				return
		
		while True:
			cmd = input("> ").strip()
			if len(cmd) < 1:
				continue
			
			match cmd:
				# Print (primitive) help menu.
				case "help" | '1':
					litxt = None
					if logged_in_as is None:
						litxt = "You are not logged in."
					else:
						litxt = f"You are logged in as: {logged_in_as}."
					print(f"{litxt}\n\n1. help\n2. add\n3. view\n4. del\n5. save\n6. switch\n7. exit")
				
				# Add a user.
				case "add" | '2':
					records = create_users()
					for user in records:
						handle_insertion(database, user, records[user])
				
				# View users.
				case "view" | '3':
					print_database(database)
				
				# Delete a user.
				case "del" | '4':
					print("[[ Pretend that account-deletion is password-protected. ]]")
					ntd = input("Enter the name ov the user to delete: ").strip()
					handle_deletion(database, ntd)
					if WHITESPACE_REGEX.search(ntd):
						print("[Note: Usernames do not contain whitespace.]")
				
				# Saves the database to a file.
				case "save" | '5':
					dbf.truncate(0)
					dbf.seek(0)
					for uname, info in database.items():
						dbf.write(f"{uname} {info[0]}")
						if not info[1] is None:
							dbf.write(f" {info[1]}")
						dbf.write(',')
					dbf.flush()
				
				# Switch the currently logged-in user.
				case "switch" | '6':
					attempt = try_login(database)
					
					match attempt:
						case (LoginStatus.ProcessFailure, _):
							print("Something went wrong...\n (Maybe the credentials were not formatted correctly?)")
						
						case (LoginStatus.WrongPassword, uname):
							print(f"You entered the incorrect password for {uname}.")
						
						case (LoginStatus.Success, uname):
							logged_in_as = uname
							print(f"You have successfully logged into the account {uname} <{database[uname][0]}>.")
						
						case (LoginStatus.NoUser, uname):
							print(f"There is no account with the username \"{uname}\".")
				
				# Exit the program.
				case "exit" | '7':
					dbf.close()
					exit(0)
	
	except KeyboardInterrupt:
		dbf.close()
		exit(0)

if __name__ == "__main__":
	main()

'''
Erik:
    Great job as always. Deleting and a separate save step were nice touches. 
'''