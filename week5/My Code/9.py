from email import header
from bs4 import BeautifulSoup
import requests
import datetime
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0', 'Accept-Language' : 'en-GB,en;q=0.5'}

page = requests.get('https://news.google.com/search?q=tesla&hl=en-US&gl=US&ceid=US%3Aen',
                    headers = headers)
# print(page.content)
bs = BeautifulSoup(page.content)
print(bs.find_all('h3')[10].string)
for i in bs.find_all('h3'):
    print(i.string)