from email import header
from bs4 import BeautifulSoup
import requests
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
resp = requests.get('https://news.google.com/search?q=microsoft', headers = headers)
# print(resp.content)
soup = BeautifulSoup(resp.content)
# print(soup.prettify())
# print(soup.text)

# for i in soup.find_all('a', class_ = "DY5T1d RZIKme"):
#     print(i.text)




# import datetime
# for i in soup.find_all('time', class_ = "WW6dff uQIVzc Sksgp slhocf"):
#     print(datetime.datetime.strptime(i['datetime'], "%Y-%m-%dT%H:%M:%SZ"))





links = []
for i in soup.find_all('a', class_ = "DY5T1d RZIKme"):
    links.append("https://news.google.com" + i['href'][1:])
# print(links[0])
resp = requests.get(links[0], headers = headers)
# print(resp.content)
# soup = BeautifulSoup(resp.content)
# print(soup.find('a', jsname = "tljFtd").text)
print(links)




