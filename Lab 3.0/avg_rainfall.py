"""
Description:  Displays the average amount ov rainfall for each and all
               years.
Author:       Calin "Katty" Baenen
Date:         24/10/21
Note:         `ui.py` is a required file to run this program, since it
               contains a commonuse function.
"""

from ui import get_yesno_input, get_int_input

'''
Erik: -0.5
    This needs to be broken out into the MIPO functions (main, input, processing, outputs). (Sorry.)

-------------------------

Calin:
    I can assure you, now, that all my functions meet MIPO requirements.
     `main` is,  ov course,  my [M]ain function, `sum` is a built-in
     function which acts as my [P]rocessing function, `print_rainfalldata`
     is my [O]utput function, and every function with "get" and "input",
     just about, are my [I]nput functions.
'''
# Define the months ov the year..
MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",  "november", "december"]





# [O]utput
def print_rainfalldata(*ytots):
	y = 1
	for tot in ytots:
		# Print the information for this year.
		print(f"Year #{y}'s rainfall total: {tot}")
		print(f"Year #{y}'s average rainfall: {tot/12:.2f}")
		print()
		
		# Increment the year.
		y += 1
	
	# Print the totaled values.
	print(f"Overall rainfall total: {sum(ytots)}")
	print(f"Overall average rainfall: {process(ytots):.2f}")



# [P]rocessing
def process(ytots):
	return sum(ytots) / (12*len(ytots))



# [I]nput
def get_rainfalldata(no_yrs) -> list[int]:
	tots = []
	
	# Get information for each year.
	y = 0
	while y < no_yrs:
		ytot = 0
		m    = 0
		
		# Get the rainfall data for each month.
		while m < 12:
			ytot += get_int_input(f"Enter rain for {MONTHS[m]}, yr {y+1}: ")
			m += 1
		
		# Add this year's total to the totals.
		tots.append(ytot)
		y += 1
	
	return tots




# [M]ain
def main():
	# Tell the user what the program will do.
	print("This program will show you the total and average rainfall over a specified period ov time.")
	times_run = 0
	
	while True:
		times_run += 1
		
		# Define key variables.
		phrase = "more"          # Technically not a key variable, but oh well.
		years  = get_int_input("How many years worth ov data do you have? ", 1)
		
		# Get the rainfall data for a given number ov years.
		print_rainfalldata(*get_rainfalldata(years))
		
		# (Re)Compute the phrase
		if times_run > 5 or years >= 10:
			phrase = "EVEN MORE"
		
		# Offer the user to print more rainfall data.
		if get_yesno_input(f"\nWould you like to calculate {phrase} rainfall data? "):
			print("[2J[u", end="")
			continue
		else:
			break
		
	'''
	Erik: -0.5
	    See the general requirements slides for the labs; starting with Chapter 3, unless the lab specifically exempts
	    the requirement, programs must offer to restart.
	
	-------------------------
	
	Calin:
	    Done! — I even gave you one ov them fancy screen clearin'
	     effects for readability!
	'''

# Call `main` if this is the file being run.
if __name__ == "__main__":
	main()