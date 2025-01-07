"""
Description:  Calculates the average test score from a list ov them.
Author:       Calin "Katty" Baenen
Date:         24/09/03
"""

# A list ov each student's test score.
scores = [45, 74, 63]

# Note:
#  I am aware this is technically not what the assignment called for;
#    however, in a realworld scenario, you would want this to be a list
#    since it lets you have a variable number ov scores, both hardcoded
#    and not.
#  
#  Not only is this more ergonomic and future-proof design, but the
#    naming convention is nearly identical anyways, so you are not
#    losing any clarity.
#  (I.e.  `scores[0]`  is just as clear as  `score1`.)

# Average score,  `(a + b + c + ...) / #terms  =  avg`.
avg_score = round(sum(scores)/len(scores), 2)

# Print the average.
print(f"The average test score is: {avg_score}.")

'''
Erik:
    Normally I would frown on someone using language features we haven't discussed in class as it's often an indication
    they didn't write the code. However, your comments make it clear you know what you're doing. Your approach is 
    obviously better than the novice level code I expect.  
'''