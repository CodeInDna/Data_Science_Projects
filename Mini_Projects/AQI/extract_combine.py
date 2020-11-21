"""
@author: CodeInDNA
"""
from clean_AQI import avg_aqi
import os
import requests
import sys
import csv
import glob

from bs4 import BeautifulSoup
import pandas as pd

def get_data(month, year):
	col_names = []
	rows = []
	html = open(f"Data/Html_Data/{year}/{month}.html")
	html_text = html.read()

	soup = BeautifulSoup(html_text, "html.parser")

	table = soup.find('table', {'class': 'medias mensuales numspan'})
	trs = table.findAll('tr')

	ths = trs[0].findAll('th')

	# extract column names
	# for idx, th in enumerate(ths):
	# 	col_name = th.get_text()
	# 	if idx not in [6, 10, 11, 12, 13, 14]:
	# 		col_names.append(col_name)

	# extract rows
	for tr in trs[1:-2]:
		row_td = []
		tds = tr.findAll('td')
		for idx, td in enumerate(tds):
			if idx not in [0, 4, 10, 11, 12, 13, 14]:
				row_td.append(td.get_text())
		rows.append(row_td)

	return rows


if __name__ == "__main__":
	if not os.path.exists("Data/Final_Data"):
		os.makedirs("Data/Final_Data")

	# for year in range(2013, 2019):
	# 	final_data = []

	# 	for month in range(1, 13):
	# 		final_data += get_data(month, year)

	# 	df = pd.DataFrame(final_data, columns=['T', 'TM', 'Tm', 'H', 'PP' , 'VV', 'V', 'VM'])

	# 	df = df[~df.isin(["", "-"]).any(axis=1)]

	# 	df['PM2.5'] = pd.Series(avg_aqi(year))[df.index]

		# df.to_csv(f'Data/Final_Data/{year}.csv', index=False)

	
	files = glob.glob('Data/Final_Data/*.csv')
	dfs = []

	for file in files:
		dfs.append(pd.read_csv(file, index_col=None, header=0))

	df = pd.concat(dfs, axis=0, ignore_index=True)

	print(df.head(200))


