import requests
resp = requests.get("https://api.thecatapi.com/v1/images/search")
print(resp.url)
print(resp.status_code)
print(resp.reason)
print(resp.headers)