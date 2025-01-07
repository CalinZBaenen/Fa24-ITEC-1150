"""
Description:  A program that reports to the user how much money their
                (heterogeneous) collection ov coins is worth.
Author:       Calin "Katty" Baenen
Date:         24/09/10
"""

stop_point = ""
quarters   = ""
errored    = False
nickels    = ""
pennies    = ""
dimes      = ""

quarters = input("How many quarters do you have? ")
if not quarters.isnumeric():
	stop_point = "quarters"
	errored    = True

if not errored:
	dimes = input("How many dimes do you have? ")
	if not dimes.isnumeric():
		stop_point = "dimes"
		errored    = True

if not errored:
	nickels = input("How many nickels do you have? ")
	if not nickels.isnumeric():
		stop_point = "nickels"
		errored    = True

if not errored:
	pennies = input("How many pennies do you have? ")
	if not pennies.isnumeric():
		stop_point = "pennies"
		errored    = True

if not errored:
	msg = ""
	
	b_dim = int(dimes)/10
	b_nic = int(nickels)/20
	b_pen = int(pennies)/100
	b_qua = int(quarters)/4
	'''
	Erik:
	    Clever. Took me a second.
	'''
	
	bal = b_qua+b_dim+b_nic+b_pen
	
	if bal > 10:
		msg = "You have over $10.00!"
	elif bal == 10:
		msg = "You have exactly $10.00."
	else:
		msg = "You have under $10.00."
	
	print()
	
	print("-------------------------")
	print(msg)
	
	msg = "{:<9}     {:>10}     ${:>10.2f}"
	print( msg.format("Quarters:", int(quarters), b_qua) )
	print( msg.format("Dimes:", int(dimes), b_dim) )
	print( msg.format("Nickels:", int(nickels), b_nic) )
	print( msg.format("Pennies:", int(pennies), b_pen) )
	
	msg = f"Total:                       ${bal:>10.2f}"
	print(msg)
	print("-------------------------")
else:
	print(f"The program failed because unexpected input was given when asked about {stop_point}.")