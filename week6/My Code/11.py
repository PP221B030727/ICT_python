import requests 
from bs4 import BeautifulSoup 
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://www.accuweather.com/en/kz/almaty/222191/weather-forecast/222191', headers = headers)
soup = BeautifulSoup(resp.content, 'html.parser')

# print(soup.find_all('div', id = 'bottom'))
# print(soup.find_all('div', class_ = 'page-subnav'))

# print(soup.find_all('div', attrs))

attrs = {'class' : 'header-citsy-link'}
print(soup.find_all('a', attrs)[0]['href'])
