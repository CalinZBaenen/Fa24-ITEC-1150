"""
Description:  Calculates bus fares for a given standard and rush fee,
                as well as the amount ov times each fee has been collected.

Author:       Calin "Katty" Baenen
Date:         24/09/03
"""

# All values are measured in USD ($), with decimals representing cents (¢).
rush_bus_rides = 12    # Amount ov bus rides during rush-hour.
std_bus_rides  = 7     # Amount ov bus rides not during rush-hour.
rush_fee       = 3     # Rush-hour bus fee.
std_fee        = 1.75  # Standard bus fee.

# The total fee.
total = round((rush_bus_rides*rush_fee) + (std_bus_rides*std_fee), 2)

# Prints the total (being used in a sentence) using a format-string.
print(f"I spent ${total:,.2f} this month on bus fare.")

"""
Erik:
    I'd noticed the lack of formatting here, but it wasn't specifically called out as a requirement.

Calin:
   Thank you.

-------------------------

Erik:
   Nice job. 
"""