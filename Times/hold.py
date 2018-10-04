# Extracts the hold times and latencies and stores them in corresponding
# folders in Parent/Hold Times and Parent/Latencies folder (make sure these
# empty folders are present)

import os
from datetime import datetime

# 1.txt contains the keyboard data
f = open('1.txt','r')
f_list = f.readlines()
f_list = [x[:-1] for x in f_list]
if f_list[-1]=='\n':
	f_list.pop()

# Extracting the timestamp and key
tstamp =  [item[-23:-2] for item in f_list]
tstamp =  [s + '000' for s in tstamp]
letter =  [item[-25] for item in f_list]

for i in range(0,len(f_list)-2,2):
	# Calculating the differences
	t1 = datetime.strptime(tstamp[i], "%d:%m:%y:%H:%M:%S:%f")
	t2 = datetime.strptime(tstamp[i+1], "%d:%m:%y:%H:%M:%S:%f")
	t3 = datetime.strptime(tstamp[i+2], "%d:%m:%y:%H:%M:%S:%f")
	hold_time = t2-t1
	hold_time = hold_time.total_seconds()
	latency = t3-t2
	latency = latency.total_seconds()
	f = open("Hold Times/" + letter[i] + ".txt", "a+")
	f.write(str(hold_time) + "\n")	
	f.close()
	f = open("Latencies/"+letter[i+1] + letter[i+2] + ".txt", "a+")
	f.write(str(latency) + "\n")	
	f.close()
