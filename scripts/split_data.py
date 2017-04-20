#!/usr/local/bin/python3

#----Splits Data between test and training given data given date  YYYY-MM-DD from /raw/ dataset
#----example: python3 split_data.py 2014-07-14
#
#
#

import sys
import csv
import os
from datetime import datetime
#libraries




def directory_itter(split_date):
	

	#define all paths and sets	
	source_path = "../datasets/raw/"
	test_path = "../datasets/test/"
	train_path = "../datasets/train/"
	split_date = datetime.strptime(split_date, "%Y-%m-%d")
	test_set = []
	train_set = []

	#go through every file in ../datasets/raw
	for files in os.listdir(source_path):
		with open(source_path + files, 'r') as fd:
			#convert file into csv and skip head 
			read_file = csv.reader(fd)
			next(read_file)
			
			#compare dates of all rows and append to appropriate sets
			for row in read_file:
				compare_date = datetime.strptime(row[1], "%Y-%m-%d")
				if compare_date > split_date:
					test_set.append(row)
				else:
					train_set.append(row)
			
			#write test set to file
			with open(test_path + files, 'w+') as test_file:
				test_csv = csv.writer(test_file)
				test_csv.writerow(["Symbol","Date","Open","High","Low","Close","Volume","Adj_Close"])
				for row in test_set:
					test_csv.writerow(row)
			
			#write train set to file
			with open(train_path + files, 'w+') as train_file:
				train_csv = csv.writer(train_file)
				train_csv.writerow(["Symbol","Date","Open","High","Low","Close","Volume","Adj_Close"])
				for row in train_set:
					train_csv.writerow(row)
			train_set[:] = []
			test_set[:] = []		
			
def main(argv):
	
	if len(argv) > 1:
		print("Error too many arguments")
		exit(1)

	split_date = str(argv[0])
	directory_itter(split_date)
			
	return 0

if __name__ == "__main__":
	main(sys.argv[1:])

