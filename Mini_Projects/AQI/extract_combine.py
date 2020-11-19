"""
@author: CodeInDNA
"""

import os
import requests
import sys
import csv

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
	for idx, th in enumerate(ths):
		col_name = th.get_text()
		if idx not in [6, 10, 11, 12, 13, 14]:
			col_names.append(col_name)

	# extract rows
	for tr in trs[1:32]:
		row_td = []
		tds = tr.findAll('td')
		for idx, td in enumerate(tds):
			if idx not in [6, 10, 11, 12, 13, 14]:
				row_td.append(td.get_text())
		rows.append(row_td)


if __name__ == "__main__":
	get_data(1, 2013)