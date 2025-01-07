"""
Description:  Prints details about a traveller's trip.
Author:       Calin "Katty" Baenen
Date:         24/09/14
"""

desc_col_width = 15
val_col_width  = 7

print("[Enter info here to see trip details.]")

miles   = float(input("How many miles was your trip? "))
gallons = float(input("How many gallons ov gas did you use? "))
price   = round(float(input("How much does a gallon ov gas cost? ")), 2)
  # Same thing as in `area.py` about the ordering ov variables.

mpg = miles/gallons

spent = round(price*gallons, 2)
mpg   = round(mpg, 2)

print(f"Here are some fun facts about your trip:\n{'MPG:':<{desc_col_width}} {mpg:>{val_col_width}.2f}\n{'Trip cost:':<{desc_col_width}}${spent:>{val_col_width}.2f}")

'''
Erik:
    Nicely done. I like how clear your input prompts are.
'''