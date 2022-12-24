# import requests
# headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
# resp = requests.get('https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1633297421&period2=1664833421&interval=1d&events=history&includeAdjustedClose=true', 
#                     headers = headers)
# print(resp.content)




import requests
url = r'https://www.howtogeek.com/wp-content/uploads/2016/10/img_57f5530e67aec.png?trim=1,1&bg-color=000&pad=1,1'
with open(r'C:\Users\user\Desktop\ICT\week5\My Code\chek2.png','wb') as file:
    file.write(requests.get(url).content)