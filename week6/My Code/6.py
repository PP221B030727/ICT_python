import imp
import requests
from bs4 import BeautifulSoup
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
resp = requests.get(r'https://www.accuweather.com/en/kz/almaty/222191/weather-forecast/222191',headers=headers)

soup = BeautifulSoup(resp.content)
print(soup.prettify())