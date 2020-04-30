import requests 
from bs4 import BeautifulSoup 
import json


URLs = ["https://www.who.int/news-room/q-a-detail/q-a-coronaviruses", 
		'https://www.who.int/news-room/q-a-detail/q-a-on-covid-19-and-pregnancy-and-childbirth',
		'https://www.who.int/news-room/q-a-detail/q-a-on-covid-19-and-breastfeeding',
		'https://www.who.int/news-room/q-a-detail/q-a-on-covid-19-and-masks',
		'https://www.who.int/news-room/q-a-detail/q-a-on-covid-19-hiv-and-antiretrovirals',
		'https://www.who.int/news-room/q-a-detail/q-a-similarities-and-differences-covid-19-and-influenza',
		'https://www.who.int/news-room/q-a-detail/q-a-on-mass-gatherings-and-covid-19',
		'https://www.who.int/news-room/q-a-detail/q-a-on-infection-prevention-and-control-for-health-care-workers-caring-for-patients-with-suspected-or-confirmed-2019-ncov',
		'https://www.who.int/news-room/q-a-detail/q-a-on-smoking-and-covid-19#',
		'https://www.who.int/news-room/q-a-detail/be-active-during-covid-19',
		'https://www.who.int/news-room/q-a-detail/malaria-and-the-covid-19-pandemic',
		'https://www.who.int/news-room/q-a-detail/violence-against-women-during-covid-19',
		'https://www.who.int/news-room/q-a-detail/contraception-family-planning-and-covid-19'
		]
data=[]		
for URL in URLs:
	r = requests.get(URL) 

	soup = BeautifulSoup(r.content, 'html5lib') 

	table = soup.find('div', attrs = {'class':'sf-accordion'})

	questions = table.findAll('div', attrs = {'class':'sf-accordion__panel'})

	# rows = table.findAll('tr')


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