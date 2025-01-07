import re

from typing import TypedDict, Self





SANITIZATION_REGEX = re.compile(r"[\W\-_]+", re.IGNORECASE)





##########     Menu Related Code     ##########

# Describes an ingredient option.
class IngredientDescriptor(TypedDict):
	"""
	Represents an object that describes a single ingredient.
	
	The type is structured as follows:
	```json
	{
	  "example": {
	    "description": "A fruit-bowl consisting ov apples, pears, orange-slices, and nuts.",
	    "price": 5.00
	  }
	}
	```
	"""
	
	def from_dict(d:dict) -> Self:
		"""
		Converts a normal `dict` into an `IngredientDescriptor`,
		synthesizing default values for fields that are not present.
		"""
		self = IngredientDescriptor()
		
		cost = d.get("price")
		desc = d.get("description")
		
		self['description'] = "" if desc is None else str(desc)
		self["price"]       = 0. if cost is None else float(cost)
		
		return self
	
	# A (brief) description ov the ingredient.
	description:str
	# The price ov the ingredient.
	price:float



# Describes the restaurant's menu.
class KattysPartyPizzaMenu(TypedDict):
	"""
	Represents the deserialized menu, containing all the necessary
	information about (pizza) ingredients and their pricing.
	"""
	
	def from_dict(d:dict) -> Self:
		self = KattysPartyPizzaMenu()
		
		# Do some
		t = type(d)
		if t is not dict:
			raise TypeError(f"expected dict value while converting to KattysPartyPizzaMenu but found {t} instead")
		d = d.copy()
		
		# Get the (potential) values for each key.
		bopts = d.get("base_options")
		sides = d.get("sides")
		sizes = d.get("sizes")
		tops  = d.get("toppings")
		
		# Pop the "consumed" keys.
		d.pop("comboable", None)
		d.pop("category", None)
		d.pop("options", None)
		d.pop("sizes", None)
		
		# Set the values on self.
		self["base_options"] = list(map(lambda d: IngredientCategory.from_dict(d), bopts))
		self["toppings"]     = dict( zip(tops.keys(), map(_stabilize_inde_value, tops.values())) )
		self["sides"]        = sides if sides is None else list(map(_stabilize_inde_value, sides))
		self["sizes"]        = sizes if sizes is None else dict(sizes)
		
		# Add any key-value pairs that may potentially be remaining.
		for residue in d:
			self[residue] = d[residue]
		
		return self
	
	# Base pizza options.
	base_options:"list[IngredientCategory]"
	# Toppings that can be added to the pizza.
	toppings:dict[str, IngredientDescriptor|float]
	# Sides that can go with the pizza.
	sides:"list[IngredientCategory]|None"
	# The sizes that a pizza can come in.
	sizes:dict[str, float]|None



# Describes a category ov ingredients.
class IngredientCategory(TypedDict):
	"""
	Represents a category ov ingredients.
	
	The type is structured as follows:
	```json
	{
	  "example": {
	    "comboable": false,
	    "category": "fruit-salad",
	    "options": {
	      "Kiwi-Go-Round": {
	        "description": "Kiwi, peach, and mandarin oranges drizzled in lemon juice.",
	        "price": 5.00
	      },
	      "apple & fig": 5.00
	    }
	  }
	}
	```
	"""
	
	def from_dict(d:dict) -> Self:
		self = IngredientCategory()
		
		# Do some elementary typechecking.
		t = type(d)
		if t is not dict:
			raise TypeError(f"expected dict value while converting to IngredientCategory but found {t} instead")
		d = d.copy()
		
		# Get the (potential) values for each key.
		comboable = d.get("comboable")
		category  = d.get("category")
		options   = d.get("options")
		sizes     = d.get("sizes")
		
		# Pop the "consumed" keys.
		d.pop("comboable", None)
		d.pop("category", None)
		d.pop("options", None)
		d.pop("sizes", None)
		
		# Set the values on self.
		self["comboable"] = False  if comboable is None else bool(comboable)
		self["category"]  = ""     if category  is None else str(category)
		self["options"]   = dict() if options   is None else dict( zip(options.keys(), map(_stabilize_inde_value, options.values())) )
		self["sizes"]     = sizes  if sizes     is None else dict(sizes)
		
		# Add any key-value pairs that may potentially be remaining.
		for residue in d:
			self[residue] = d[residue]
		
		return self
	
	# Whether or not ingredients ov this type can be comboed.
	comboable:bool|None
	# The type ov ingredient this is.
	category:str
	# The different variants ov this type ov ingredient.
	options:dict[str, IngredientDescriptor|float]
	# The sizes this 'ingredient' is available in.
	sizes:dict[str, float]|None

