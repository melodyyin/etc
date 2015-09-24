#!/usr/bin/python

import sys

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
	   continue
    # day, total sales
    thisKey, thisCount = data_mapped

    # sum the total sunday sales 
    if int(thisKey) == 6:
	   print "sum sales for sunday:", float(thisCount)
