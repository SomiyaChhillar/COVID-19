import requests 
from bs4 import BeautifulSoup 
import json


URL = "https://www.who.int/news-room/q-a-detail/q-a-coronaviruses"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') 

table = soup.find('div', attrs = {'class':'sf-accordion'})

questions = table.findAll('div', attrs = {'class':'sf-accordion__panel'})

# rows = table.findAll('tr')

data=[]
for question in questions:
	# print(q uestion)
	q = question.find('div', attrs = {'class':'sf-accordion__trigger-panel'}).a.text.strip()
	con = question.find('div', attrs = {'class':'sf-accordion__content'}).get_text()
	a = con.strip()
	print(q, a, sep='\n')

	obj = {'title':q, 'content':a}

	data.append(obj)
	
	
with open('Data/who.json', 'w') as f:
	json.dump(data, f)