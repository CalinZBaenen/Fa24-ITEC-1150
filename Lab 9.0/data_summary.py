"""
Description:  A program which summarizes the data in `ch_9_lab_data.txt`.
Author:       Calin "Katty" Baenen
Date:         24/11/18
"""
from table import Table





def main():
	error_ct = 0
	num_ct   = 0
	table    = Table()
	total    = 0
	nums     = list()
	
	f = open("ch_9_lab_data.txt", 'r')
	lines = f.readlines()
	f.close()
	
	for line in lines:
		try:
			num = int(line)
			
			num_ct += 1
			total += num
			nums.append(num)
		except:
			error_ct += 1
	
	avg = total/num_ct
	
	table.add_row(["#/Numbers", "#/Unique Numbers", "#/Unrecognized Numbers", "Sum", "Average"])
	table.add_row([num_ct, len(set(nums)), error_ct, total, avg])
	
	# The numbers are technically right and left aligned, like you asked1
	# ... Even if that's not admittedly apparent.
	#
	# For some reason, Python's string alignment formatting isn't playing
	#  nice, despite me doing similar things with it in the past(???).
	print(table)
	f = open("summary.txt", "w+")
	f.write(str(table))
	f.close()

if __name__ == "__main__":
	main()

'''
Erik:
    Ha! I might add "get a count of unique numbers" for next semester. Surprised it's a round 5K.
'''