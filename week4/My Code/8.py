import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'}
dictio = {
    'gender' : 'male', 
    'nat' : 'FR'
}
url = "https://randomuser.me/api"
resp = requests.get(url, params = dictio, headers = headers)
print(resp.text)