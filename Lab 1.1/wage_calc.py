"""
Description:  Calculates an employees wage, including overtime.
Author:       Calin "Katty" Baenen
Date:         24/09/03
"""

ot_hours = 10     # The amount ov overtime hours worked.
ot_rate  = 1.5    # The bonus multiplier for overtime.
hours    = 40     # The amount ov scheduled hours worked.
wage     = 15.34  # The standard wage in USD ($) per hour.

# Calculate and print the total.
total = round(hours*wage + (ot_rate*wage)*ot_hours, 2)  # Formula: (wage * hours) + (overtime_rate * wage)*overtime_hours
print(f"Your gross pay is ${total:.2f}.")


"""
Erik:
    > You should be relieved to know that the formatting error was an
      oversight on my part; I knew to do it, but somehow forget.
      
    I assumed as much; I thought it unlikely you didn't know how.
    
-------------------------

Calin:
    > I deserve a deduction as an instructor as the lab notes suggested looking at slide 35 in the lecture notes, but
    should've referenced slide 36
    
    I believe both slides are equally important; however, it shouldn't be
      a huge deal, since you'd naturally see the slides together.
    
    You should be relieved to know that the formatting error was an
      oversight on my part; I knew to do it, but somehow forget.
    
    Takeaway:  small errors – mistakes – can happen.
    
    
    (P.S:  I've also patched `bus_fare.py` as,  even though it isn't marked incorrect,  it shares the same bug.)

-------------------------

Erik: 
    Ensure the output value is rounded to two decimal places (no more, no less).
    Expected:
        Your gross pay is $843.70.
    Your program's output:
        Your gross pay is $843.7.
        
    I deserve a deduction as an instructor as the lab notes suggested looking at slide 35 in the lecture notes, but
    should've referenced slide 36 (formatting strings). 
"""