##########     Menu Related Code     ##########





##########     Order Related Code    ##########

# Describes a full order.
class KattysPartyPizzaOrder:
	def __init__(self):
		self.pizzas = list()
		self.sides  = list()
	
	def is_empty(self) -> bool:
		return len(self.pizzas) == 0 and len(self.sides) == 0
	
	def total(self) -> float:
		res = 0.
		for pizza in self.pizzas:
			res += pizza.price()
		for side in self.sides:
			res += side.price
		return res
	
	pizzas:"list[Pizza]"
	sides:"list[IngredientSelection]"



# Represents a side that can go with a pizza.
class IngredientSelection:
	"""
	Represents a side dish to go with a pizza.
	
	This is essentially just have an `IngredientDescriptor` with a name
	that is the preserved key.
	"""
	
	def __init__(self, name:str, description:IngredientDescriptor|float|int|str|None=None, amount:int=0, size:str|None=None):
		self.description = None
		self.amount      = amount
		self.name        = name
		self.size        = size
		
		t = type(description)
		if t is IngredientDescriptor or t is dict:
			self.description = description["description"]
			self.price       = description["price"]
		elif t is float or t is int:
			self.description = None
			self.price       = float(description)
		elif t is str:
			self.description = description
			self.price       = 0.
		else:
			raise ValueError(f"expected IngredientDescriptor, int/float, or str, but got {t}")
	
	# Stringify an ingredient selection.
	def __str__(self):
		return f"{str(self.amount)+' ' if self.amount != 1 else ''}{self.size+' ' if self.size is not None else ''}{self.name}{'s' if self.amount != 1 else ''}"
	
	# The description ov the side.
	description:str|None
	# The amount ov this product to be ordered.
	amount:int
	# The price ov this side (before multiplication by `amount`).
	price:float
	# The name ov this side.
	name:str
	# The desired size ov the item, adding this amount
	size:str|None



class Pizza:
	def __init__(self, base_options:list[IngredientSelection]|None=None, toppings:list[IngredientSelection]|None=None, size:str|None=None):
		self.base_options = base_options if base_options is not None else list()
		self.toppings     = toppings     if toppings     is not None else list()
		self.size         = size
	
	def __str__(self):
		out = f"{self.size+' ' if self.size is not None else ''}pizza with "
		
		# Loop through the toppings to get a general idea ov what this
		#  pizza is.
		i = 0
		l = len(self.toppings)
		while i < l:
			topping = self.toppings[i]
			
			# Add a new ingredient to the output string.
			if i == l-1 and l > 1:
				if l == 2:
					out += ' '
				out += "and "
			out += topping.name.lower()
			if i < l-1 and l > 2:
				out += ", "
			
			i += 1
		
		return out
	
	# Get the price ov the pizza.
	def price(self) -> float:
		total = 0.
		for bo in self.base_options:
			total += bo.price
		for top in self.toppings:
			total += top.price
		return total
	
	# The base configuration ov the pizza.
	base_options:list[IngredientSelection]
	# The toppings the pizza is decorated with.
	toppings:list[IngredientSelection]
	# The size ov the pizza.
	size:str|None

##########     Order Related Code    ##########





# Make sure a value is a valid ingredient-descriptor.
def _stabilize_inde_value(v:IngredientDescriptor|float|dict|None) -> IngredientDescriptor|float:
	"""
	Stabalize a value that could potentially become an
	`IngredientDescriptor` and return it.
	"""
	
	# If `v` is None, return zero.
	if v is None:
		return 0.
	
	t = type(v)
	if t is float or t is IngredientDescriptor:
		return v
	elif t is dict:
		return IngredientDescriptor.from_dict(v)
	
	return float(v)