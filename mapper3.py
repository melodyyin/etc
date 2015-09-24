#!/usr/bin/python

import sys
from datetime import datetime

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 6:
	continue
    
    day = datetime.strptime(data_mapped[0], "%Y-%m-%d").weekday()
    amount = data_mapped[4]

    print "{0}\t{1}".format(day, amount)
