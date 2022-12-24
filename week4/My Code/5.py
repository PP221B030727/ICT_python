import requests
url = 'https://api.thecatapi.com/v1/images/search'
resp = requests.get(url,headers= {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'})
print(resp.json()[0]['id'])
print(resp.json()[0]['height'])
print(resp.json()[0]['url'])
# print(resp.text)