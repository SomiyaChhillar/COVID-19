import requests 
from bs4 import BeautifulSoup 
import json


#MoHFW website
URL = "https://www.mohfw.gov.in/"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') 

table = soup.find('table', attrs = {'class':'table table-striped'})

rows = table.findAll('tr')

print(len(rows))

data = []
for i in range(1,33):
	state = rows[i].findAll('td')
	
	name = state[1].text
	total = state[2].text
	cured = state[3].text
	death = state[4].text
	
	obj = {"state":name, "total_cases":total, "cured":cured, "death":death}
	data.append(obj)

with open('data.json', 'w') as f:
	json.dump(data, f)


