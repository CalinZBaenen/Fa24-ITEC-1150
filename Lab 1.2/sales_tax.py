"""
Description:  Calculates the sales tax on a transaction.
Author:       Calin "Katty" Baenen
Date:         24/09/14
"""

# Set column widths.
price_col_width = 13
name_col_width  = 15

# Get the cost ov the order.
cost = float(input("What is the total cost ov your purchase? $"))

# Calculate the tax for state and province respectively.
province_tax = round(cost*0.05, 2)
state_tax    = round(cost*0.025, 2)
total        = round(cost+(cost*0.05)+(cost*0.025), 2)

# Round the cost, now that the precise value is no longer needed.
cost = round(cost, 2)

# Print the table.
print("Custom Delivery Sales Receipt")
print(f"{'Base Price':{name_col_width}} ${cost:{price_col_width},.2f}")
print(f"{'State Tax':{name_col_width}} ${province_tax:{price_col_width},.2f}")
print(f"{'Country Tax':{name_col_width}} ${state_tax:{price_col_width},.2f}")
print(f"{'Total':{name_col_width}} ${total:{price_col_width},.2f}")

'''
Erik:
    Good job.
'''