import requests


endpoint = 'http://localhost:8000/tdl/create/'


data = {
    'priority':'L',
    'content': 'study dm'
}

get_response = requests.post(endpoint,data=data) # data that is sent 

print(get_response.json())
