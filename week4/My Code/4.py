import requests
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
url = 'https://api.thecatapi.com/v1/images/search'
resp = requests.get(url, headers = headers)
print(resp.request.headers)