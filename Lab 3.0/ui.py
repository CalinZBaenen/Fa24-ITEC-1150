# I added typing for the hell ov it; sorry if that makes it harder to read.


# Get affirmative or negative input and return it as a boolean.
def get_yesno_input(prompt:str="") -> bool:
	"""
	Prompts the user for a yes/no or true/false input.
	"""
	
	while True:
		ans = input(prompt).lower()
		if (ans == 'y' or ans == "yes" or ans == "true"):
			return True
		if (ans == 'n' or ans == "no" or ans == "false"):
			return False
		
		print("Your input could not be recognized as affirmative (yes) or negative (no).")
		return False

# Get (strictly numeric) input from the user, and persists multiple fails.
def get_int_input(prompt:str="", min:int=0) -> int:
	"""
	Prompts the user for a strictly numeric input and does not stop until
	the user appropriately responds.
	"""
	
	out = None
	while True:
		try:
			out = int(input(prompt))
			if not (min is None) and out < min:
				'''
				Erik:
				    I would recommend defaulting min to None in the params so that a user of this method wouldn't 
				    have a min value unless they specifically requested one. Obviously it's your method and you can 
				    do what you like, but if you were sharing this, it would probably surprise people that the 
				    default was 0 and they had to override with None to allow any int.
				'''
				raise ValueError
			break
		except ValueError:
			num_desc = "nonnegative, whole number"
			if min == 1:
				num_desc = "positive, whole number"
			elif min != 0:
				num_desc = f"whole number greater than {min}"
			print(f"You must enter a {num_desc}. — Do not separate the digits with any character.")
	
	return out