import requests
import json

api_url = 'http://127.0.0.1:8000/api/'

api_search = api_url + 'search/'

api_add = api_url + 'add/'

api_control = api_url + 'control/'

response = requests.get(api_search, params={'search-value':'narinji'})
print(response.status_code)
print(response.json())