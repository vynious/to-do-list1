import requests

endpoint = 'http://localhost:8000/tdl/'
get_response = requests.get(endpoint)
print(get_response.json())