"""
Description:  Generate a list ov random numbers and print it.
Author:       Calin "Katty" Baenen
Date:         24/10/28
Note:         `ui.py` is a required file to run this program, since it
               contains a commonuse function.
"""
from random import randint
from ui     import get_yesno_input, get_num_input





# [P]rocessing
def create_rand_list(n):
	nums = []
	i = 0
	while i < n:
		nums.append(randint(1, 100))
		i += 1
	nums.sort()
	'''
	Erik: 
	    Everything works if I add the obviously missing return here.
	
	-------------------------
	
	Calin:
	    Oops.

	-------------------------
	Erik:
	    LOL. I can only imagine how mortified you must've felt. (It happens to all of us.)
	'''
	return nums



# [O]utput
def display(nums):
	print(f"Here is your list ov five random numbers, sorted:\n\t{nums}")
	
	print(f"Here is your list, printed using the spread operator (*):\n\t", end="")
	print(*nums, sep=", ")
	
	print("Here is your list, printed in a loop and summed:\n\t", end="")
	res = 0
	i   = 0
	for n in nums:
		if i > 0:
			print(' ', end="")
		
		print(f"{n}", end="")
		
		if i < len(nums)-1:
			print(" +", end="")
		
		res += n
		i += 1
	print(f" = {res}")





# [M]ain
def main():
	while True:
		print("Welcome to Random Number Generator (RNG)!")
		
		display( create_rand_list(get_num_input("How many random numbers would you like? ", 1)) )
		
		run_again = get_yesno_input("Would you like some more random numbers? ")
		if not run_again:
			break

if __name__ == "__main__":
	main()