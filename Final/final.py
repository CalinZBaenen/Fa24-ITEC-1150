"""
Dependencies:
               Python:       3.11.0
               PyInputPlus:  0.2.12
               Requests:     2.23.3
               JSON:         2.0.9
Description:   A program that allows a user to order pizza.
Author:        Calin "Katty" Baenen  <calinbaenen@gmail.com>
Date:          24/12/18

       @@#[@@@                          
       @ @@@@ #@@               @@@@@   
       @ @    @@ @@   @@@ @@@+ (@@@@@@  
       @ @       @ @+      @@@@@]  @@   
       @>]@  @@@@@ :-)]]](^-    @@@     
        @ @#@@--    =<]]]]]]]]]>. ~@    
       @@@*=+ ={@@@@@^=^]]]>+   =^ @@   
       @< -<=]@@  @@ @@ ^]+*@@@@@*+ @   
       @>+)()@   @    @@[@=@    @@~ @   
       @}^>>@(  @*.%] @]@ ^@  @  @  @   
       @@ >+@    @ =  @{>  @@ @  @ (@   
        @@: (@   @@+ @@     @@@  @@@@@@ 
   @@@@@@@@@@@@    ]@@  @@@)   .@@    @ 
@@             ~@@#~     @@ . @     @@] 
@>       ^^^^^^^^^^<*:@   }   @[=+:   %@
  @@@@@@-^^^^^^^***^* @@@@@@@@      @@  
    @@   ^^^*=:.~~-:.           @@@     
   @@  ::..:.~).   *==~      @@         
   @           [@@ ~~*++@@@@            
    @@@@@@@@@@                          
"""
import pyinputplus as pyip
import requests
import json

from collections.abc import Iterable
from pizzalib        import *
from requests        import ConnectionError as ReqErr
from pathlib         import Path





__version__ = "1.0.0"
__author__  = "Calin Z. Baenen  <calinbaenen@gmail.com>"



INGREDIENTS_PATH:Path    = Path("ingredients.json")
UPDATE_OPTIONS:list[str] = ["online", "locally"]
COMMANDS:dict[str, str]  = {
	"help": "Prints a menu with the commands you can use, as well some helpful advice.",
	"order": "Order something else.",
	"checkout": "Submit your order and show the receipt.",
	"credits": "Print the credits for the application.",
	"review": "Review your order.",
	"exit": "Exit the program."
}
KATTY:str                = "            @@@@@@@@                                            \n           @@@#***#%@@@@                                        \n           @@##@@@@#**#@@@@                        @@@@@@@@@    \n           @@#%#::=#@@%#*#@@@               @%@@@@@@@@@@@%@@    \n           @%##%-:....-*%@##@@@@@@@@@@@@@@@@@%##%@@%#*==@%@@    \n           @@##@=:........%@%*@@##**+**+**#@@@#@@@*=-::#@@@     \n           @@##@*::.::::--=+@@***+*++*++**++***####@@=%@@@      \n            @%#%@-::+%*@@####*+*+**+**++**++*++++++#@@@@        \n            @@##@@=@@###***+++*++**+**+**+***+*****+**#@@       \n             @@#%@@@#***+***+**++*++*++*++**++**+*++*++*@@      \n            @@@@###**+*+++*######**+**+**+*++**++**+****#@@     \n            @@#*****+***#@%+=-+%@@@#+*+**+****#%%%#*++*+*@@     \n           @@%**++*++*#@*   -@*:::=@%*++*++**@@=#@%@**++*#@     \n           @@#**+**+*#@.   +%:   ::#@#***++#@# .:# *@****#@     \n           @@##***++#@    .%: .::::=@@*+***%@::::=  @#*++#@     \n           @@%#**+**@*    -*::::-::-@#*+-=+%@::::+  =@***#@     \n            @@##*+**%     -+:::-:::=@**=::=#@*:-:#  :@**#@@     \n            @@##**+*%      %---:::-#@*+::::=%%-:=#  :@###@@     \n             @@###**%#     =#-:::-=@#=::::::=#@%@-  .@##@@@@@@@ \n              @@###**@=     =%*==%@#=:::::::::+#+--=*#%@@%+==*%%\n      @@@@@@@@@@@@###*%#.      =#*+-:::*%#+=:::::::=@@+-::-=+@@ \n  @@@@#=:::::::-==#@@*=+++++====-::::::@@@@@*:::::::::::::=#@@  \n @@*==-::::::::::::::::::::::::::::::::-=#*=::::*+:::::::-@@@@@ \n@%==--=---::::::::::::::::::::::::-#=:::::::::::*%-::::::::==*@@\n @@@#+====---:::::::::::::::::::::-%+:::-#@=---+@#:::::::-==%@@ \n    @@@@@@@@-::::::::::::::::::::::+@%##%@*#####=::::::-=*@@@   \n        @@#-:::::::::::::::::::::::::::-::::::::::--=*@@@@      \n       @@=::::::::::::::::---::::::::::::::::---==%@@@          \n      @@::::::::::::::::--=-----=-----------===#@@@             \n     @%-:::::::::::----==#=====-=------====+#%@@                \n     @*----------=--=-==*@@@%+=*******@@@@@@@                   \n     @@#===========+#@@@                                        \n        @@@@@@@@@@@@                                            "
TIPS:str                 = "Tip: You can order some things together, such as different cheeses – to do so, separate the desired options with a comma.\nTip: When placing an order, you can refer to items by their number rather than their name, making it faster to order certain items."
URL:str                  = "https://itec-minneapolis.s3.us-west-2.amazonaws.com/ingredients.json"





