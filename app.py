import requests


ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN' #replace with your actual access token
LONG_URL = 'https://www.github.com/salambae' #replace your long url
API_URL = 'https://api.tinyurl.com/create' # connect to a api


headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}
data = {
    "url": LONG_URL,
    "domain": "tinyurl.com",
    "description": "string"
}
response = requests.post(API_URL, headers=headers, json=data)
if response.status_code == 200: #if response is 200, get data from json then read tiny url json 
    SHORT_URL = response.json().get('data', {}).get('tiny_url')
    print(f'Shortened URL: {SHORT_URL}') #print the url result
else:
    print(f'Error: {response.status_code}, {response.text}') #print error code