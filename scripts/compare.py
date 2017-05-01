#READ GUIDLINE IN predict.py TO MAKE SURE YOUR DATA WORKS WITH THIS SCRIPT
#MUST GENERATE OUTPUT FILE BEFORE USING, OUTPUT FILE MUST MEET SPECIFICATIONS IN predict.py

#This script takes the prices that you predicted for your range of dates for a given stock,
#and compares them to the actual prices on those days
#to use, command line argument of stock you wish to compare
#USAGE: python compare.py AAPL

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from yahoo_finance import Share

stock = sys.argv[1]

dates = []
predictedPrices = []
actualPrices = []

filename = stock + "output.csv"

#pull dates and prices from csv of predicted prices
def readData(filename):
	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			dates.append(int(row[0]))
			predictedPrices.append(float(row[1]))
	csvfile.close()
	return

#pull actual prices on those dates using yahoo finance api
def getActual(stock):
	c_share = Share(stock);
	oldestDate =  str(dates[0])[:4] + '-' + str(dates[0])[4:6] + '-' + str(dates[0])[6:]
	newestDate =  str(dates[-1])[:4] + '-' + str(dates[-1])[4:6] + '-' + str(dates[-1])[6:]
	data = c_share.get_historical(str(oldestDate), str(newestDate))
	#data = c_share.get_historical('2017-04-05', '2017-04-28')
	for date in data:
		for key in date:
			if key == "Close":
				actualPrices.insert(0, float(date[key]))

#plot the results			
def compare():
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Predicted Prices vs. Actual Prices of ' + stock)
	plt.scatter(dates, predictedPrices, color="red", label = "Predicted Prices")
	plt.scatter(dates, actualPrices, color="blue", label = "Actual Prices")
	plt.legend()
	plt.show()

readData(filename)
getActual(stock)
compare()

