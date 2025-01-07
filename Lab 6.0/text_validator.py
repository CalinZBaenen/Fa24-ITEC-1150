"""
Description:  (Correctly) Capitalizes a title.
Author:       Calin "Katty" Baenen
Date:         24/10/28
Note:         `ui.py` is a required file to run this program, since it
               contains common program components.
"""
from ui import *

import re





# "The", "A", and "An" can stay capitlized, since they are connected to
#  a noun which is capitalized, so leaving it lowercase is nonsensical.
'''
Erik:
    You'd be amazed how often seemingly nonsensical requirements turn out to have a good reason behind them. (And, 
    unfortunately, how often nonsensical requirements are just something you have to live with because a user wants 
    them.)
'''
#
# Other than that, the words choaen come from knowledge, plus a list
#  provided by
#  https://prowritingaid.com/list-of-words-not-capitalized-in-titles.
#
# Some words have been filtered for preference.
CAPITALIZATION_EXCEPTIONS = re.compile(r"\b(and|as|at|but|by|for|from|if|in|into|near|nor|o(f|v)|or|so|than|to|upon|with|yet)\b", re.IGNORECASE)
WHITESPACE                = re.compile(r"\s+")





# [O]utput.
def show_corrected_title(title:str):
	print(f"The corrected title is: {title}")



# [P]rocessing
def title_caps(s:str) -> str:
	s = WHITESPACE.sub(' ', s.lower())
	
	words = s.split()
	i     = 0
	
	for word in words:
		if (CAPITALIZATION_EXCEPTIONS.match(word) is None) or i == 0:
			words[i] = word.capitalize()
		i += 1
	
	return ' '.join(words)





# [M]ain
def main():
	print("[2J[u", end="")
	print("Welcome to Title Capitalization Program 24!")
	
	while True:
		print("Enter the title to capitalize!")
		show_corrected_title( title_caps(get_nonempty("> ")) )
		print("Would you like to validate another title?")
		
		ans = get_yesno()
		if ans is None:
			print("Could not tell if you meant \"yes\" or \"no\".")
			ans = False
		if not ans:
			break
		
		print("[2J[u", end="")

if __name__ == "__main__":
	main()

'''
Erik:
    Great work.
'''