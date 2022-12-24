import requests

url = "https://api.polygon.io/v2/aggs/ticker/TSLA/range/1/minute/2021-07-22/2021-09-22?sort=asc&limit=5000&apiKey=lFm05uiT4LHXMiZbEQzcTCmnwZpWAJXU"
resp = requests.get(url)
print(resp.json())
