"""
Description:  Prints the area ov a rectangle in a given unit ov measurement
               but in a way that is 'safer' and more realistic.
Author:       Calin "Katty" Baenen
Date:         24/09/14
"""

# I made all this before I heard about the point deduction(s) for using
#  features we haven't went over.
#
# I'm a bit disappointed about it.

'''
Erik:
    I appreciate how much you clearly enjoy doing this, and am sorry to disappoint you by pushing back against more 
    advanced language features. Please let me explain a couple of the reasons.
    
    The most prominent one is that in many cases (although clearly not in yours), it's a strong indication that someone
    is using an LLM to generate code for the class rather than attempting to learn. Restricting language features makes
    using LLMs more difficult than writing code manually (or at least requires enough knowledge to simplify the
    generated code, and demonstration of knowledge is the purpose of graded assignments).
    
    The other major factor is that the more complex the program, the more time is required to understand and assess.
    Class sizes are progressively smaller as the concepts become more complex, in part due to that reality. I would 
    actually love to receive assignment submissions like this one that went above and beyond, but have to recognize that
    if this were more common, I would have no chance of getting timely feedback to everyone.
'''

##################################################
#                                                #
#            Rectange Area Calculator            #
#        A program that calculates the           #
#         area ov a rectangle, with a            #
#         specified unit ov measurement          #
#                                                #
#         (50 char * 9 char = 450 char)          #
#                                                #
#           Professional-Grade Program           #
#                                                #
##################################################
from enum import Enum;





###########################################################################
#                                                                         #
#     Like with the last assignment, classes are a feature we have        #
#      not yet learned – not only, but I am making use ov something       #
#      known as an enum.                                                  #
#                                                                         #
#     In the real world, instead ov storing a string like "cm" or         #
#      such, you would use an enum, which allows you to represent one     #
#      ov many possible, yet finite, states.                              #
#                                                                         #
#     Yes, I will continue to leave explanations/justifications for       #
#      things I use that have not yet been discussed in the course.       #
#                                                                         #
###########################################################################

"""
The `Unit` enum represents a unit ov measurement.
"""
class Unit(Enum):
	CENTIMETERS = "cm"
	KILOMETERS  = "km"
	INCHES      = "in"
	METERS      = 'm'
	FEET        = "ft"
	
	# Hidden, optional, `plural` option so that "foot" can change to "feet"
	#  when it makes sense.
	def __str__(self, plural=False):
		# This is a `match` statement, which does pattern-matching,
		#  something which has not yet been discussed in the course.
		#
		# Pattern matching,  `match`-`case`,  is similar to
		#  `switch`-`case` in the C-like languages, except it can
		#  capture values that you are not certain ov at
		#  "program-writing time".
		#
		# This is one ov my favorite features in the Rust programming
		#  languages, as it is immensely powerful there.
		match self:
			case Unit.CENTIMETERS:
				return "centimeters" if plural else "centimeter"
			case Unit.KILOMETERS:
				return "kilometers" if plural else "kilometer"
			case Unit.INCHES:
				return "inches" if plural else "inch"
			case Unit.METERS:
				return "meters" if plural else "meter"
			case Unit.FEET:
				return "feet" if plural else "foot"
			case _:
				return ""



class Confirmation(Enum):
	YES = 'Y'
	NO  = 'N'
	
	def __bool__(self):
		return True if self == Confirmation.YES else False
	
	def __str__(self):
		return "yes" if self == Confirmation.YES else "no"





# Even though this function is only used twice, I still decided to keep it
#  as a function because if you were a maintainer ov this application,
#  a scenario might come up in the future where you may need to reuse this
#  code.

"""
Converts an amount from unit to an amount ov another unit.

"src" stands for "source", "dst" stands for "destination", "msr" stands
 for "measure" – how much you have, and `unit` is just `unit`.

This could – and probably should – be turned into a wrapper type that
 stores a `float` and a `Unit`, but I'm too lazy.
 (I'll go the extra mile, but I'm not going that many extra miles.)
"""
def convert_unit(src_msr:float, src_unit:Unit, dst_unit:Unit) -> float:
	match (src_unit, dst_unit):
		# Feet-to-Inches  &  Inches-to-Feet
		case (Unit.FEET, Unit.INCHES):
			return src_msr*12
		case (Unit.INCHES, Unit.FEET):
			return src_msr/12
		
		# Kilometer-to-Meter  &  Meter-to-Kilometer
		case (Unit.KILOMETERS, Unit.METERS):
			return src_msr*1000
		case (Unit.METERS, Unit.KILOMETERS):
			return src_msr/1000
		
		# Centimeter-to-Meter  &  Meter-to-Centimeter
		case (Unit.CENTIMETERS, Unit.METERS):
			return src_msr/100
		case (Unit.METERS, Unit.CENTIMETERS):
			return src_msr*100
		
		# Because writing conversions to and from every unit would be
		#  absolutely ludicrous, I will use meters as a mediator between
		#  the units.
		case (Unit.INCHES, Unit.METERS):
			return src_msr/39.37
		case (Unit.FEET, Unit.METERS):
			return src_msr*0.3048
		case (Unit.METERS, Unit.INCHES):
			return src_msr*39.37
		case (Unit.METERS, Unit.FEET):
			return src_msr*3.28084
		
		# This basically says that a unit can convert to itself
		#  (e.g. meter -> meter).
		case (a, b) if a == b:
			return src_msr
		
		# Converts unit A to meters, then converts that to unit B.
		#
		# This tactic is nice, since if we add support for more units in
		#  the future, we technically only have to have a conversion from
		#  it to meters and meters to it.
		case (a, b):
			return convert_unit(
				convert_unit(src_msr, a, Unit.METERS),
				Unit.METERS,
				b
			)