# Offer the user which method they would like to use to fetch the menu,
#  then return it (or `None` in the case ov an error).
#
# I really couldn't think ov a better name for this function.
def get_menu_from_offered_fetch_method() -> KattysPartyPizzaMenu|None:
	menu = None
	mthd = pyip.inputMenu(UPDATE_OPTIONS, "How would you like to update the menu?\n", numbered=True)
	
	# Fetch the new menu based on the method chosen.
	match mthd:
		case "locally":
			menu = get_local()
		case "online":
			menu = get_d2l()
		case _:
			pass
	
	return menu



# Get a pizza order.
def get_pizza_order(menu:KattysPartyPizzaMenu) -> Pizza:
	# Get the base options for the pizza.
	base_options = list()
	for bo in menu["base_options"]:
		opts = list(bo["options"].keys())
		size = None
		
		# Ask which category ov base-option the customer would like.
		print(f"What type ov {bo['category']} would you like?")
		
		# Allow the user to select their base options based on whether or
		#  not it is comboable.
		if bool(bo.get("comboable")):
			for item in inputChoices("", opts):
				ingredient = IngredientSelection(item, bo["options"][item], 1)
				base_options.append(ingredient)
		else:
			item = pyip.inputMenu(opts, "", numbered=True)
			
			ingredient = IngredientSelection(item, bo["options"][item], 1)
			base_options.append(ingredient)
	
	# Get the toppings for the pizza.
	toppings = list()
	for item in inputChoices(f"Which toppings would you like?", list(menu["toppings"].keys()), True):
		ingredient = IngredientSelection(item, menu["toppings"][item], 1)
		toppings.append(ingredient)
	
	# Offer the customer pizza-sizes if there are sizes to choose from.
	if menu.get("sizes") is not None:
		size = pyip.inputMenu(list(menu["sizes"].keys()), f"How big would you like your pizza?\n", numbered=True)
	
	# Create and return the pizza.
	return Pizza(base_options, toppings, size)



# Get an order for a side.
def get_sides_order(menu:KattysPartyPizzaMenu) -> list[IngredientSelection]:
	sides = list()
	for side in menu["sides"]:
		print(f"Would you like (a) {side['category']}?")
		
		# If the user accepts this side, list the different types ov each
		#  side.
		if pyip.inputYesNo(prompt="[y / n] ") == "yes":
			item = pyip.inputMenu(list(side["options"].keys()), f"Which {side['category']} would you like?\n", numbered=True)
			size = None
			if side.get("sizes") is not None:
				size = pyip.inputMenu(list(side["sizes"].keys()), f"What size would you like your {item}?\n", numbered=True)
			
			ingredient = IngredientSelection(item, side["options"][item], 1, size)
			if size is not None:
				ingredient.price += side["sizes"][size]
			sides.append(ingredient)
	
	return sides



# Print the credits.
def print_credits():
	print("[2J[u", end="")
	print(KATTY)
	print("This application was created and published Calin \"Katty\" Baenen.\nhttps://calinzbaenen.github.io/\n")



