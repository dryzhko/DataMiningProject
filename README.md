# Predicting Stock Prices
Group Project for CSCI 4502

Chandler Baggett, Jacob Toomey, Dmytro Ryzhkov


# Project Description

We wanted to utilize machine learning in order to try and predict stock market prices. We mined historical prices for
various stocks using the Yahoo Finance API, and used Support Vector Regression in Scikit-Learn in order to create a model that would be used to predict prices on certain dates. These predicted prices were then compared to the actual prices on the given dates, to determine how accurate our predictions were, and whether or not it is feasible to predict the stock market using a machine learning model.


# Questions and Answers

Can you effectively use machine learning in order to predict prices in the stock market?


The stock market is volatile and unpredictable, and attempting to predict the prices of future stocks using only historical price data did not give us very accurate results. There are a multitude of outside factors that influence the the market that our model does not account for.



# Applications

While we did not get the most accurate prices, our model was able to accurately predict the behavior of the stock market. When there are no major outside influences, stocks tend to remain at a fairly even level, and our model demonstrated this. This knowledge can be applied in many different ways. It can be applied for stock market research, more specifically research regardign what sorts of events break this behaviour, and cause steady prices to either fluctuate, skyrocket, or plummet. Our findings can also be applied to developing a more advanced model, one that uses techniques like sentiment analysis in order to factor in outside forces and provide for a more accurate prediction.



# Video Demonstration

http://www.screencast.com/t/6Cxg1LgweN



# Final Paper

https://docs.google.com/document/d/1rHo3U0LdOX9gOegAQOq-gGW8XA0KQutzE78RYGUT3NE/edit?usp=sharing



# Scripts

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
