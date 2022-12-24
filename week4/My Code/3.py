import requests
# resp = requests.get("https://api.thecatapi.com/images/searc")
# print(resp.text)



resp = requests.get("https://api.thecatapi.com/v1/images/search")
print(resp.request.headers)
print(resp.headers)