import csv
import numpy as np
import matplotlib.pyplot as plt

dates = []
predictedPrices = []
actualPrices = [144.02, 143.66, 143.34, 143.17, 141.63, 141.80, 141.05, 141.83, 141.20, 141.68, 141.44, 142.27, 143.64, 144.53, 143.68, 143.79, 143.65]
filename = "AAPLoutput.csv"

def readData(filename):
	with open(filename, 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			dates.append(int(row[0]))
			predictedPrices.append(float(row[1]))
	csvfile.close()
	return

def compare():
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Predicted Prices vs. Actual Prices of AAPL')
	plt.scatter(dates, predictedPrices, color="red", label = "Predicted Prices")
	plt.scatter(dates, actualPrices, color="blue", label = "Actual Prices")
	plt.legend()
	plt.show()

readData(filename)
compare()
