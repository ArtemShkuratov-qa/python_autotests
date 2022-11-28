import pytest
import requests

url = "https://petstore.swagger.io/v2/pet/18"
def test_status_code():
    response = requests.get (url)
    assert response.status_code == 200

def test_check_response():
    response = requests.get (url)
    response = response.json()
    assert response["name"] == "Raichu007"



data = [("name", "Raichu007", 18),("name", "Pikachu001", 19),("status", "available", 20)]
@pytest.mark.parametrize("key, value, id", data)
def test_piece_of_body (key, value, id):
    url = f"https://petstore.swagger.io/v2/pet/{id}"
    response = requests.get (url)
    response = response.json()
    assert response[key] == value