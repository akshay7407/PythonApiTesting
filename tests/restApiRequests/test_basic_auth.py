import pytest
import requests
from requests.auth import HTTPBasicAuth

# Replace these with your API URL and credentials
API_URL = "https://example.com/api"
USERNAME = "your_username"
PASSWORD = "your_password"

@pytest.fixture
def auth():
    return HTTPBasicAuth(USERNAME, PASSWORD)

@pytest.mark.parametrize("endpoint", ["/endpoint1", "/endpoint2"])
def test_basic_authentication(endpoint, auth):
    url = API_URL + endpoint
    response = requests.get(url, auth=auth)

    # Assert that the status code is 200 (OK) for successful authentication
    assert response.status_code == 200

    # You can add more assertions based on your API's response

    # For example, check for a specific JSON response:
    # assert response.json() == expected_json_data

    # Or check for a specific header value:
    # assert response.headers['Content-Type'] == 'application/json'
