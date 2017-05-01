# DataMiningProject
Group Project for CSCI 4502

Chandler Baggett, Jacob Toomey, Dmytro Ryzhkov



# Scripts:

# get_data.py:
Uses the Yahoo Finance API to pull information from stocks specified in a txt file and puts them into a csv.
Usage: python get_data.py filename

# predict.py: 

Uses a simple Support Vector Regression model to predict a specified stock's price for a specified range of dates (DATES MUST BE CONTINUOUS WITH NO GAP, AND CAN'T INCLUDE DATES MARKET IS OPEN, MORE INFO AT TOP OF SCRIPT), and outputs them to a csv file for use with the compare script.

Usage: (DON'T INCLUDE DAYS MARKET IS CLOSED, LIKE WEEKENDS!, The example skips 20170408 and 20170409 because those are weekends)

python prediction.py filename YYYYMMDD YYYYMMDD YYYYMMDD YYYYMMDD

python predict.py aapl.csv 20170405 20170406 20170407 20170410

# compare.py: 

Uses the predicted data, and compares it to the actual data, displaying the information on a graph.
You must run predict.py before using this script to generate the csv of predicted dates. Run with a command line argument of the stock you wish to compare

Usage: python compare.py AAPL
