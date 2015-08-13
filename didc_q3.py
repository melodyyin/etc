from bs4 import BeautifulSoup
import urllib2 

pagesf = "C:/Users/MelodyYin/Desktop/pages.txt"
with open(pagesf) as f:
	pages = f.readlines()

names = []
basics = []
comments = []
lipies = []

for p in pages:
	page = urllib2.urlopen(p.rstrip())
	soup = BeautifulSoup(page)
	
	nm = soup.find_all("h1")	# not all are relevant
	impt = soup.find_all("div", class_="important")
	cmt = soup.find_all("div", class_="comment-content")
	lip = soup.find_all("div", class_="lipies")

	for n in nm:
		ntext = n.get_text()
		if len(ntext) > 0:
			for rep in impt: # repeat for number of reviews 
				names.append(ntext)
				
	for i in impt: 
		basics.append(i.get_text().encode('utf-8').strip())

	for c in cmt: 
		newc = c.get_text().encode('utf-8').replace("\t", "").replace("\n", " ").strip()
		comments.append(newc)

	for l in lip:
		lipies.append(int(l.find("span").get("class")[0][2]))

# save separately
with open("names.txt", "w") as wf:
	for name in names: 
		wf.write("%s\n" % name)

with open("basics.txt", "w") as wf:
	for basic in basics:
		wf.write("%s\n" % basic)

with open("comments.txt", "w") as wf:
	for comment in comments:
		wf.write("%s\n" % comment)

with open("lipies.txt", "w") as wf:
	for lipie in lipies:
		wf.write("%d\n" % lipie)
