"""
Description:  A, helpful, program which shows you the result of mixing two colors.
Author:       Calin "Katty" Baenen
Date:         24/09/19
"""

errored = False
result  = ""
c1_set  = False
c1      = ""
c2      = ""

print("Welcome to Katty's Color-Mixer!\nType \"colors\" to list the available colors.")

# I'm unsure if `.lower()` was went over, though – to my knowledge – this
#  (making the case consistent*) the only way to process case-insensitive
#  user-input.
# In the video, you mentioned using all lowercase for your comparisons,
#  but you don't mention that the mismatching case can cause bugs
#  (even if it is common-sense to the both ov us).
#
# Unrelated, but I've been meaning to find time to meet you; I wanted to
#  join your Zoom meeting this past week, but I was (and I have been)
#  very tired after school, due to an unfortunate placement ov classes.
'''
Erik:
    Hmmm. I thought I mentioned the reason for keeping things lowercase for now. That's kind of a no-brainer to explain.
    
    If you ever want to meet at some other time, just let me know.
'''
cmd = input("Color A: ").lower()

# Prints the available colors.
if cmd == "colors":
	print("(Letters enclosed in brackets denote a shorthand-code for each color.)")
	print("[Y]ellow")
	print("[Bl]ack")
	print("[G]reen")
	print("[B]lue")
	print("[R]ed")

# Checks to see if the "command" is a color, if so, treat it as though
else:
	c1_set = True
	c1 = cmd

# Because we have not covered `exit()`, I have to use a codeblock which
#  runs when there is not an error.
if not errored:
	if not c1_set:
		c1 = input("Color A: ").lower()
	
	# Convert color A shorthand-codes to longhand names.
	if c1 == 'y':
		c1 = "yellow"
	elif c1 == "bl":
		c1 = "black"
	elif c1 == 'g':
		c1 = "green"
	elif c1 == 'b':
		c1 = "blue"
	elif c1 == 'r':
		c1 = "red"
	
	# Get the value ov color B, then do a similar conversion.
	c2 = input("Color B: ").lower()
	if c2 == 'y':
		c2 = "yellow"
	elif c2 == "bl":
		c2 = "black"
	elif c2 == 'g':
		c2 = "green"
	elif c2 == 'b':
		c2 = "blue"
	elif c2 == 'r':
		c2 = "red"
	
	# Test if color A is a valid color.
	if not (
		c1 == "yellow" or
		c1 == "black"  or
		c1 == "green"  or
		c1 == "blue"   or
		c1 == "red"
	):
		if c1 == "":
			print(f"Error: Color A's value is not set")
		else:
			print(f"Error: Color A, \"{c1}\", is not a recognized color")
		errored = True
	# Test if color B is a valid color.
	if not (
		c2 == "yellow" or
		c2 == "black"  or
		c2 == "green"  or
		c2 == "blue"   or
		c2 == "red"
	):
		if c1 == "":
			print(f"Error: Color B's value is not set")
		else:
			print(f"Error: Color B, \"{c2}\", is not a recognized color")
		errored = True
	
	# Test if the colors are unique.
	if not errored and c1 == c2:
		print(f"Error: Color A (\"{c1}\") and color B (\"{c2}\") are identical")
		errored = True
	
	# If there is no error, continue.
	# (If only you could `break` from `if`-statements like `for`-loops.)
	if not errored:
		# I wish I could use `match`.
		# This code is just as bad as, if not worse than, YandereDev's code.
		if (c1 == "yellow" and c2 == "black") or (c1 == "black" and c2 == "yellow"):
			result = "darkyellow"
		elif (c1 == "yellow" and c2 == "green") or (c1 == "green" and c2 == "yellow"):
			result = "chartreuse"
		elif (c1 == "yellow" and c2 == "blue") or (c1 == "blue" and c2 == "yellow"):
			result = "green"
		elif (c1 == "yellow" and c2 == "red") or (c1 == "red" and c2 == "yellow"):
			result = "orange"
		elif (c1 == "black" and c2 == "green") or (c1 == "green" and c2 == "black"):
			result = "darkgreen"
		elif (c1 == "black" and c2 == "blue") or (c1 == "blue" and c2 == "black"):
			result = "darkblue"
		elif (c1 == "black" and c2 == "red") or (c1 == "red" and c2 == "black"):
			result = "darkred"
		elif (c1 == "green" and c2 == "blue") or (c1 == "blue" and c2 == "green"):
			result = "junglegreen"
		elif (c1 == "blue" and c2 == "red") or (c1 == "red" and c2 == "blue"):
			result = "purple"
		
		print(f"Result: {c1} + {c2} = {result}")

'''
Erik:
    Totally over the top, but great work :-)
'''