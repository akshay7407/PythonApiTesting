import json

import jsonpath
import requests
import pytest

@pytest.fixture(scope='module')
def start_exec():
    global url
    url = "https://reqres.in/api/users?page=2"

@pytest.mark.smoke
def test_get_books_and_fetch_user_data(start_exec):

    response = requests.get(url)

    # display response
    print(response.content)

    print("Name of the server  : "+response.headers.get('Server'))
    # fetch cookies
    print("Fetch cookies : "+ str(response.cookies))

    # parse response to json format

    json_response = json.loads(response.text)
    print(json_response)

    # fetch the value using json response using jsonpath

    pages = jsonpath.jsonpath(json_response,'total_pages')
    print("Total number of pages  : " + str(pages[0]))

    for i in range (0,3):
        emailId = jsonpath.jsonpath(json_response,'data['+str(i)+'].email')
        # print all email ID
        print(emailId[0])

    assert  pages[0] == 2

@pytest.mark.sanity
def test_get_response_header(start_exec):
        response = requests.get(url)
        # display headers
        print(response.headers)
        assert "application/json" in response.headers["Content-Type"]

@pytest.mark.smoke
def test_validate_response_status(start_exec):
    response = requests.get(url)
    assert response.status_code == 200






