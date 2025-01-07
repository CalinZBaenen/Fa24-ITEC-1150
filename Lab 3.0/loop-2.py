"""
Description:  Loop counter program #2.
Author:       Calin "Katty" Baenen
Date:         24/10/09
Note:         `ui.py` is a required file to run this program, since it
               contains a commonuse function.
"""

from ui import get_yesno_input, get_int_input



def print_range_and_sum(a=0, b=0):
	print('(', end="")
	
	# Print the range and sum the numbers.
	res = 0
	while a <= b:
		print(f"\t{a},")
		res += a
		b += 1
	
	# Print the sum.
	print(f"Sum: {res})")

'''
Erik: -0.5
    This needs to be broken out into the MIPO functions (main, input, processing, outputs).
    You obviously know how to use functions, but I have to have some consistency with my grading (yes, "A foolish 
    consistency is the hobgoblin of little minds...", but it's more the expectation of others than my own need for 
    consistency :-) )

-------------------------

Calin:
    > This needs to be broken out into the MIPO functions (main, input, processing, outputs).
    
    I thought I had (enough). — Hopefully making the `print_range_and_sum`
     function was solution!
'''
def main():
	# Greet the user and explain the program.
	print("Welcome!\nThis program lists the numbers in a range, then adds them up.\n")
	
	while True:
		# Get the big and small numbers.
		small = get_int_input("Enter number A (smaller): ", None)
		big   = get_int_input("Enter number B (bigger): ", small)
		
		# Print the range and sum.
		print_range_and_sum(small, big)
		
		# Offer the user to print another range.
		if not get_yesno_input("Would you like to print another range? "):
			break
		
	'''
	Erik: -0.5
	    See the general requirements slides for the labs; starting with Chapter 3, unless the lab specifically exempts
	    the requirement, programs must offer to restart.
	
	-------------------------
	
	Calin:
	    Did I do it correctly?
	    I assume what you meant by "offer to restart" is "allow the user to
	     use the functionality ov the program without opening it again".
	'''

if __name__ == "__main__":
	main()

'''
Erik:
    This is obviously really well-written, but make sure to hit the requirements before jumping into the fun stuff!
'''