"""
Description:  Loop counter program #2.
Author:       Calin "Katty" Baenen
Date:         24/09/29
"""

# -------------------------
# There might be a better way to write this program, and I would probably
#  write it differently myself if I thought it through harder.
# -------------------------

print("Welcome!\nThis program lists the numbers in a range, then adds them up.\n")

# Define X and Y.
x = None  # I know we haven't discussed `None`;  however, unlike in
          #  languages like Java or Rust, I can't declare a variable;s
          #  existence without a value. — Python uses `None` to
          #  represent a value that has not been defined yet.
y = None
'''
Erik:
    I briefly introduce None this week, but don't get into it in depth. Some people will get it and some people 
    aren't quite ready for it.
'''


# Get the smaller number.
while True:
	small = input("Enter number A (smaller): ")
	if small.isnumeric():
		x = int(small)
		break
	print("Only positive, whole, numeric input is accepted.")


# Get the bigger number.
while True:
	big = input("Enter number B (bigger): ")
	
	if big.isnumeric():
		'''
		Erik: -0.25
		    I assume this is just a typo or a copy/paste error, but the cast to int below fails if big isn't numeric.
		
		-------------------------
		
		Calin:
		    Yes, it was a copy-and-paste error.
		    This is a rookie mistake for someone like me – ack!
		'''
		
		'''
		Erik:
		    Happens to all of us :-)
		'''
		y = int(big)
		
		# Validate that the bigger number is actually bigger.
		if y > x:
			break
		else:
			print(f"Number B must be larger than number A ({x}).")
	else:
		print("Only positive, whole, numeric input is accepted.")


# Print the numbers from A to B (inclusive).
res = 0
n   = x

print("Numbers in range: ")
while n <= y:
	print(f"\t{n}")
	res += n
	n += 1
print(f"\nSum: {res}")

'''
Erik:
    Nicely done.
'''