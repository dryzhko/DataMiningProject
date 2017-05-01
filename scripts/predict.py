#TO USE: run with CSV file as a command line argument, followed by the dates you want predicted in YYYYMMDD format
#example: python predict.py aapl.csv 20170405 20170406 20170407

#The script will output a CSV of the date and the prediction on that date, that is used by the compare script to compare
#to the actual prices on that date

#This script uses Support Vector Regression in order to predict the stock price of a stock on a certain day
#The original data will be plotted, with the model over it, and the prediction will be printed to the terminal

#Originally had RBF, Linear, and Polynomial Models, after testing them RBF was the only one that worked, so the
#others are commented out

import sys
import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt



marketDates = []
marketPrices = [] #closing price
filename = sys.argv[1]
outputDates = filename.split('.')[0] + "output.csv"
inputDates = sys.argv[2:]



def readData(name):
	with open(name, 'r') as csvfile:
		reader = csv.reader(csvfile)
		next(reader)
		for row in reader:
			marketDates.append(int(row[5].replace('-', '')))
			marketPrices.append(float(row[6]))
	csvfile.close()
	return

def formatDate(date):
	formatedDate = date[:4] + '-' + date[4:6] + '-' + date[6:]
	return formatedDate

def prediction(date, prices, x):
	dates = np.reshape(date, (len(date), 1))
	#SVRlin = SVR(kernel = 'linear', C=1e3)
	#SVRpoly = SVR(kernel = 'poly', C=1e3, degree = 2)
	SVRrbf = SVR(kernel = 'rbf', C=1e3, gamma=0.1) #Creating the model and fitting it to the prices
	print "Creating RBF model... (This takes a while)"
	SVRrbf.fit(dates, prices)
	#SVRpoly.fit(dates,prices)
	#SVRlin.fit(dates,prices)
	plt.scatter(dates, prices,  label = 'Data') #plotting the data and the model
	plt.plot(dates, SVRrbf.predict(dates), color='red', label = 'RBF model')
	#plt.plot(dates, SVRlin.predict(dates), color='green', label = 'Linear model')
	#plt.plot(dates, SVRpoly.predict(dates), color='blue', label = 'Polynomial model')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Support Vector Regression')
	plt.legend()
	output = open(outputDates, "w")
	for date in x:
		print"The predicted price on " + formatDate(str(date)) + " is " + str(SVRrbf.predict(date)[0])
		output.write(date + "," + str(SVRrbf.predict(date)[0]) + "\n")
	
	output.close()
	plt.show()
	
	#return SVRrbf.predict(x)[0], SVRlin.predict(x)[0], SVRpoly.predict(x)[0]
	return SVRrbf.predict(x)[0]
	


readData(filename)
prediction(marketDates, marketPrices, inputDates)




