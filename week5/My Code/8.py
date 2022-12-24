import requests
import datetime
url = 'https://news.google.com/search?q=tesla&hl=en-US&gl=US&ceid=US%3Aen'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0', 'Accept-Language' : 'en-GB,en;q=0.5'}

resp = requests.get(url, headers = headers)
print(resp.text)
