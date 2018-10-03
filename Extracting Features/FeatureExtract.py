# Stores the list of input points with respect to the features mentioned in a file
# The remaining files in the folder are for running a toy example. 
# common_feat.txt contains the list of common features
# Hold times and Latencies folders contain the respective times for a user

import itertools
import os

# The common features file feat_names.txt contains features as strings, one per line
f = open('common_feat.txt','r')
f_list = f.readlines()
f_list = [x[:-1] for x in f_list]
if f_list[-1]=='\n':
	f_list.pop()
# f_list contains common features

# Extracting the hold times and latencies from the files
hold_list = os.listdir('Hold Times')
lat_list = os.listdir('Latencies')
total_list = hold_list + lat_list
# Common feature
total_list = [x for x in f_list if x in total_list]

# List of lists of latencies and hold times
l = []

# Parsing the files to generate l
for x in total_list:
	inner_list = []
	try:
		with open('Hold Times/'+x) as f:
			for line in f:
				try:
					inner_list.append([float(elt.strip()) for elt in line.split(' ')])
				except:
					continue
		inner_list = [item for sublist in inner_list for item in sublist]
		l.append(inner_list)
	except:
		with open('Latencies/'+x) as f:
			for line in f:
				try:
					inner_list.append([float(elt.strip()) for elt in line.split(' ')])
				except:
					continue
		inner_list = [item for sublist in inner_list for item in sublist]
		l.append(inner_list)

# Generating the feature vector
feat_vec = map(list,list(itertools.product(*l)))
