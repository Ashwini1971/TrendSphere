
import requests
import json
import string
import random

# base_url
base_url = 'https://gorest.co.in'

# bearer token
bearer_token = 'Bearer 9e188a464d7f133f3bdbf3d087c3ee2e32e9a5e5953a63c5cfcd1b491f449e5b'

# Get random email id
def get_random_email_id():
    domain = 'automation.com'
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + '@' + domain
    return email

# GET
def get_request():
    url = base_url + '/public/v2/users'
    headers = {'Authorization': bearer_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_string = json.dumps(json_data, indent=4)
    print('json response body : ', json_string)
    print('.....GET user is done.....')
    print('------===============--------')

# POST
def post_request():
    url = base_url + '/public/v2/users'
    print('Post url', url)
    headers = {'Authorization': bearer_token}
    data_ = {
        "id": 7637815,
        "name": "Aswini",
        "email": get_random_email_id(),
        "gender": "female",
        "status": "inactive"
    }
    response = requests.post(url, json=data_, headers=headers)
    print(response.status_code)
    print(f"Response Content: {response.text}")
    assert response.status_code == 201
    json_data = response.json()
    json_string = json.dumps(json_data, indent=4)
    print('json response body : ', json_string)
    user_id = json_data['id']
    print('User-id ==> ', user_id)
    print('-------Created a User-------')
    assert 'name' in json_data
    assert json_data['name'] == "Aswini"
    return user_id

# PUT/PATCH
def put_request(user_id):
    url = base_url + f'/public/v2/users/{user_id}'
    print('Post url', url)
    headers = {'Authorization': bearer_token}
    data_ = {
        "id": 7637815,
        "name": "Aswini",
        "email": get_random_email_id(),
        "gender": "female",
        "status": "active"
    }
    response = requests.put(url, json=data_, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_string = json.dumps(json_data, indent=4)
    print('json PUT response body : ', json_string)
    assert json_data['id'] == user_id
    print('.....PUT user is done.....')
    print('------===============--------')

# DELETE
def delete_request(user_id):
    url = base_url + f'/public/v2/users/{user_id}'
    print('Post url', url)
    headers = {'Authorization': bearer_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print('.....DELETE user is done.....')
    print('------===============--------')


# -------------Calling-------------
get_request()
# post_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)


