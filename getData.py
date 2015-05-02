import csv
from Init import *

def getData(filename):
	read = csv.reader(open(filename, "rU"));
	print read;
	data = list();
	first = 1;
	for row in read:
		#print row
		if (first):
			first = 0;
			continue;
		l = len(row);
		tmp = dict();
		for i in range(l):
			tmp[Name[i]] = float(row[i])
		data.append(tmp);
	return data;
