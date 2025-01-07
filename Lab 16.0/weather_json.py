"""
Description:  Opens a weather forecast file that's written in JSON and
               prints some info about the weather.
Author:       Calin "Katty" Baenen
Date:         24/11/25
"""
import json

from pathlib import Path





# [M]ain
def main() -> int:
	paths = [Path("lab_16_forecast.json"), Path("forecast.json")]
	db    = None
	
	# Iterate the possible paths you could get a forecast from, then choose
	#  the first valid file.
	for p in paths:
		if p.exists() and p.is_file():
			db = open(p, 'r')
			break
	# Report an error to the user if no forecast file exists.
	if db is None:
		print("There is no (locally) stored forecast data to show you...")
		return 1
	
	# Load the forecast, then print the info for each period in it.
	forecast = json.loads(db.read())
	llbl     = 0
	ltxt     = 0
	for day_info in forecast["periods"]:
		lbll = len( str(day_info["name"]) )
		txtl = len( str(day_info["detailedForecast"]) )
		
		if lbll > llbl:
			llbl = lbll
		if txtl > ltxt:
			ltxt = txtl
	for day_info in forecast["periods"]:
		print(f"{day_info['name']: <{llbl}}   {day_info['detailedForecast']: ^{ltxt}}")
	
	return 0

if __name__ == "__main__":
	exit(main())

'''
Erik:
    Nice job.
'''