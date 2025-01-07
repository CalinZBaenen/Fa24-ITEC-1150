"""
Description:  Prints the area ov a rectangle in a given unit ov
               measurement.
Author:       Calin "Katty" Baenen
Date:         24/09/14
"""

# This file, despite being misleadingly named, canonically comes after
#  `area_but_better.py`.
#
# I hope it is acceptable that  I kept the old file as well, since I am
#  providing this version, which does meet your criteria.

print("Welcome to Rectangle Area Calculator!")

unit = input("Which unit (e.g: in, ft, cm, et cetera) do you wish to measure in? ")

# We technically haven't used `if`-blocks yet, but surely this is safe,
#  right?
#
# (
#   I'm worried now because you are going to start deducting points for
#    using features we haven't went over yet.  😟
# )
if unit == "in":
	unit = "inches"
if unit == "ft":
	unit = "feet"
if unit == "cm":
	unit = "centimeters"
if unit == 'm':
	unit = "meters"
'''
Erik:
    See my comments in your other submission for this lab section. No deductions :-)
    
    I know you're having fun with this, so I want you to know the following comments are for discussion and thought, 
    and are not a criticism of your work!
    I'll mention from a software engineering perspective, adding features/constraints that haven't been asked for is
    generally a bad practice.
    - Obviously, it can take time that should be spent on other, more important work.
    - Much less obviously, you can paint yourself into a corner when you later get requirements that conflict with what
        you assumed. The first point can waste x amount of time, but when you have to then re-write that code, you can 
        end up with 2x or more time invested.
    Writing solid code that meets requirements and delaying decision on a design of other features until you actually 
    have to make a decision gives you the best opportunity to get the most done with the least re-work. It's far more
    enjoyable to extend and add new things to your codebase than it is to have to fix bugs and clean up bad decisions 
    from weeks, months, or years ago. (This is knowledge hard-won and painfully endured.)
    
    Search for "YAGNI" if you want to read other people talking about this, and grab time with me if you want to discuss
    more.
'''
#     (... Even if points are deducted for the `if`s, at least it's easy to patach out)     

width  = float(input(f"What is the width ov the rectangle in {unit}? "))
height = float(input(f"What is the height ov the rectangle in {unit}? "))
  # Like I mentioned in the original version ov this program, I hate how
  #  I'm forced to put `width` before `height`, since I like sorting
  #  variables lengthwise and alphanumerically.

# Calculate the area.
area = width*height

# Print the rounded and formatted number.
print(f"Your rectangle is {round(area, 2):.2f} square {unit}.")

'''
Erik:
    Obviously, nice work.
'''