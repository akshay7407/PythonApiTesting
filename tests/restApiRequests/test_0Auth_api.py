import pytest
import requests

# Replace these with your OAuth API endpoints and client credentials
TOKEN_URL = "https://oauth.example.com/token"
RESOURCE_URL = "https://api.example.com/resource"
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
USERNAME = "your_username"
PASSWORD = "your_password"

@pytest.fixture
def get_access_token():
    data = {
        "grant_type": "password",
        "username": USERNAME,
        "password": PASSWORD,
    }
    response = requests.post(
        TOKEN_URL,
        data=data,
        auth=(CLIENT_ID, CLIENT_SECRET),
    )
    assert response.status_code == 200
    return response.json()["access_token"]

def test_oauth_api_resource_access(get_access_token):
    headers = {
        "Authorization": f"Bearer {get_access_token}",
    }
    response = requests.get(RESOURCE_URL, headers=headers)

    # Assert that the status code is 200 for successful resource access
    assert response.status_code == 200

    # You can add more assertions based on your API's response

    # For example, check for a specific JSON response:
    # assert response.json() == expected_json_data

    # Or check for a specific header value:
    # assert response.headers['Content-Type'] == 'application/json'
