import requests

endpoint='http://localhost:8000/user/register/'

data = {
    'email':'shawn@gmail.com',
    'first_name':'shawn',
    'last_name':'shawn',
    'password':'',
    'password2':''
}

get_response = requests.post(endpoint,data=data)

print(get_response.json())