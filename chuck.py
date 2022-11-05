import requests
import json
from pprint import pprint

url = "https://api.chucknorris.io/jokes/random"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

responseJson = response.json()

pprint(response.text)
