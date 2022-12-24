import requests
query_param = {
    "api_key" : "DEMO_KEY",
    "earth_date": "2020-07-01"
}

resp = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos', params = query_param)
# print(resp.text)
for i in resp.json()['photos']:
    print(i['img_src'])





