#!/usr/bin/python

import sys

amount = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
	continue

    thisDay, thisAmount = data_mapped
    
    # if dict does not contain thisDay 
    if thisDay not in amount:
	amount[thisDay] = float(thisAmount)
    else:
	amount[thisDay] += float(thisAmount) 

for key in amount:
    print "{0}\t{1}".format(key, amount[key])
