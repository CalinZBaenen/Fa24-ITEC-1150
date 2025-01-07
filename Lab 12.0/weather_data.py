"""
Description:  Downloads a weather-forecase page from a given URL and prints
               the weather in the form ov a table.
Author:       Calin "Katty" Baenen
Date:         24/12/06
"""
import pyinputplus as pyip
import geocoder
import requests

from geocoder.ipinfo import IpinfoQuery
from bs4             import BeautifulSoup as Soup





def main() -> int:
	try:
		while True:
			print("Enter a URL to a weather-forecast.")
			parser = None
			site   = pyip.inputURL("> ", blank=True)
			
			if site == "":
				lctn = geocoder.ip("me")
				lctn = lctn.latlng if type(lctn) is IpinfoQuery else [0, 0]
				site = f"https://forecast.weather.gov/MapClick.php?lat={lctn[0]}&lon={lctn[1]}"
				print(f"No URL was entered, would you like to use the National Weather Service?\n ({site})")
				
				if pyip.inputYesNo("[y / n] ") != "yes":
					continue
			
			# Make the request and test the status-code.
			res = requests.get(site)
			match res.status_code:
				# Match a successful response.
				case 200:
					parser = Soup(res.text, "html.parser")
				
				# Handle any possible errors.
				case status:
					print(f"There was a ({status}) error loading your text document.")
					return 2
			
			# Check if the parser was made.
			if parser is None:
				return 2
			
			# Get the forecast labels and texts.
			forecast_labels = parser.select(".forecast-label")
			forecast_texts  = parser.select(".forecast-text")
			
			# Check for forecast data.
			if len(forecast_labels) < 1 or len(forecast_texts) < 1:
				print("There does not seem to be any forecast data here...\n... Please try again.")
				'''
				Erik:
				    If there is no data in your lists, print an error message and have the user try again.
				    You printed the error, but the program exited.
				
				-------------------------
				
				Calin:
				    Huh.
				    Man, my code's (been) lackin'.
				
				-------------------------
				
				Erik:
				    Catching all the details in requirements is a challenge when you're looking at a bigger picture (as
				    you are with the additional features).
				'''
				continue
			
			# Get the longest label and text lengths.
			lng_label = 0
			lng_txt   = 0
			for label in forecast_labels:
				l = len(label.text)
				if l > lng_label:
					lng_label = l
			for text in forecast_texts:
				l = len(text.text)
				if l > lng_txt:
					lng_txt = l
			
			# Print the labels and the texts.
			for (label, text) in zip(forecast_labels, forecast_texts):
				print(f"{label.text: <{lng_label}} {text.text: ^{lng_txt}}")
			
			# Offer the user to run the program again.
			print("Would you like to show weather from another URL?")
			if pyip.inputYesNo("[y / N] ", default="no", limit=1) != "yes":
				break
	
	except ConnectionError:
		print("There was an error connecting to the website at the provided URL...")
		return 2
	
	except Exception as e:
		print(f"An unexpected error ({type(e)}) occured.")
		return 1
	
	return 0

if __name__ == "__main__":
	exit(main())