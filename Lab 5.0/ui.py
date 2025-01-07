from typing import Optional
from enum import Enum





class Command(Enum):
	"""
	Generic `Command` class.

	Represents one ov a few commands in both applications, hence the
	creation ov a common application interface.
	"""
	
	def __str__(self) -> str:
		return str(self.value)
	
	Delete = "del"
	Edit   = "edit"
	Exit   = "exit"
	Help   = "help"
	View   = "view"
	Add    = "add"





def get_nonempty(prompt:str="") -> str:
	"""
	Gets non-empty input from the user.
	"""
	
	while True:
		out = input(prompt).strip()
		if len(out) > 0:
			return out



def get_command() -> tuple[Command, list[str]]:
	"""
	Takes a string from a user, and tries to convert it to a command, along
	with a list ov additionally inpassed arguments.
	"""
	
	while True:
		cmdtxt:str = None
		
		try:
			# Get a refined version ov the user input which only has keywords entered.
			args = list(filter(lambda s: len(s.strip()) > 0, get_nonempty("> ").split()))
			
			# Set the command-text and remove the command from the arguments list.
			cmdtxt = args.pop(0)
			
			# Try and create a command from the command-text.
			cmd = Command(cmdtxt)
			
			# Return the command and arguments.
			return (cmd, args)
		
		# Catches a `ValueError`, which occurs from a bad cast from `str` to `Command`.
		except ValueError as e:
			# Reports to the user that their input was not valid.
			print(f"\"{cmdtxt}\" is not a recognized command.")
		
		# Catch all other errors.
		except Exception as e:
			print("An unexpected error occured:\n\t{}".format( str(e) ))



def get_yesno() -> Optional[bool]:
	ans = get_nonempty("[Y / N] ").lower()
	
	match ans:
		# Affirmative.
		case "yes" | 'y':
			return True
		# Negative.
		case "no" | 'n':
			return False
		# Other.
		case _:
			return None



def get_int(prompt:str="", min:Optional[int]=0, max:Optional[int]=None) -> int:
	"""
	Prompts the user for a strictly numeric input and does not stop until
	the user appropriately responds.
	"""
	
	out = None
	while True:
		try:
			out = int(input(prompt))
			if (not (min is None) and out < min) or (not (max is None) and out > max):
				raise ValueError
			break
		except ValueError:
			num_desc:str = None 
			
			match (min, max):
				# Minimum ov zero, no maximum.
				case (0, None):
					num_desc = "nonnegative, whole number"
				# Minimum ov one, no maximum.
				case (1, None):
					num_desc = "positive, whole number"
				# (Any) Minimum not equal to zero or one, no maximum.
				case (_, None):
					num_desc = f"whole number greater than or equal to {min}"
				# Maximum ov zero, no maximum.
				case (None, 0):
					num_desc = "nonpositive, whole number"
				# Maximum ov negative one, no minimum.
				case (None, -1):
					num_desc = "negative, whole number"
				# (Any) Maximum not equal to zero or one, no minimum.
				case (None, _):
					num_desc = f"whole number less than or equal to {max}"
				# Any number between, every other combination ov, the
				#  minimum and maximum values.
				case (_, _):
					num_desc = f"whole number between {min} and {max}"
			
			print(f"You must enter a {num_desc}. — Do not separate the digits with any character.")
	
	return out