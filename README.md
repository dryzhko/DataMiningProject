# DataMiningProject
Group Project for CSCI 4502

Chandler Baggett, Jacob Toomey, Dmytro Ryzhkov



Scripts:

get_data.py: Uses the Yahoo Finance API to pull information from stocks specified in a txt file and puts them into a csv.
Usage: python get_data.py filename

predict.py: Uses a simple Support Vector Regression model to predict a specified stock's price for a specified range of dates (put in whichever dates you want as command line arguments in format YYYYMMDD), and outputs them to a csv file for use with the compare script.
Usage: python prediction.py filename YYYYMMDD YYYYMMDD YYYYMMDD

compare.py: Uses the predicted data, and compares it to the actual data, displaying the information on a graph.
Usage: python compare.py
