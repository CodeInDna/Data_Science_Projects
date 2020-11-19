"""
@author: CodeInDNA
"""

import os
import requests
import sys
import time

def get_html():
	for year in range(2013, 2020):
		for month in range(1, 13):
			# add 0 infront of month if it is single digit number 
			if month < 10:
				url = f"https://en.tutiempo.net/climate/0{month}-{year}/ws-427540.html"
			else:
				url = f"https://en.tutiempo.net/climate/{month}-{year}/ws-427540.html"
				
			texts = requests.get(url)
			text_utf = texts.text.encode('utf=8')

			# make dir for each year
			if not os.path.exists(f"Data/Html_Data/{year}"):
				os.makedirs(f"Data/Html_Data/{year}")

			# dump html year and month wise
			with open(f"Data/Html_Data/{year}/{month}.html", "wb") as html_file:
				html_file.write(text_utf)

		# flush the file before closing 
		sys.stdout.flush()

if __name__ == "__main__":
	start_time = time.time()
	get_html()
	end_time = time.time()
	print(f"Time Elapsed: {start_time - end_time}")