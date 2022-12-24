import requests
from bs4 import BeautifulSoup
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://www.accuweather.com/en/kz/almaty/222191/weather-forecast/222191', headers = headers)
soup = BeautifulSoup(resp.content, 'html.parser')
# for desc in soup.body.div.descendants:
#     print(desc)
# print(soup.body.div.header.contents)
# print(soup.body.div.header.h1.string)
print(soup.div.header.div.find_all('a'))
