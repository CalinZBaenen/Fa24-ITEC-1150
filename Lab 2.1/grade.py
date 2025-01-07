"""
Description:  A program that translates a test score (0 to 100) into a
                grade (F to A+).
Author:       Calin "Katty" Baenen
Date:         24/09/10
"""

score = input("Enter your test score (0 to 100): ")

if score.isnumeric() is True:
	grade = ""
	score = int(score)
	hint  = ""
	
	if score >= 90:
		grade = 'A'
		hint  = "Excellent job! – Keep up the great work!"
	elif score >= 80:
		grade = 'B'
		hint  = "Nicely done!"
	elif score >= 70:
		grade = 'C'
		hint  = "You should work on improving your grade..."
	elif score >= 60:
		grade = 'D'
		hint = "Your grade is below a C; you should meet with an instructor soon."
	else:
		grade = 'F'
		hint = "Meet with an instructor as soon as possible."
	#
	# ... What?  Not going down to Fs?
	'''
	Erik: -0.25
	    Display a letter grade for any numeric value entered.
	    Just a guess, but I suspect you don't like D/F grades as a thing? It's just a simple program, and it *is* the 
	    requirement...
	
	-------------------------
	
	Calin:
	  My mistake; it didn't tell us the threshold for D and F, and I hadn't
	    seen that displaying a letter grade was a requirement, so I just
	    assumed I shouldn't do anything.
	    
	-------------------------
	
	Erik:
	    LOL. That's a much more obvious reason.
	'''
	if score >= 100:
		hint = "You should get an A+! – Keep up the great work!"
	
	if grade != "":
		print(f"Grade: {grade}")
	print(hint)
else:
	print("This program only accepts (whole) numbers from zero to one-hundred; rerun the program to try again.")

'''
Erik:
    Nice job. 
'''