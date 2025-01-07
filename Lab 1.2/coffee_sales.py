"""
Description:  Prints information about how much ov each drink, and all
               drinks in total, are sold, as well as how much money was
			   earned from sales.
Author:       Calin "Katty" Baenen
Date:         24/09/15
"""

# Column-widths.
drink_type_col_width = 15
cups_sold_col_width  = 20
price_col_width      = 13
total_col_width      = 14
padding              = 4

# How many (ov each drink) was sold.
cappuccinos_sold = int(input("How many cappuccinos were sold today? "))
coffees_sold     = int(input("How many coffees were sold today? "))
teas_sold        = int(input("How many teas were sold today? "))

# How much each drink costs.
cappuccino_price = round(float(input("How much did cappuccinos cost today? ")), 2)
coffee_price     = round(float(input("How much did coffee cost today? ")), 2)
tea_price        = round(float(input("How much did tea cost today? ")), 2)

# Earnings.
cappuccino_earnings = cappuccino_price * cappuccinos_sold 
coffee_earnings     = coffee_price * coffees_sold
tea_earnings        = tea_price * teas_sold

# Totals.
drinks_sold = cappuccinos_sold + coffees_sold + teas_sold
earnings    = cappuccino_earnings + coffee_earnings + tea_earnings

# Create preformatted strings.
# ... These price strings are absolute monsters...
#
# Because I can't use the `len()` function, I am unable to compute each
#  column's boundary, which makes it difficult to align the columns.
#
# I am aligning each thing as you tell us to, floats to the right, column
#  labels centered, and everything else on the left, but my table comes
#  out nothing like the table shown in the slides.
#
# However, despite my table looking... questionable... it technically meets
#  the critera:  dollar signs and decimal-points vertically aligned,
#  correct alignment (left, center, and right) is used for floats, strings,
#  and integers — there is no requirement stating that the content ov the
#  columns MUST be under,  or close to being under,  the label.
# There is also no requirement for the dollar signs to be near to
#  (or far from) the price – they just have to be aligned vertically.
#
# I am not really sure how to make the table look better than my tests
#  without features that haven't been discussed yet, such as `len()`,
#  for-loops, and arrays.

'''
Erik:
    It's perfectly acceptable to estimate column widths. Individual drink prices are unlikely to be more than 99.99,
    and total sales are unlikely to be more than 9,999,999.99, although I wouldn't really expect anyone to anticipate
    more than 9,999.99 for this assignment.
'''

# Row-layout format-string.
tot_row_fmt = "{:<{drink_type_col_width}}{:<{cups_sold_col_width}}{:{gap}}{:>{padding}}{:{total_col_width},.2f}"
row_fmt     = "{:<{drink_type_col_width}}{:<{cups_sold_col_width}}{:>{padding}}{:>{price_col_width},.2f}{:>{padding}}{:>{total_col_width},.2f}"

# Detailed rows.
cappuccino_row_str = row_fmt.format(
	"Cappuccino", cappuccinos_sold, '$', cappuccino_price, '$', cappuccino_earnings,
	
	drink_type_col_width = drink_type_col_width,
	cups_sold_col_width  = cups_sold_col_width,
	price_col_width      = price_col_width,
	total_col_width      = total_col_width,
	padding              = padding
)
coffee_row_str     = row_fmt.format(
	"Coffee", coffees_sold, '$', coffee_price, '$', coffee_earnings,
	
	drink_type_col_width = drink_type_col_width,
	cups_sold_col_width  = cups_sold_col_width,
	price_col_width      = price_col_width,
	total_col_width      = total_col_width,
	padding              = padding
)
tea_row_str        = row_fmt.format(
	"Tea", teas_sold, '$', tea_price, '$', tea_earnings,
	
	drink_type_col_width = drink_type_col_width,
	cups_sold_col_width  = cups_sold_col_width,
	price_col_width      = price_col_width,
	total_col_width      = total_col_width,
	padding              = padding
)

# Totals row.
total_row_str = tot_row_fmt.format(
	"Total", cappuccinos_sold+coffees_sold+teas_sold, "", '$', cappuccino_earnings+coffee_earnings+tea_earnings,
	
	drink_type_col_width = drink_type_col_width,
	cups_sold_col_width  = cups_sold_col_width,
	total_col_width      = total_col_width,
	padding              = padding,
	gap                  = price_col_width+padding
)

'''
Erik: -0.25
    With currency fields, there should be an additional column for the currency symbol so that it is not directly 
    abutting the previous column value.
    You can see an example of this on slide 18 of the lecture notes.
    
    Something I covered in the video but which didn't make it into the notes:
        DETAIL_LINE = "{:<18}{:>8}{:>6}{:>8.2f}{:>6}{:>10.2f}"
        print(DETAIL_LINE.format("Coffee", num_coffee, "$", price_coffee, "$", total_coffee))
    That can make multiple rows much easier to work with as you only have to declare the formatting once.

-------------------------

> DETAIL_LINE = "{:<18}{:>8}{:>6}{:>8.2f}{:>6}{:>10.2f}"

How come the format for `num_coffee` is right-aligned, when the slides
 specify integers have to be left-aligned?
 
 Erik: Because I either made a mistake in adapting the content or I'm mentally inconsistent. I think it's the former.

Am I missing some information?

I dunno if my table is any better, but hopefully the improvements I have
 made – with the help ov your suggestion – are at least enough to be
 considered an improvement.
The only thing I think looks funky is the Cups Sold column, which has a
 severe misalignment between its label and content.
 (But, to reiterate, there was no requirement to make the table look good – even if that is an implicit requirement in the realworld.)
 
 Erik: Agreed. There's room for interpretation. I'll call out things that I know would immediately be considered "wrong"
    in the 'real world' (such as the dollar sign issue I originally marked), but things that are more of a judgement 
    call will be ignored unless egregious (e.g., making the columns 50 characters wide). These sorts of decisions
    are tricky as it's not possible to enumerate all the possible requirements unless I require students to exactly 
    match a given output, which takes all the fun out of developing the solution (just like the real world, LOL) but I 
    imagine they can feel capricous, which I try really hard to avoid.
    
    I really enjoy these comment conversations! 
'''

# Print the table.
print(f"{'Drink Type':^{drink_type_col_width}}{'Cups Sold':^{cups_sold_col_width}}{'':{padding}}{'Price':^{price_col_width}}{'':{padding}}{'Total':^{total_col_width}}")
print(cappuccino_row_str)
print(coffee_row_str)
print(tea_row_str)
print(total_row_str)

'''
Erik:
    Looks fine! 
'''