# I know you said you'd waive this, though, I want to give some insight as
#  to why this function exists anyways.
#
# This function exists because `pyinputplus.inputChoice` only allows you to
#  input one option at a time; however, with some things being "comboable",
#  it's necessary that multiple options can be selected in the same prompt,
#  since some categories,  such as `toppings`,  become so ridiculously big
#  asking a yes/no question for every single item would become bothersome
#  for the user.
def inputChoices(prompt:str, choices:Iterable[str], allow_empty:bool=False) -> list[str]:
	"""
	Prompts the user to select one or more options from a numbered list and
	returns the selected ones as strings in an array.
	
	```
	>>> inputChoices("This is a test.", ["Ketchup", "Mustard", "Mayo"])
	This is a test.
	1. Ketchup
	2. Mustard
	3. Mayo
	1, mayo
	["Ketchup", "Mayo"]
	```
	"""
	
	# Define key variables.
	amt_choices = len(choices)
	selections  = list()
	cic         = list(filter(lambda s: s.strip().casefold(), choices))
	
	# Print the prompt and the choices.
	if prompt != "":
		print(prompt)
	for n in range(amt_choices):
		print(f"{n+1}. {choices[n]}")
	
	# Loop to get input.
	while True:
		# Get input from the user.
		# (This is using `pyip.inputStr` rather than `input` so that it
		#  adheres as closely to the requirements as possible.)
		i:str = pyip.inputStr().casefold()
		
		# Check to see if the input is empty or not.
		# If `allow_empty` is true and the input is empty, the function can
		#  immediately break out ov the loop, otherwise if `allow_empty` is
		#  false and the input is empty,
		match (allow_empty, len(i)):
			# Empty, empty allowed.
			case (True, 0):
				break
			# Empty, empty not allowed.
			case (False, 0):
				print("You must choose one or more options.")
				continue
			# Other.
			case _:
				pass
		
		# Loop to validate input.
		for (idx, opt) in enumerate(i.split(',')):
			opt = opt.strip()
			
			ival = 0
			try:
				ival = int(opt)
			except:
				pass
			
			# Validate whether the input is a valid selection or not,
			#  allowing for items to be chosen by number.
			if opt in cic:
				selections.append(choices[idx])
			elif ival <= amt_choices and ival > 0:
				selections.append(choices[ival-1])
			else:
				print(f"\"{opt}\" is not a valid choice.")
		break
	
	return selections



# Print an order.
def print_order(order:KattysPartyPizzaOrder):
	if order.is_empty():
		print("[There is nothing to review.]")
	
	# Define key variables.
	itnolb_maxlen = len(order.pizzas)+len(order.sides)    # The max len ov the item number.
	item_no       = 1                                     # Item number. (Used for numbering items.)
	
	# Print the pizza details
	print("Pizzas:")
	for pizza in order.pizzas:
		print(f"    #{item_no:0>{itnolb_maxlen}} {pizza} (${pizza.price():0>5.2f}):")
		for bopt in pizza.base_options:
			print(f"{'        '+str(bopt): <58}  ${bopt.price:0>5.2f}")
		for top in pizza.toppings:
			print(f"{'        '+str(top): <58}  ${top.price:0>5.2f}")
		item_no += 1
	
	# Print the side details.
	print("Sides:")
	for side in order.sides:
		lead = f"    #{item_no:0>{itnolb_maxlen}}"
		print(f"{lead+' '+str(side): <58}  ${side.price:0>5.2f}")
		item_no += 1



def save_order(order:KattysPartyPizzaOrder):
	# Calculate the "plain" version ov the data.
	out = {
		"pizzas": [{
			"toppings": [{"name": topping.name, "price": topping.price} for topping in pizza.toppings],
			"base": [{"name": bopt.name, "price": bopt.price} for bopt in pizza.base_options]
		} for pizza in order.pizzas],
		"sides": [{
			"description": side.description,
			"amount": side.amount,
			"price": side.price,
			"name": side.name,
			"size": side.size
		} for side in order.sides]
	}
	
	# Write the data to a file.
	try:
		f = open("order.json", "w+")
		f.write(json.dumps(out))
		f.close()
	except:
		pass



def get_local() -> KattysPartyPizzaMenu|None:
	# Check if the path to the ingredients exists and is a file, and open
	#  the file if so.
	if not (INGREDIENTS_PATH.exists() or INGREDIENTS_PATH.is_file()):
		print(f"A file named `{INGREDIENTS_PATH}` must exist to update the menu locally.")
		return None
	f = open(INGREDIENTS_PATH, 'r', encoding="utf-8")
	
	# Read the file and close it.
	txt = f.read()
	f.close()
	
	# Return the parsed menu.
	return KattysPartyPizzaMenu.from_dict( json.loads(txt) )



