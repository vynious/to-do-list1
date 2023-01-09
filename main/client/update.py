import requests

product_id = input('which note to update: ')

content = input('new note: ')
data= {
    content: content
}

endpoint = f'http://localhost:8000/tdl/{product_id}/update/'

get_response=requests.post(endpoint,json=data)

print(get_response.json())
