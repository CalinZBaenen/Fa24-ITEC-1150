"""
Description:  Displays the total and average amount ov points for each ov a
               number ov students.
Author:       Calin "Katty" Baenen
Date:         24/09/29
"""

# Important variables.
avg_display = ""
students = 0
scores = 0

# Get the number ov students.
while True:
    txt = input("How many students are in the class? ")
    if txt.isnumeric() and int(txt) > 0:
        students = int(txt)
        break
    # Typically, zero is considered neutral, rather than positive or
    #  negative, so there is no need specifying "greater than zero".
    print("You must enter a positive, whole number ov students!")

# Get the number ov scores per student.
while True:
    txt = input("How many scores does each student have? ")
    if txt.isnumeric():
        scores = int(txt)
        break
    # Ditto previous comment.
    print("You must enter a nonnegative, whole number ov scores!")

# Have the user enter the number ov scores, if there are any.
i = 0
if scores > 0:
    while i < students:
        tot = 0
        j = 0

        print(f"Enter information for student #{i + 1}:")
        while j < scores:
            txt = input(f"\tEnter score #{j + 1}: ")
            if txt.isnumeric():
                tot += int(txt)
            else:
                print("You must enter a nonnegative, whole number.")
                '''
                Erik:
                    Because it's enough of a challenge for most students to handle loops and break. Adding another 
                    flow-control construct is one step to far for most people. Remember, this is an intro to programming
                    course, not a Python for people who already know how to program course. There's a *lot* of stuff
                    that necessarily gets glossed over (for example, I left out a huge amount of detail on scoping in 
                    Python and said some things that are technically incorrect but are good enough for a working model.
                    
                    It's like teaching Newtonian physics instead of diving into relativity, or showing someone the 
                    Rutherford model of the atom instead of jumping right to the quantum model. The goal is to get 
                    groundwork laid (even if we later have to re-teach some things when people are ready). You're a 
                    special case, as you're well beyond what is being taught in this course. 
                '''
                continue  # I dunno why we didn't go over `continue`, since
                #  it is basically `break`'s companion.
            j += 1
        i += 1

        print(f"Total points for student #{i + 1}: {tot}")
        print(f"Average score for student #{i + 1}: {tot / scores:.2f}")
else:
    print("There are no scores – goodie!")