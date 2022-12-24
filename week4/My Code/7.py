import requests 
# url = "https://randomuser.me/api?gender=male"
# resp = requests.get(url)
# print(resp.text)




url = "https://randomuser.me/api?gender=male&nat=FR"
resp = requests.get(url)
print(resp.text)