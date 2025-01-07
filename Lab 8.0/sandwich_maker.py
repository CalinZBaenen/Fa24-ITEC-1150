"""
Description:  Take sandwich orders from the user!
Author:       Calin "Katty" Baenen
Date:         24/11/15
Note:         You will need to make sure you have the PyInputPlus library
               installed on your machine.
"""
import pyinputplus as pyip





# A class which describes sandwiches and their prices.
class Sandwich:
	SANDWICH_OVERVIEW_MESSAGE = "{bread}-bread with {protein}, {cheese}, {addon_combo}, and {sauce_combo}."
	
	protein:"SandwichOption"
	toasted:bool
	addons:"SandwichOption|None"
	cheese:"SandwichOption|None"
	sauce:"SandwichOption|None"
	bread:"SandwichOption"
	
	def __init__(self):
		self.toasted = False
		self.addons  = None
		self.cheese  = None
		self.sauce   = None
	
	def min_printing_len(self) -> int:
		return max(
			self.protein.min_printing_len(),
			0 if self.addons is None else self.addons.min_printing_len(),
			0 if self.cheese is None else self.cheese.min_printing_len(),
			self.bread.min_printing_len(),
			0 if self.sauce is None else self.sauce.min_printing_len()
		)
	
	# Description.
	def description(self) -> str:
		"""
		Returns a short description ov the sandwich.
		"""
		
		return Sandwich.SANDWICH_OVERVIEW_MESSAGE.format(
			addon_combo = "no addons" if self.addons is None else self.addons.content.lower(),
			sauce_combo = "no sauces" if self.sauce  is None else self.sauce.content.lower(),
			protein     = self.protein.content.lower(),
			cheese      = "no cheese" if self.cheese is None else f"{self.cheese.content.lower()}-cheese",
			bread       = f"Toasted {self.bread.content.lower()}" if self.toasted else self.bread.content
		)
	
	def total(self) -> float:
		return (
			self.protein.price +
			0 if self.addons is None else self.addons.price +
			0 if self.cheese is None else self.cheese.price +
			0 if self.sauce  is None else self.sauce.price +
			self.bread.price +
			0.05 if self.toasted else 0
		)



# A class which (primitively) describes an order.
class SandwichOption:
	content:str
	label:str|None
	price:float
	
	def __init__(self, v:dict=None):
		if type(v) is dict:
			self.content = v.get("content")
			self.label   = v.get("label")
			self.price   = v.get("price", 0)
	
	def min_printing_len(self) -> int:
		# 8 =
		#  7 for, at least, " ..... "  +
		#  1 for '$'.
		
		has_label = not self.label is None
		has_cont  = type(self.content) is str
		return (
			len(self.name())           +
			len(f"{self.price:0<5.2f}") +
			8
		)
	
	def name(self) -> str:
		s = self.content
		if not self.label is None:
			s += f" ({self.label})"
		return s





