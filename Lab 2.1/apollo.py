"""
Description:  A program that quizzes the user on Apollo 11.
Author:       Calin "Katty" Baenen
Date:         24/09/10
"""

print("QUIZ TIME!")

ans = input("What year did Apollo 11 land on the moon? ")
if ans.isnumeric():
	yr = int(ans)
	if yr == 1969:
		print(f"Your answer ({yr}) is correct!")
	elif yr == 1970 or yr == 1968:
		print(f"Your answer ({yr}) is close but off by a year!\nThe correct answer is 1969.")
	else:
		print(f"Your answer ({yr}) is incorrect.\nThe correct answer is 1969.")
else:
	print("Error: Your input may only be a (whole) number.")

'''
Erik:
    Nice job.
'''