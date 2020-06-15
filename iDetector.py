# iDetector (Desktop version) by alombi. Version 1.0. 
# This version works only on Macs
import bs4, requests
import inquirer

print('\n\nWelcome to the desktop version of iDetector! You are running the 1.0 version, which correspond to the iOS version 1.7\n')

#Zone request
questions = [inquirer.List('zone', message = 'Choose the zone', choices = ['Argentina', 'Australia', 'Belgium', 'Brasil', 'Canada', 'Denmark', 'France', 'Germany', 'Hong Kong', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Russia', 'Spain', 'Sweden', 'UK', 'USA' ] ), ]
answers = inquirer.prompt(questions)
print(answers['zone'])

if answers['zone'] == 'Italy':
	link = 'https://downdetector.it/problemi/'
	green = 'Non problemi'
	yellow = 'Potenziali problemi'
	red = 'Problemi'
elif answers['zone'] == 'USA':
	link = 'https://downdetector.com/status/'
	green = 'No problems'
	yellow = 'Possible problems'
	red = 'Problems'
elif answers['zone'] == 'UK':
	link = 'https://downdetector.co.uk/status/'
	green = 'No problems'
	yellow = 'Possible problems'
	red = 'Problems'
elif answers['zone'] == 'France':
	link = 'https://downdetector.fr/statut/'
	green = 'Aucun problème'
	yellow = 'Panned potentielles'
	red = 'Pannes'
elif answers['zone'] == 'Germany':
	link = 'https://allestörungen.de/stoerung/'
	green = 'Keine Störung'
	yellow = 'Möglicherweise Störung'
	red = 'Störung'
elif answers['zone'] == 'Spain':
	link = 'https://downdetector.es/problemas/'
	green = 'Ninguna falla'
	yellow = 'Falla potencial'
	red = 'Falla'
elif answers['zone'] == 'Canada':
	link = 'https://downdetector.ca/status/'
	green = 'No problems'
	yellow = 'Possible problems'
	red = 'Problems'
elif answers['zone'] == 'Mexico':
	link = 'https://downdetector.mx/problemas/'
	green = 'Ninguna falla'
	yellow = 'Falla potencial'
	red = 'Falla'
elif answers['zone'] == 'Netherlands':
	link = 'https://allestoringen.nl/storing/'
	green = 'Er is geen storing bij '
	yellow = 'Mogelijke storing bij '
	red = 'Storing bij'
elif answers['zone'] == 'Portugal':
	link = 'https://downdetector.pt/fora-do-ar/'
	green = 'Nenhuma falha'
	yellow = 'Falha potencial'
	red = 'Falha'
elif answers['zone'] == 'Hong Kong':
	link = 'https://downdetector.hk/status/'
	green = 'No problems'
	yellow = 'Possible problems'
	red = 'Problems'
elif answers['zone'] == 'Australia':
	link = 'https://downdetector.com.au/status/'
	green = 'No problems'
	yellow = 'Possible problems'
	red = 'Problems'
elif answers['zone'] == 'Norway':
	link = 'https://downdetector.no/feil-problem/'
	green = 'Ingen'
	yellow = 'Mulige'
	red = 'Problemer'
elif answers['zone'] == 'Sweden':
	link = 'https://downdetector.se/problem-storningar/'
	green = 'Inga'
	yellow = 'Möjliga'
	red = 'Problem'
elif answers['zone'] == 'Denmark':
	link = 'https://downdetector.dk/problem-fejl/'
	green = 'Ingen'
	yellow = 'Problemer potentiale'
	red = 'Problemer'
elif answers['zone'] == 'Belgium':
	link = 'https://allestoringen.be/storing/'
	green = 'Er is geen storing'
	yellow = 'Mogelijke storing'
	red = 'Storing'
elif answers['zone'] == 'Brasil':
	link = 'https://downdetector.com.br/fora-do-ar/'
	green = 'Nenhuma falha'
	yellow = 'Possíveis problemas'
	red = 'Problemas'
elif answers['zone'] == 'Russia':
	link = 'https://downdetector.ru/ne-rabotaet/'
	green = 'Нет сбоя'
	yellow = 'Возможные проблемы'
	red = 'Сбои'
elif answers['zone'] == 'Poland':
	link = 'https://downdetector.pl/status/'
	green = 'Nie ma problemów'
	yellow = 'Potencjalna awaria'
	red = 'Awaria'
elif answers['zone'] == 'Japan':
	link = 'https://downdetector.jp/shougai/'
	green = '障害'
	yellow = 'に問題があるかもしれません'
	red = 'には問題がありません'
elif answers['zone'] == 'Argentina':
	link = 'https://downdetector.com.ar/problemas/'
	green = 'Ninguna falla'
	yellow = 'Falla potencial'
	red = 'Problemas'

#Service request
element = input('Enter the request: ')

#Beautiful Soup function
def Detect(url):
	req = requests.get(url)
	req.raise_for_status()
	soup = bs4.BeautifulSoup(req.text, 'html.parser')
	elems = soup.select('#company > div.card.card-body.px-2.px-md-4.pt-3.pb-4.mb-3.mr-lg-n3')
	res = elems[0].text.strip()

	#ifs loop
	if yellow in res:
		return('Potential problems reported for' + element + '.')
	elif green in res:
		return('No problems detected with ' + element + '!')
	elif red in res:
		return('We have detected some issues at ' + element + '! It may be offline.')
	else:
		return('404')

#Calling the function
status = Detect(link + element + '/')

#finally ;)
print(status)