from typing import Union
from enum   import Enum

class NumberType(Enum):
	Float = 'f'
	Int   = 'i'



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
		return None

# Get (strictly numeric) input from the user, and persists multiple fails.
#
# I've made a breaking change by renaming the function.
# In a typically library, only the parameter would be added, or an entirely
#  new function would be created specifically for floats.
# However, I wanted to save myself from rewriting code, hence the
#  `NumberType` enum, to signal to this function whether to get an
#  int or a float.
def get_num_input(prompt:str="", min:int=0, ty:NumberType=NumberType.Int) -> Union[int, float]:
	"""
	Prompts the user for a strictly numeric input and does not stop until
	the user appropriately responds.
	"""
	
	out = None
	while True:
		try:
			txt = input(prompt)
			match ty:
				case NumberType.Float:
					out = float(txt)
				case NumberType.Int:
					out = int(txt)
			
			if not (min is None) and out < min:
				'''
				Erik:
				    I would recommend defaulting min to None in the params so that a user of this method wouldn't 
				    have a min value unless they specifically requested one. Obviously it's your method and you can 
				    do what you like, but if you were sharing this, it would probably surprise people that the 
				    default was 0 and they had to override with None to allow any int.
				
				-------------------------
				
				Calin:
				    This would make the most sense if this were a
				     public-facing library;  however, if this were code
				     developed for a particular application or codebase –
				     which is a lot closer to the scenario ov us making
				     code for you – a developer would design a function
				     around the most common scenario — furthermore, having
				     no minimum is the LEAST common scenario.
				    
				    Sans the fact there is no documentation stating this,
				     do you think I make a good argument for why I chose
				     the default value that I did?
				'''
				raise ValueError
			break
		except ValueError:
			num_desc = ""
			sign     = ""
			
			if min == 1:
				sign = "positive"
			elif min == 0:
				sign = "nonnegative"
			
			num_desc += f"{sign}"
			if ty == NumberType.Int:
				# Add comma and space if the wordform ov the sign appears.
				if sign != "":
					num_desc += ", "
				
				# Adds the word whole if only integers are accepted.
				num_desc += "whole "
			elif sign != "":
				num_desc += ' '
			# Add the word "number" to the description.
			num_desc += "number"
			# Add the minimum to the description if it's more complex than
			#  nonnegative or positive.
			if sign == "":
				num_desc += f" greater than or equal to {min}"
			
			print(f"You must enter a {num_desc}.")
	
	return out