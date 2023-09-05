import json

import jsonpath
import requests
import pytest

# Assuming your API base URL
BASE_URL = "https://reqres.in/api"


@pytest.fixture
def new_user_data():
    # Define the data for creating a new user
    return {
    "name": "Akshay",
    "job": "Automation Engineer"
}


def test_create_user(new_user_data):
    url = f"{BASE_URL}/users"

    response = requests.post(url, json=new_user_data)
    print(response.content)
    assert response.status_code == 201  # Assuming successful creation

#    parse rseponse to json format
    json_response = json.loads(response.text)
    print(json_response)

#     pick the id
    id = jsonpath.jsonpath(json_response,'id')
    print(id[0])



