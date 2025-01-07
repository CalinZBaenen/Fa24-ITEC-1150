"""
Description:  Displays the total and average amount ov points for each ov a
               number ov students.
Author:       Calin "Katty" Baenen
Date:         24/10/06
Note:         `ui.py` is a required file to run this program, since it
               contains a commonuse function.
"""

from ui import get_int_input




def main():
	# Define key varables.
	students    = get_int_input("How many students are in the class? ", 1)
	scores      = get_int_input("How many scores does each student have? ")
	
	i = 0
	if scores > 0:
		while i < students:
			tot = 0
			j   = 0
			
			print(f"Enter information for student #{i+1}:")
			while j < scores:
				tot += get_int_input(f"Enter score #{j+1}")
				j += 1
			i += 1
			
			print(f"Total points for student #{i+1}: {tot}")
			print(f"Average score for student #{i+1}: {tot/scores:.2f}")
	else:
		print("There are no scores – goodie!")

if __name__ == "__main__":
	main()