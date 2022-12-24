import requests
resp = requests.get(r'https://www.google.com')
print(resp.content)