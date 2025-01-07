"""
Description:  Loop counter program #1.
Author:       Calin "Katty" Baenen
Date:         24/09/29
"""

x = 0


# Loop 1: Count from zero to five.
print("Here are the numbers from zero to five:")
while x <= 5:
	print(f"\t{x}")
	x += 1

print()


# Loop 2: Count from one to twenty.
x = 1
print("Here are the numbers from one to twenty:")
while x <= 20:
	print(f"\t{x}")
	x += 1

print()


# Loop 3: Count by twos from zero to twentyfour.
x = 0
print("Here are the even numbers from zero to twentyfour:")
while x <= 24:
	print(f"\t{x}")
	x += 2

print()


# Loop 4: Count by twos from thirtyseven to fiftythree.
x = 37
print("Here are the odd numbers from thirtyseven to fiftythree:")
while x <= 53:
	print(f"\t{x}")
	x += 2

print()


# Loop 5:
x = 10
print("Here are the multiple ov ten, up to sixty, starting at ten:")
while x <= 60:
	print(f"\t{x}")
	x += 10

print()


# Loop 6:
x = 30
print("Here are the numbers from twenty to thirty backwards:")
while x >= 20:
	print(f"\t{x}")
	x -= 1

print()

'''
Erik:
    Ha. This is intended as practice with range, but no matter :-)
'''