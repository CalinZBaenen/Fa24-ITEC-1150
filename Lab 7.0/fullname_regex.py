"""
Description:  Checks to see if a name is valid (using a regex),
               capitalizing it properly if so.
Author:       Calin "Katty" Baenen
Date:         24/11/03
"""
import re





FIRST_CHAR_REGEX = re.compile(r"\b[A-Z]", re.IGNORECASE)





def name_caps(s:str) -> str:
	builder = list(s)
	
	i = 0
	while (m := FIRST_CHAR_REGEX.search(s, i)) is not None:
		fch = m.start()
		builder[fch] = builder[fch].capitalize()
		i = m.end()
	s = "".join(builder)
	
	return s





def main():
	print("Welcome to NameReader.\n(Press Ctrl+C to exit.)")
	
	# This will not work for letters which use additional markings to
	#  distinguish themselves from others (such as Å, Ä, and Ö in Swedish).
	FULLNAME_REGEX = re.compile(r"^([A-Z]+')?[A-Z]+\s+([A-Z]+|[A-Z]\.?)\s+[A-Z]+$", re.IGNORECASE)
	
	while True:
		print()
		print("Enter a name in the format `[first] [M | middle] [last]`:")
		txt = input("> ").strip()
		
		m = FULLNAME_REGEX.match(txt)
		if not m is None:
			print(f"Here is the name: {name_caps(m.group(0))}")
		else:
			print("That does not look like a threepart name!")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print()

'''
Erik:
    Great work.
'''