import requests


endpoint = 'http://localhost:8000/tdl/create/'


data = {
    'priority':'L',
    'content': 'study stats'
}

get_response = requests.post(endpoint,data=data)

print(get_response.json())
