from typing import Any





class Table:
	data:list[list[Any]]
	
	def __init__(self):
		self.data = list()
	
	def add_row(self, row:list[Any]):
		self.data.append(row)

	def __repr__(self):
		# Calculate the width ov each column, accounting for linebreaks.
		#  1. Master list-comprehension contains multiple
		#      list-comprehensions A, B, and C
		#      (according to the order they appear).
		#  2. List-comprehension A inserts the length ov the (stringified)
		#      cell in a column, or zero if it's missing from the table's
		#      "tail".
		#  3. List-comprehension B – used for list-comprehension A – gets
		#      the longest row's length (in columns).
		#  4. List-comprehension C – used for list-comprehension A – runs
		#      the other two comprehensions for however many rows are
		#      present.
		#
		# This explanation is for both ov our sakes.
		# ... This line ov code is a nightmare to look at.
		col_widths = [
			[
				max(
					list(map(lambda s: len(s), str(self.data[ri][c]).splitlines()) if c < len(self.data[ri]) else [0])
				) for c in range(max( *[len(r) for r in self.data] ))
			 ] for ri in range(len(self.data))
		]
		
		# Calculate the height ov each row.
		# row_heights = [max(len(str(cell).splitlines()) for cell in row) for row in self.data]
		
		# Make borders for each section (top, middle, bottom).
		# bottom_border = '└' + '┴'.join('─' * max(w) for w in zip(*col_widths)) + '┘'
		# mid_border    = '├' + '┼'.join('─' * max(w) for w in zip(*col_widths)) + '┤'
		# top_border    = '┌' + '┬'.join('─' * max(w) for w in zip(*col_widths)) + '┐'
		
		# Construct all data rows with box-drawing lines between them
		# table_repr = [top_border]
		# r          = 0
		# while r < len(self.data):
		# 	h = row_heights[r]
		#
		# 	row_repr = '│' + '│'.join(f"{cell: >{w}}" if (type(cell) is int or type(cell) is float) else f"{cell:{w}}" for cell, w in zip(self.data[r], col_widths[r])) + '│'
		# 	while len(row_repr.splitlines()) < h:
		# 		row_repr += "\n│" + '│'.join([' '*w for w in col_widths[r]]) + '│'
		# 	table_repr.append(row_repr)
		# 	table_repr.append(mid_border)
		#
		# 	r += 1
		
		# Remove the last added mid-border and add the bottom border
		# table_repr = table_repr[:-1] + [bottom_border]
		
		table_repr = []
		for ri in range(len(self.data)):
			row_repr = ' '.join([f"{cell: >{w}}" if isinstance(cell, (float, int)) else f"{cell: <{w}}" for cell, w in zip(self.data[ri], col_widths[ri])])
			table_repr.append(row_repr)
		
		return '\n'.join(table_repr)