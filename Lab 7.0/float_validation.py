"""
Description:  Checks to see if a float is valid using regex, reading it
               back to the user if it is.
Author:       Calin "Katty" Baenen
Date:         24/11/03
"""
import re





def main():
	print("Welcome to FloatValidator.\n(Press Ctrl+C to exit.)")
	
	FLOAT_REGEX = re.compile(r"^(\+|-)?[0-9]+(\.[0-9]+)?$")
	
	while True:
		print()
		print("Enter a number (optionally, with a decimal): ")
		'''
		Erik: -0.25
		    LOL. It took me a minute to figure out how your name validation was so broken. Turns out it's the float 
		    validation but asks for a name.
		'''
		txt = input("> ").strip()
		
		m = FLOAT_REGEX.match(txt)
		if m is not None:
			print(f"{m.group(0)} is a valid number!")
		else:
			print("This does not look like a valid number!")

if __name__ == "__main__":
	main()