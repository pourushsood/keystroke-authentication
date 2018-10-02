# Stores the list of input points with respect to the features mentioned in a file

import itertools

l = []
with open('data.txt') as f:
	for line in f:
		try:
			inner_list = [float(elt.strip()) for elt in line.split(' ')]
			l.append(inner_list)
		except:
			continue

feat_vec = map(list,list(itertools.product(*l)))