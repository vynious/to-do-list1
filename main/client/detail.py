import requests

product_id = input('which id to view: ')

endpoint = f'http://localhost:8000/tdl/{product_id}/'

get_response = requests.get(endpoint)

print(get_response.json())