def get_d2l() -> KattysPartyPizzaMenu|None:
	try:
		# Make a request.
		req = requests.get(URL)
		
		# Check to make sure the response is OK, and take the response-text
		#  if so.
		if req.status_code != 200:
			print(f"Something went wrong, and a ({req.status_code}) error occurred while trying to fetch the list ov available ingredients.\nCheck in your browser to make sure {URL} exists.")
			raise Exception()
		txt = req.text
		
		# Close the request and return the parsed menu.
		req.close()
		return KattysPartyPizzaMenu.from_dict( json.loads(txt) )
	except:
		return None





def main() -> int:
	# Define key variables.
	order_placed:bool           = False                      # Whether or not the order has been placed. (Used for warning the user upon exiting.)
	blanks:int                  = 0                          # The amount ov blank lines the user has entered (in a row).
	order:KattysPartyPizzaOrder = KattysPartyPizzaOrder()    # The order to be placed.
	menu:KattysPartyPizzaMenu   = get_d2l()                  # The menu which describes the available ingredients.
	e:int                       = 0                          # Error count.
	
	# Indicate that an error has occured.
	if menu is None:
		print("An occurred while trying to load the menu.")
	while menu is None:
		print(f"Would you like to try reloading the menu{'' if e == 0 else ' again'}?")
		if pyip.inputYesNo("[Y / n] ", default="yes", limit=1) == "yes":
			menu = get_menu_from_offered_fetch_method()
		else:
			return 1
		e += 1
	
	# Print a greeting and some basic instructions.
	print("Welcome to Katty's Party-Pizza Pizza-Maker!")
	print("For instructions on how to use the program, type \"help\" and press enter. — When you are ready to start your order, type \"order\" and press enter.")
	
	# Loop for user-input.
	while True:
		# Allow the user to clear the screen by entering three blank lines
		#  consecutively in case it gets too cluttered...
		#
		# ... which, from experience testing, I can say happens A LOT.
		if blanks >= 3:
			print("[2J[u", end="")
			blanks = 0
		
		# Get a command.
		i = pyip.inputStr("> ", blank=True).casefold()
		l = len(i)
		
		# Count the consecutive amount ov blank lines inputted.
		if l == 0:
			blanks += 1
		else:
			blanks = 0
		
		# Match the command.
		match i:
			# Submit your order.
			case "checkout":
				if order.is_empty():
					print_order("You have not yet added any food-items to your order.")
					continue
				
				print_order(order)
				print(f"Total: ${order.total():0>5.2f}")
				print('-'*50)
				print("Are you sure you'd like to place your order?\n (This decision is FINAL.)")
				if pyip.inputYesNo("[y / N] ", default="no", limit=1) == "yes":
					save_order(order)
					break
			
			# Print the credits.
			case "credits":
				print_credits()
			
			# Review the currently placed order.
			case "review":
				print_order(order)
			
			# Use my version ov the menu.
			case "update":
				try:
					new_menu:KattysPartyPizzaMenu|None = get_menu_from_offered_fetch_method()
					
					# Check if the menu could be updated (this way) and
					#  report it could or not.
					if new_menu is None:
						print(f"The menu could not be updated.  :(")
					else:
						menu = new_menu
						print("Menu updated!")
				except:
					pass
			
			# Place an order.
			case "order":
				# Offer a pizza.
				print("Would you like a pizza?")
				if pyip.inputYesNo("[y / n] ") == "yes":
					pizza_order = get_pizza_order(menu)
					order.pizzas.append(pizza_order)
					print(f"You have added a {pizza_order} to your order.")
				
				# Offer a side.
				if "sides" in menu and menu["sides"] is not None:
					print("Would you like a side?")
					if pyip.inputYesNo("[y / n] ") == "yes":
						sides_order = get_sides_order(menu)
						order.sides.extend(sides_order)
						print(f"{len(sides_order)} side(s) has been added to your order.")
			
			# Exit the program.
			case "exit":
				if not order_placed and not order.is_empty():
					print(f"You have not placed your order yet!\nAre you sure you want to exit?")
					if pyip.inputYesNo("[y / N] ", default="no", limit=1) == "yes":
						break
				else:
					break
			
			# Print an elementary help-menu.
			case "help":
				for command in COMMANDS:
					print(f"{command}\n\t{COMMANDS[command]}")
				print()
				print(TIPS)
				print()
			
			# Indicate that the command was not recognized.
			case cmd if l > 0:
				print(f"The command \"{cmd}\" was not recognized.\n (Use \"help\" for help.)")
	
	return 0

if __name__ == "__main__":
	exit(main())

'''
Erik:
    This is fun, as always. Really great work!
'''