# [O]utput
def print_receipt(orders:list[Sandwich]):
	SANDWICH_TOTAL_ENTRY = "Sandwich Total — ${cost:0>5.2f}"
	INGREDIENT_ENTRY     = "{ingredient} — ${cost:0>5.2f}"
	
	receipt_width = 50
	grand_total   = 0
	
	# Find the receipt's width.
	for sandwich in orders:
		grand_total += sandwich.total()
		receipt_width = max(receipt_width, sandwich.min_printing_len())
	
	# Print a line (indicating the start ov the receipt).
	print('-'*receipt_width)
	
	# Print subreceipts for each sandwich.
	for sandwich in orders:
		# Clamp the length.
		line_len = min(max(sandwich.min_printing_len(), receipt_width), receipt_width)
		
		# Print (a cut version ov) the sandwich's description.
		print(cut_string(sandwich.description(), receipt_width))
		
		# Print sandwich details.
		s = INGREDIENT_ENTRY.format(
			ingredient = sandwich.bread.name(),
			cost       = sandwich.bread.price
		)
		s = s.replace('—', '.'*(line_len-len(s)))
		print(s)
		s = INGREDIENT_ENTRY.format(
			ingredient = sandwich.protein.name(),
			cost       = sandwich.protein.price
		)
		s = s.replace('—', '.'*(line_len-len(s)))
		print(s)
		if sandwich.toasted:
			s = INGREDIENT_ENTRY.format(
				ingredient = "Toasting Fee",
				cost       = 0.05
			)
			s = s.replace('—', '.'*(line_len-len(s)))
			print(s)
		if not sandwich.cheese is None:
			s = INGREDIENT_ENTRY.format(
				ingredient = sandwich.cheese.name(),
				cost       = sandwich.cheese.price
			)
			s = s.replace('—', '.'*(line_len-len(s)))
			print(s)
		if not sandwich.sauce is None:
			s = INGREDIENT_ENTRY.format(
				ingredient = sandwich.sauce.name(),
				cost       = sandwich.sauce.price
			)
			s = s.replace('—', '.'*(line_len-len(s)))
			print(s)
		if not sandwich.addons is None:
			s = INGREDIENT_ENTRY.format(
				ingredient = sandwich.addons.name(),
				cost       = sandwich.addons.price
			)
			s = s.replace('—', '.'*(line_len-len(s)))
			print(s)
		
		# Print the sandwich's total cost.
		print()
		'''
		Erik: 
		    Obviously, the missing piece above.
		
		-------------------------
		
		Calin:
		    There we go...
		    ... Took me longer than it probably should have, but I wanted
		     to make sure I give it that extra level ov polish.
		
		-------------------------
		
		Erik:
		    You're the only person who keeps my comments in as a conversation log, which I like, but every time I 
		    wrap up grading I run my output generator and then have to come back and remove all of the deductions 
		    because they show up again and momentarily confuse me.
		
		-------------------------
		
		Calin:
		    I'm sorry for the inconvenience this poses.
		    I would remove the deductions myself, but I aim to preserve
		     these documents as accurately as I can.
		'''
		s = SANDWICH_TOTAL_ENTRY.format(cost = sandwich.total())
		s = s.replace('—', '.'*(line_len-len(s)))
		print(s)
		
		# Print a line.
		print('- '*(line_len//3))
		'''
		Erik:
		    Technically, I should deduct half a point because the requirements are to display the prices for each
		    ingredient in each sandwich, but this is so much fun and so over the top that I just don't have the heart 
		    :-)
		    
		    Be aware though that professionally, going big with the code but missing the requirements will tend to not
		    go over well. I imagine you can probably guess that, but it's usually a reality programmers have to deal 
		    with if we want to get paid for writing code.
		
		-------------------------
		
		Calin:
		    > the requirements are to display the prices for each
		      ingredient in each sandwich
		    
		    Excluding the combos, I do technically do that, albeit without
		     tomatos and onions, which are required...
		    I can't believe I let another thing slip.
		    
		    Thankfully, thanksgivingsbreak is here, so I have some time to
		     catch up and breathe, then when we come back, I'll give you
		     even more well -made and -tested work, providing the same
		     signature charm I've tried to incorporate into all my
		     projects.
		    
		    > it's usually a reality programmers have to deal with if we
		      want to get paid for writing code.
		    
		    Right.
		    I can and will make this concession – you know I'm following
		     the gist ov the program and implement it.
		    
		    I'm sure you can tell: I'm making these assignments just as
		     much for their enjoyment value as their functionality.
		    
		    Ov course, I'll never "go rogue" and write code that is
		     unproductive or completely antithetical to the program's goal.
		    
		    Thank you for the reality check and pointing out this error, as
		     this is helpful to understand why others might not like my
		     program, even if it (generally) does do what they want.
		'''
	
	# Print the grand total
	print(f"Grand Total = ${grand_total:0>5.2f}")
	
	# Print a line (indicating the endov the receipt).
	print('-'*receipt_width)



def cut_string(s:str, cpl:int) -> str:
	lines = []
	words = s.strip().split()
	line  = ""
	
	i = 0
	l = len(words)
	while i < l:
		n = i+1
		
		if len(line)+len(words[i])+1 <= cpl:
			line = f"{line} {words[i]}"
			if n == l:
				lines.append(line)
		else:
			lines.append(line)
			line = f" {words[i]}"
		
		i = n
	
	return '\n'.join(lines)





# [M]ain
def main():
	orders:list[Sandwich] = []
	
	sauce_combos = {
		"Mustard": 0.05,
		"Mayo": 0.05,
		"Horseradishsauce": 0.05,
		"Mustard & mayo": 0.05,
		"Mustard & horseradishsauce": 0.05,
		"Mustard & mayo & horseradishsauce": 0.05
	}
	proteins     = {
		"Steak": 3.50,
		"Chicken": 3.50,
		"Turkey": 3.50,
		"Pork": 3.50,
		"Tofu": 2.00,
		"Ham": 3.50,
		"Salami": 3.50,
		"Bologna": 3.50,
		"Veggiepatty": 3.50,
		"Egg": 3.50
	}
	cheeses      = {
		"Cheddar": 1.50,
		"Provolone": 1.50,
		"Gouda": 1.50,
		"Creamcheese": 1.50,
		"Brie": 1.50,
		"Pepperjack": 1.50,
		"Swiss": 1.50,
		"Mozzarella": 1.50
	}
	addons       = {
		"Onions": 0.05,
		"Tomato": 0.10,
		"Lettuce": 0.15,
		"Onions & tomato": 0.15,
		"Onions & lettuce": 0.20,
		"Tomato & lettuce": 0.25,
		"Tomato & lettuce & onions": 0.30
	}
	breads       = {
		"Wheat": 0.50,
		"Rye": 0.50,
		"Sourdough": 1.00,
		"Bruschetta": 1.00,
		"Brown": 0.50,
		"Pumpernickel": 0.50,
		"Ciabatta": 1.00
	}
	
	# Get the (initial) amount ov sandwiches that the user wants.
	sandwich_ct = pyip.inputInt("How many sandwiches would like to make? ", min=1)
	
	n = 0
	while n < sandwich_ct:
		# Construct a sandwich(-order).
		order = Sandwich()
		
		# Keystone variables.
		toasted:str = None  # Whether or not the bread is toasted.
		a_pref:str  = None  # Addons.
		b_pref:str  = None  # Bread(type).
		c_pref:str  = None  # Cheese.
		p_pref:str  = None  # Protein(type).
		s_pref:str  = None  # Sauce combo.
		
		# Get the preferred breadtype, and whether or not it should be toasted.
		b_pref = pyip.inputMenu(list(breads.keys()), "Choose a bread!\n", numbered=True)
		toasted = pyip.inputYesNo("Would you like your bread toasted? ")
		
		# Get the preferred type ov protein.
		p_pref = pyip.inputMenu(list(proteins.keys()), "Choose a protein!\n", numbered=True)
		
		# Ask the user if they'd like cheese, then ask for which type ov cheese
		#  they would like if they answer affirmatively.
		if pyip.inputYesNo("Would you like cheese? ") == "yes":
			c_pref = pyip.inputMenu(list(cheeses.keys()), "Choose a cheese!\n", numbered=True)
			
			order.cheese = SandwichOption({
				"content": c_pref,
				"label": "Cheese",
				"price": cheeses[c_pref]
			})
		
		# Similar to the previous code-snippet, asks the user for their
		#  preferences about sauces and addons.
		if pyip.inputYesNo("Would you like any sauces? ") == "yes":
			s_pref = pyip.inputMenu(list(sauce_combos.keys()), "Choose a sauce combo!\n", numbered=True)
			
			order.sauce = SandwichOption({
				"content": s_pref,
				"price": sauce_combos[s_pref]
			})
		if pyip.inputYesNo("Would you like any addons (i.e. onions, tomato, lettuce)? ") == "yes":
			a_pref = pyip.inputMenu(list(addons.keys()), "Choose an addon combo!\n", numbered=True)
			
			order.addons = SandwichOption({
				"content": a_pref,
				"price": addons[a_pref]
			})
		
		order.protein = SandwichOption({
			"content": p_pref,
			"price": proteins[p_pref]
		})
		order.toasted = toasted == "yes"
		order.bread  = SandwichOption({
			"content": b_pref,
			"label": "Bread",
			"price": breads[b_pref]
		})
		
		# Add this order to the list ov orders, then print its description.
		orders.append(order)
		print(order.description())
		n += 1
		
		# Offer the user to order any additional lastminute sandwiches.
		if n == sandwich_ct and pyip.inputYesNo("Would you like to order any more sandwiches? ") == "yes":
			sandwich_ct += pyip.inputInt("How many more sandwiches would you like? ", min=1)
	
	# Print the receipt for the order.
	print_receipt(orders)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		exit(0)

'''
Erik:
    This is the first sandwich maker that actually made me feel a little hungry :-D

-------------------------

Calin:
    If this makes you hungry, you should look at how Nd Cube made the
     sandwiches in (the Mario Party minigame) Sandwiched:
      https://massivelyop.com/wp-content/uploads/2024/10/mario_party_jamboree_sandWIN.jpg
    
    There's something with programmers and food I guess.

-------------------------
Erik:
    A bit to...regular for me. I like bread with fractal edges.

-------------------------

Calin:
    Bread with fractal edges must by VERY filling!
'''