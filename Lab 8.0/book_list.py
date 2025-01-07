"""
Description:  Collect a list ov books and their prices, then summarize it.
Author:       Calin "Katty" Baenen
Date:         24/11/25
Note:         You will need to make sure you have the PyInputPlus library
               installed on your machine.
"""
import pyinputplus as pyip
import re





FIRST_CHAR_REGEX = re.compile(r"\b[A-Z]", re.IGNORECASE)





def capitalize_precise(s:str) -> str:
	"""
	Capitalizes the first character ov a string, similar to
	`str.capitalize()`; however, non-word-characters are not included, so
	they may precede the first letter, while still allowing it to be
	capitalized.
	"""
	
	try:
		builder = list(s.lower())
		
		# Get the index ov the string's first (word) characters.
		for fch in FIRST_CHAR_REGEX.finditer(s):
			builder[fch.start()] = builder[fch.start()].capitalize()
		
		# Replaces the first (word) character with a capital
		s = "".join(builder)
	except:
		pass
	
	return s



# [O]utput
def display_pricemap(pm:dict[str, float]):
	BOOK_COL_LABEL = "Book Title"
	
	longest_price_len = 5
	longest_title_len = len(BOOK_COL_LABEL)
	total_price       = 0
	avg_price         = 0
	
	# Longest title and textformed price.
	for book in pm:
		if len(book) > longest_title_len:
			longest_title_len = len(book)
		if len( str(pm[book]) ) > longest_price_len:
			longest_price_len = len(f"{longest_price_len:>5.2f}")
	
	print(f"{BOOK_COL_LABEL:^{longest_title_len}}    {'Price':^{longest_price_len}}")
	for book in pm:
		total_price += pm[book]
		print(f"{capitalize_precise(book):<{longest_title_len}}  $ {pm[book]:>{longest_price_len}.2f}")
	
	avg_price = total_price/len(pm)
	
	# Now the columns are smashed together... whereas last time the money
	#  was centered.
	# ... What am I doing wrong?
	print(f"{'Total':<{longest_title_len}}  $ {total_price:>{longest_price_len}.2f}")
	print(f"{'Average':<{longest_title_len}}  $ {avg_price:>{longest_price_len}.2f}")
	'''
	Erik:
	     Decimal points need to be aligned and titles need to be title case.
	     The decimal formatting is off because the longest_price_len calculation doesn't take the decimal places into 
	     consideration; you need to get the length of the formatted price for that to work.
	        Book Title        Price
	        java jumpstart  $  0.00
	        clojure codex   $ 101.00
	        Total           $ 101.00
	        Average         $ 50.50
	
	-------------------------
	
	Calin:
	    Hopefully this formatting works good enough.
	    I can't believe something this simple was slipping my mind.
    
	-------------------------
	Erik:
	    Well, the total is causing misalignment because it's larger than the other values, but I'll let that slide since
	    you went above and beyond. 
	    
	    It didn't occur to me until a moment ago that you could've skipped finding the longest price and just used the 
	    length of the total, since that will always be the >= the length of any individual price.
	'''



# [I]nput
def get_pricemap(no:int) -> dict[str, float]:
	"""
	Uses PyInputPlus functions to get a selection ov booktitles and prices.
	"""
	pm = dict()
	i  = 0
	while i < no:
		print(f"Enter details for book #{i+1}:")
		
		title = input(f"\tWhat is the title ov book #{i+1}? ").strip().lower()
		# I can't believe I only thought ov this better solution just now!
		# ... Much less cluttered.
		if len(title) < 1:
			print("\tThe book you are purchasing must have a title!")
			continue
		price = pyip.inputFloat(f"\tHow much does {capitalize_precise(title)} cost? ", min=1, max=100)
		'''
		Erik:
		    Restrict individual book prices to $1.00 minimum and $100.00 maximum
		
		-------------------------
		
		Calin:
		    Oops.
		    I saw that in the requirements but totally overlooked its implementation.
		
		-------------------------
		Erik:
		    I recently spent several hours fixing a job that was failing because of some edge cases with a particular 
		    field.
		    
		    It was pointed out to me today that the field that was causing the problems didn't even need to be included.
		    So it goes.
		'''
		
		# Check if the title is in the map, and prompt the user for whether
		#  or not they want to change its price if so.
		if title in pm:
			replace = pyip.inputYesNo("A book with this title already exists – would you like to change its price? ") == "yes"
			if not replace:
				continue
		
		# Set the price ov the book and advance the loop.
		pm[title] = price
		i += 1
	
	return pm





# [M]ain
def main():
	while True:
		# Get the number ov books to buy, then the pricemap for it.
		no_books = pyip.inputInt("How many books are you purchasing? ", min=1)
		pricemap = get_pricemap(no_books)
		
		display_pricemap(pricemap)
		
		# Ask the user if they want to get more books.
		run_again = pyip.inputYesNo("Would you like to order more books? ")
		if not run_again == "yes":
			if run_again is None:
				print("Your input could not be recognized as a yes or no input – assuming \"no\".")
			break

if __name__ == "__main__":
	main()

'''
Erik:
    If only there were a way to put an animated gif in place of the 'under construction' banner so it would look like a 
    1990's website... 
'''