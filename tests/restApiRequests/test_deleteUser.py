import requests
import pytest




def test_delete_user():
    # Assuming your API base URL
    BASE_URL = "https://reqres.in/api/users/2"

    response = requests.delete(BASE_URL)

    assert response.status_code == 204  # Assuming successful deletion
    assert response.content == b''  # Empty response content

    # Optionally, you might want to check that the user is actually deleted
    # by trying to fetch the user again and expecting a 404 response.

# Optionally, you might add more tests for error cases, authentication,
# and other scenarios relevant to your API.
