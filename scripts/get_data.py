#!/usr/bin/python

from yahoo_finance import Share
import sys

#For this script Give input file of Stock Names and it will output to the 
#raw dataset in csv form


def dictToCSVFile(fd, share_data):

	#setup column names
	columns = []
	#loop over keys to get column names in order,
	#dicts are unordered to can't hardcode column names
	for dictionaries in share_data:
		#get every value in dict
		for key, value in dictionaries.items():
			if key not in columns:
				#Store keys in a list, then write columns to top
				columns.append(key)
	fd.write(','.join(columns) + "\n")


	#parse out the dictionaries 
	for dictionaries in share_data:
		#get every value in dict
		for key, value in dictionaries.items():
			if key not in columns:
				columns.append(key)
			#if float else treat as string
			try:
				fd.write('%f,' %float(value))
			except:
				fd.write('%s,' %value)
		fd.write('\n')
		
def main(argv):
	
	#grab filename and read through contents
	filename = str(argv[0])
	with open(filename) as f:
		company = f.readlines()
	
	#strip all the \n endings
	companies = [x.strip() for x in company]	
	
	#api pull for every company in list
	for stocks in companies:
		#gets company stock
		c_share = Share(stocks);
		#appends path to file
		filename = "../datasets/raw/" + stocks + ".csv"
		#open if doesn not already exists w+
		target_file = open( filename , "w+")
		#grab the past 15 years of data
		try:
			data = c_share.get_historical('2002-04-04', '2017-04-04')
		except:
			#visa company doesnt have public trading data before 08
			data = c_share.get_historical('2008-04-04', '2017-04-04')
		#call function to write and cleanup
		dictToCSVFile(target_file, data)
		target_file.close()




if __name__ == "__main__":
	main(sys.argv[1:])
