from email import header
import re
import requests
# resp = requests.get(r'https://www.google.com')
# print(resp.content)
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
resp = requests.get(r'https://www.google.com',headers=headers)
print(resp.content)