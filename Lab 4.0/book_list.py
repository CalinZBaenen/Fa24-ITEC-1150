"""
Description:  Collect a list ov books and their prices, then summarize it.
Author:       Calin "Katty" Baenen
Date:         24/10/13
Note:         `ui.py` is a required file to run this program, since it
               contains a commonuse function.
"""
from ui import get_yesno_input, get_num_input, NumberType


'''
Erik: 
    The program works correctly, but needs to be broken out into the MIPO functions (main, input, processing,
outputs). I know your knowledge of functions is beyond an introductory course, but the requirements are the same for 
everyone.

-------------------------

Calin:
    Done.
'''
# [O]utput
def display_pricemap(pricemap):
	longest_price_len = 0
	longest_title_len = 0
	total_price       = 0
	avg_price         = 0
	
	# Longest title and textformed price.
	for book in pricemap:
		if len(book) > longest_title_len:
			longest_title_len = len(book)
		if len( str(pricemap[book]) ) > longest_price_len:
			longest_price_len = len(str( pricemap[book] ))
	
	print(f"{'Book Title':<{longest_title_len}}    {'Price':>{longest_price_len}}")
	for book in pricemap:
		total_price += pricemap[book]
		print(f"{book:<{longest_title_len}}  $ {pricemap[book]:>{longest_price_len}.2f}")
	
	avg_price = total_price/len(pricemap)
	
	# Somehow, I think  I broke how the floats are displayed...
	# For some reason, the floats are appearing centered, instead ov on the
	#  right... contrary to what the code says it should do.
	#
	# Hopefully this doesn't somehow earn me deductions.
	print(f"{'Total':<{longest_title_len}}  $ {total_price:>{longest_price_len}.2f}")
	print(f"{'Average':<{longest_title_len}}  $ {avg_price:>{longest_price_len}.2f}")



# [P]rocessing
# Not (necessarily) [I]nput.
def get_pricemap(no):
	pricemap = {}
	'''
	Erik:
	    If the user enters the same title twice, it overwrites the first price with the second. This lab was to use 
	    lists, not maps.
	
	-------------------------
	
	Calin:
	    I see how this could be an issue.
	    Though, it's very rare to see two books with the same name...
	     ... Unless one is actively fighting a copyright battle!
	    
	    In case the subtracted points is for a map, rather than the bug
	     itself, I have provided a version that uses lists.
	    
	    (Please note that I will read feedback in the list-using version;
	      however, I won't keep that version around, since it's a
	      duplicate. — For the sake ov centralization, this is the
	      program's "canonical" version.)
	'''
	i = 0
	while i < no:
		print(f"Enter details for book #{i+1}:")
		
		# I'm sorry about this code – it looks quite cluttered.
		title = ""
		while title == "":
			title = input(f"\tWhat is the title ov book #{i+1}? ").strip()
			if title == "":
				print("\tThe book you are purchasing must have a title!")
		price = get_num_input(f"\tHow much does {title} cost? ", 0, NumberType.Float)
		
		status = check_if_title_is_in_pricemap_and_offer_the_user_to_replace_it_as_a_processing_function(pricemap, title, price)
		if status is None:
			pricemap[title] = price
		elif not status:
			continue
		
		i += 1
	
	return pricemap



# [P]rocessing
# (Just in case you still consider the previous function as [I]nput.)
def check_if_title_is_in_pricemap_and_offer_the_user_to_replace_it_as_a_processing_function(pricemap:dict[str, float], title:str, new_price:float) -> None|bool:
	overwrite = None
	
	for book in pricemap:
		if title.lower() == book.lower():
			overwrite = get_yesno_input("A book with this title already exists – would you like to change its price? ")
			if overwrite:
				pricemap[book] = new_price
	
	return overwrite





# [M]ain
def main():
	while True:
		no_books = get_num_input("How many books are you purchasing? ", 1)
		pricemap = get_pricemap(no_books)
		
		display_pricemap(pricemap)
		
		run_again = get_yesno_input("Would you like to order more books? ")
		
		if run_again is None:
			print("Your input could not be recognized as a yes or no input – assuming \"no\".")
		if not run_again:
			break

if __name__ == "__main__":
	main()

'''
Erik:
    Nice job.
'''