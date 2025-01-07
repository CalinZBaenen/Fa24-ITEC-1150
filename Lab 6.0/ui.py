from typing import Optional





def get_nonempty(prompt:str="") -> str:
	"""
	Gets non-empty input from the user.
	"""
	
	while True:
		out = input(prompt).strip()
		if len(out) > 0:
			return out



def get_yesno() -> Optional[bool]:
	ans = get_nonempty("[Y / N] ").lower()
	
	match ans:
		# Affirmative.
		case "yes" | 'y':
			return True
		# Negative.
		case "no" | 'n':
			return False
		# Other.
		case _:
			return None