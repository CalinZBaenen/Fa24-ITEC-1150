"""
Description:  Calculates some numbers with the help ov Python's inbuilt
                `math` library.
Author:       Calin "Katty" Baenen
Date:         24/09/14
"""

import math;
'''
Erik:
    The semicolon isn't used in Python :-)
'''

# Truncate the number to an integer.
num = 7.89
print( f"cut off {num} to {math.trunc(num)}" )

# Round the number to the nearest thousandths place.
num = 54.345395
print( f"round {num} to {round(num, 3)}" )

# Calculate the square root ov the number.
num = 2
print( f"calculate the square root ov {num} ({math.sqrt(num)})" )

# Calculate the sin ov the number.
num = 7
print( f"calculate the sin ov {num} ({math.sin(num)})" )

# Print Pi (π).
print( f"display the value of pi ({math.pi})" )

# Print Pi (π) rounded to the nearest thousandths place.
print( f"display pi rounded to 3 decimal places ({round(math.pi, 3)})" )

'''
Erik:
    Nice job.
'''