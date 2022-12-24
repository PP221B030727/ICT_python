import requests
url = 'https://api.thecatapi.com/v1/images/search'
resp = requests.delete(url)
# print(resp.text )




url = 'https://cdn2.thecatapi.com/images/250.jpg'
resp = requests.get(url)
# print(resp.content)

with open(r"C:\Users\user\Desktop\ICT\week4\My Code\chek.jpg", 'wb') as file:
    file.write(resp.content)