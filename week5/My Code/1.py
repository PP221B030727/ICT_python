import requests 
resp = requests.get(r'https://www.python.org/static/img/python-logo.png')
with open(r'C:\Users\user\Desktop\ICT\week5\My Code\chek.png','wb') as file:
    file.write(resp.content)





