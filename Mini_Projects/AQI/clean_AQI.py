"""
@author: CodeInDNA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

def avg_aqi(year):
	file_path = f"Data/AQI/aqi{year}.csv"

	average = []
	for rows in pd.read_csv(file_path, chunksize=24):
		rows['PM2.5'] = rows['PM2.5'].apply(lambda x: float(x) if x not in ['NoData', 'PwrFail', '---', 'InVld'] else 0)
		average.append(round(np.mean(rows['PM2.5']), 2))
	return average

if __name__ == "__main__":
	start_time = time.time()
	avg_aqi2013 = avg_aqi(2013)
	avg_aqi2014 = avg_aqi(2014)
	avg_aqi2015 = avg_aqi(2015)
	avg_aqi2016 = avg_aqi(2016)
	avg_aqi2017 = avg_aqi(2017)
	avg_aqi2018 = avg_aqi(2018)
	plt.plot(range(0, 365), avg_aqi2013, label="2013 Data")
	plt.plot(range(0, 364), avg_aqi2014, label="2014 Data")
	plt.plot(range(0, 365), avg_aqi2015, label="2015 Data")
	plt.xlabel("Day")
	plt.ylabel("PM 2.5")
	plt.legend(loc='upper right')
	plt.show();
	end_time = time.time()
	print(f"Time Elapsed: {end_time - start_time}")