print("Welcome to Rectangle Area Calculator!")

unit_type = input("What unit (e.g: in, ft, cm, et cetera) do you wish to measure in? ")

###########################################################################
#                                                                         #
#     We have not discussed error handling; however, in the real          #
#      world, this is absolutely necessary.                               #
#     If you don't account for certain situations, the program can,       #
#      seemingly without reason, exit, often times not even providing     #
#      (useful) error information to the end-user.                        #
#                                                                         #
#     `try`-`catch` is a very common error-handling pattern,              #
#      especially in C-like languages.                                    #
#     However, I don't like `try`-`catch`, as it doesn't seem             #
#      elegant — I like how Rust,  the programming language,  handles     #
#      errors by having a `Result` type which will let you use any        #
#      values you want to represent success and failure in                #
#      combination with pattern matching                                  #
#       (which is a feature I use in this program).                       #
#                                                                         #
###########################################################################
unit:Unit = None
try:
	unit = Unit(unit_type)
except ValueError:
	print(f"\"{unit_type}\" is not a known unit\n[hint: use the abbreviation ov the unit you wish to use]")
	exit(0x11)
except:
	print("An unexpected error occurred.")
	exit(0x01)

height = 0
width  = 0

try:
	width  = float(input(f"What is the width ov the rectangle in {unit.__str__(True)}? ").strip())
	height = float(input(f"What is the height ov the rectangle in {unit.__str__(True)}? ").strip())
	  # I hate that I had to define `height` after `width`, as I like
	  #  arranging my variables from longest to shortest, A-Z, 0-9,
	  #  et cetera, but I am forced to define it in this order due to
	  #  `input`, since it can't be "ordered" or
	  #  "queued in a certain order" (as far as I am aware).
	
	# Validate that the width and height are greater than or equal to zero;
	#  a negative area here wouldn't make sense.
	if width < 0 or height < 0:
		print("Negative sizes are unacceptable.")
		exit(0x21)
except ValueError:
	print("There was an error converting your input to a mumber.")
	exit(0x12)

# Calculate the area.
area = width*height

# Decides whether or not the next printed unit name is plural.
plural = False
if area != 1:
	plural = True

# Decides whether the area is an approximation or not.
# I thought this would be a nice touch.  ;3
approximate = area != round(area, 2)

# Prints the final result.
print(
	f"Your rectangle is {'(approximately) ' if approximate else ''}{round(area, 2):.2f} square {unit.__str__(plural)}."
)
if round(area, 2) == 0:
	print("[note: if your number was \"approximately\" zero, then it was too small to be displayed properly]")

# Offer to convert their final measurement to another unit.
do_conversion = False
response      = input("Would you like to convert the result to another unit? ")
try:
	do_conversion = bool( Confirmation(response) )
except ValueError:
	print(f"\"{response}\" is not 'Y' or 'N' – \"no\" assumed\n[hint: use 'Y' for \"yes\" and 'N' for \"no\"]")
	exit(0x13)
except:
	print("An unexpected error occurred.")
	exit(0x01)

if not do_conversion:
	# Exiting with a status code ov zero, in any language, means the
	#  program terminated successfully
	#  (i.e. everything went "according to plan").
	#
	# The program is exiting early, if we don't want to do the conversion,
	#  because otherwise the rest ov the code would have to be
	#  nested an `if`-block, which doesn't look great.
	exit(0x00)

# Get the new unit.
new_unit_type:str = None
new_unit:Unit = None

# While-loop to allow for multiple tries at answering.
while new_unit == None:
	try:
		new_unit_type = input("Which unit would you like to convert the answer to? ")
		new_unit = Unit(new_unit_type)
	except ValueError:
		print(f"\"{new_unit_type}\" is not a known unit\nThe available units are:", end="")
		for available_unit in Unit:
			print(f"\n\t{available_unit.value}", end="")
		print()
	except:
		print("An unexpected error occurred.")
		exit(0x01)

# Calculate the new area.
new_height = convert_unit(height, unit, new_unit)
new_width  = convert_unit(width, unit, new_unit)
new_area   = new_width*new_height

# Do the plurality thing again.
plural = False
if new_area != 1:
	plural = True

# Do the approximation thing again.
approximate = new_area != round(new_area, 2)

# Prints the result ov the conversion.
print(
	f"Your rectangle is {'(approximately) ' if approximate else ''}{round(new_area, 2):.2f} square {new_unit.__str__(plural)}."
)
if round(new_area, 2) == 0:
	print("[note: if your number was \"approximately\" zero, then it was too small to be displayed properly]")