"""
Description:  Gets a list ov positive feedback phrases, separated by '!'.
Author:       Calin "Katty" Baenen
Date:         24/10/28
Note:         `ui.py` is a required file to run this program, since it
               contains common program components.
"""
from ui import *

from typing import Optional
import re





END_OF_PHRASE = re.compile(r"\b\s+(!|$)")
WHITESPACE    = re.compile(r"\s+")





# [P]rocessing
def extract_phrases(s:str) -> Optional[list[str]]:
	phrases = []
	phrase  = ""
	
	# Search the string for different characters.
	i = 0
	for c in s:
		match c:
			case '!' if len(phrase) > 0:
				phrase = END_OF_PHRASE.sub("", WHITESPACE.sub(' ', phrase)).capitalize()+'!'
				phrases.append(phrase)
				phrase = ""
			
			case _ if c.isspace():
				if len(phrase) > 0:
					phrase += ' '
			
			case _:
				phrase += c
		
		i += 1
	
	# Ask the user whether or not they meant to put an exclamationpoint
	#  after the phrase they entered.
	if len(phrases) < 1 and len(phrase) > 0:
		new_phrase = END_OF_PHRASE.sub("", phrase).capitalize()+'!'
		
		print(f"It seems like you wrote \"{phrase}\"; however, phrases must end in an exclamationpoint, '!'.")
		print(f"Did you mean \"{new_phrase}\"?")
		
		ans = get_yesno()
		if ans is None:
			print("Answer was not a yes-or-no answer – assuming \"no\".")
			ans = False
		
		if ans:
			phrases.append(new_phrase)
		else:
			return None
	
	# Return the phrases.
	return phrases



# [O]utput
pno = 0
def print_phrases(phrases:list[str]):
	global pno
	
	print("These are the phrases you provided:")
	for phrase in phrases:
		pno += 1
		print(f"{pno}: {phrase}")





# [M]ain
def main():
	print("Welcome to Feedback Collector!")
	print("Please enter one or more phrases that end in exclamation points!")
	
	while True:
		phrases = extract_phrases( get_nonempty("> ") )
		if phrases is None:
			continue
		
		print_phrases(phrases)
		
		print("Would you like to submit more responses?")
		ra = get_yesno()
		if ra is None or not ra:
			break
		print("Please enter more phrases:")

if __name__ == "__main__":
	main()

'''
Erik:
    Outstanding!
'''