"""
Description:  Downloads a text file from a given URL and prints the
               content.
Author:       Calin "Katty" Baenen
Date:         24/11/25
"""
import pyinputplus as pyip
import requests
import re

from requests import ConnectionError





TEXT_URI_REGEX = re.compile(r"(.(csv|txt|md))?$")
ENTER_URL_MSG  = "Enter a URL to a text file on the internet to print."





def main() -> int:
	print("Welcome to the Text-Document Display Program.")
	
	print(ENTER_URL_MSG)
	while True:
		url = pyip.inputURL("> ", default="", limit=1)
		# If no URL is entered, provide a default value.
		if url == "":
			print("A valid URL was not provided – the robots.txt file for Calin Baenen's website will be used instead.")
			url = "https://calinzbaenen.github.io/robots.txt"
		# Start over if this isn't (likely) a text file.
		if TEXT_URI_REGEX.search(url) is None:
			print("Hmmm... this doesn't look like a text document...\n (Text documents usually end in .txt, like files.)")
			continue
		
		try:
			res = requests.get(url)
			
			match res.status_code:
				case 404:
					print("This text document does not seem to exist.")
				
				case 200:
					text = res.text
					pl   = max([len(s) for s in text.splitlines()])
					
					if len(text) > 0:
						print("Here is your text document:")
						print(f" ┌{'─'*pl}┐")
						for line in text.splitlines():
							print(f" │{line:<{pl}}│")
						print(f" └{'─'*pl}┘")
					else:
						print("The text document you referred to exists but is empty.")
				
				case status:
					print(f"There was a ({status}) error loading your text document.")
					return 2
			
			print("Would you like to display another text file?")
			ans = pyip.inputYesNo("[y / N] ", default="no", limit=1) == "yes"
			if ans:
				print("[2J[u", end="")
				print(ENTER_URL_MSG)
			else:
				return 0
		
		# Catch `ConnectionError`s.`
		except ConnectionError:
			print("There was a problem connecting to the provided website.")
			return 2
		
		# Catch other errors.
		except Exception as e:
			print(f"An unexpected error ({type(e)}) occured.")
			return 1
	
	return 0

if __name__ == "__main__":
	exit(main())

'''
Erik:
    Great work.
'''