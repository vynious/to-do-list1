import requests


product_id = input('which id to delete: ')

endpoint = f'http://localhost:8000/tdl/{product_id}/delete/'

get_response = requests.delete(endpoint)

print(get_response.status_code, get_response.status_code==204)