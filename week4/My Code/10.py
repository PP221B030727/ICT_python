import requests
query_param = {
    "api_key" : "DEMO_KEY",
    "earth_date": "2020-07-01"
}

resp = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos', params = query_param)
for index, data in enumerate(resp.json()['photos']):
    resp2 = requests.get(data['img_src'])
    with open(r"C:\Users\user\Desktop\ICT\week4\My Code"+ str(index) +".jpg", 'wb') as file:
        file.write(resp2.content)
