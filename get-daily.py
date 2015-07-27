### the following reads in a large (>200MB) json file and performs some analysis on the extracted data
### due to memory constraints, json file was divided into fifths, and only the relevant variables were stored
### assignment completed for COMPANY X in mid-june 
### part 1 of 4 

import bz2
import json

userids = []    # relevant vars
totals = []
hours = []
urls = []

myfile = bz2.BZ2File('daily.json.bz2')

for line in myfile:
    obj = json.loads(line)
    userids.append(obj["userid"])
    totals.append(obj["total"])
    hours.append(obj["hours"])
    urls.append(obj["buzz"])

with open("userids.txt", "w") as wf:
	for userid in userids:
		wf.write("%s\n" % userid)

with open("totals.txt", "w") as wf:
	for total in totals:
		wf.write("%d," % total)

with open("hours.txt", "w") as wf:
    for hour in hours:  # list
        for h in hour:
            wf.write("%d " % h)

with open("urls.txt", "w") as wf:
	for url in urls:
		wf.write("%s\n" % url)