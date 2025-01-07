"""
Description:  Displays the average amount ov rainfall for each and all
               years.
Author:       Calin "Katty" Baenen
Date:         24/09/29
"""

# Variables.
months = [
	"january",   "february", "march",    "april",
	"may",       "june",     "july",     "august",
	"september", "october",  "november", "december"
]
years = 0
tots = []

# Greet the user.
print("This program will show you the total and average rainfall over a specified period ov time.")


# Get the number ov years.
while True:
	txt = input("How many years worth ov data do you have? ")
	if txt.isnumeric() and int(txt) > 0:
		years = int(txt)
		break
	else:
		print("You must enter a positive, whole number.")


# Loop through the number ov years.
y = 0
while y < years:
	ytot = 0
	m    = 0
	
	# Get the rainfall data for each month.
	while m < 12:
		txt = input(f"Enter rain for {months[m]}, yr {y+1}: ")
		if txt.isnumeric():
			ytot += int(txt)
			m += 1
		else:
			print("You must enter a nonnegative (whole) number.")
	
	# Print the information for this year.
	print(f"Year #{y+1}'s rainfall total: {ytot}")
	print(f"Year #{y+1}'s average rainfall: {ytot/12:.2f}")
	print()
	
	# Add this year's total to the totals.
	tots.append(ytot)
	y += 1


# Print the final values.
print(f"Overall rainfall total: {sum(tots)}")
print(f"Overall average rainfall: {sum(tots) / (12*years):.2f}")

'''
Erik:
    Nice.
'''