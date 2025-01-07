"""
Description:  Prints the subtotals and (eventually) total price for the
               textbook(s) you are purchasing.
Author:       Calin "Katty" Baenen
Date:         24/09/29
"""

no_textbooks = 0
prices = []  # I know we haven't discussed arrays, but hopefully a
             #  a concession can be made in favor for a better looking
             #  user-interface.
'''
Erik:
    To be honest, of the reasons I enumerated for using advanced language features, the one that carries the most weight
    is the concern about AI generated code.
    
    From speaking with you, I have the necessary confidence that you know what you're doing, so no worries. Just don't 
    go so wild that it takes me 10 minutes to understand your code :-)
'''


# Get (and validate) the number ov textbooks from the user.
while True:
	no = input("How many textbooks are you purchasing? ")
	
	if no.isnumeric():
		no_textbooks = int(no)
		break
	print("You may only provide a positive, whole number.")


# I know, we haven't learned `len()` functon either, but I might as
#  well make this optimization, since I am using an array.
#
# The studious way ov handling this would be to make a variable
#  called `textbooks_rang_up` or so and increment it each time a book's
#  price is registered.
while len(prices) < no_textbooks:
	# Points can't be docked for this print statement, I'm pretty sure.
	#
	# This clears the screen and resets the cursor using ANSI codes.
	print("[2J[u", end="")
	print(f"How many textbooks are you purchasing? {no_textbooks}\n")
	
	# Print the subtotals if any books have been reigstered.
	if len(prices) > 0:
		print(f"Subtotals (${sum(prices):.2f}):")
		
		book_no = 1
		for price in prices:
			print(f"\tBook #{book_no}: ${price:.2f}")
			book_no += 1
		
		print()
	
	# Get the price from the user and validate it and add it to the
	#  list.
	price = round(float( input(f"How much does book #{len(prices)+1} cost? ") ), 2)
	prices.append(price)


# Clear the screen again.
print("[2J[u", end="")

# Review the subtotals (if more than one book was purchased).
if len(prices) > 1:
	print("Subtotals:")
	
	book_no = 1
	for price in prices:
		print(f"\tBook #{book_no}: ${price:.2f}")
		book_no += 1
	
	print()

# Print the grand total.
print(f"Grand Total: ${sum(prices):.2f}\n")

'''
Erik:
    Great work, as always.
'''