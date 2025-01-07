"""
Description:  A program that reports to the user how much money their
                pennies are worth.
Author:       Calin "Katty" Baenen
Date:         24/09/10
"""

pennies = input("How many pennies do you have? ")

if pennies.isnumeric():
	balance = int(pennies)/100
	
	if balance > 1:
		print("Wow!\nYou have over a dollar in pennies!")
	elif balance == 1:
		print("You have exactly one dollar's worth ov pennies!")
	elif balance > 0:
		print("You have less than a dollar in pennies.")
	else:
		print("You have no pennies?!\nBummer...")
	print("-------------------------")
	print(f"In total, you have ${balance:.2f} worth ov pennies.")
else:
	print("The program failed because your input was a not a positive, whole number.")

'''
Erik:
    Really nice.
'''