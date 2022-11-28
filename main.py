import requests


url = "https://petstore.swagger.io/v2/pet"
data_new_pet = {
  "id": 18,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Raichu001",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

response = requests.post (url, json = data_new_pet)
print(response.text)

data_new_pet1 = {
  "id": 19,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Pikachu",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.post (url, json = data_new_pet1)
print(response.text)

data_new_pet2 = {
  "id": 20,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Slowpoke",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.post (url, json = data_new_pet2)
print(response.text)

url = "https://petstore.swagger.io/v2/pet"
data_new_pet = {
  "id": 18,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Raichu007",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.put (url, json = data_new_pet)
print(response.text)

data_new_pet1 = {
  "id": 19,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Pikachu001",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.put (url, json = data_new_pet1)
print(response.text)

data_new_pet2 = {
  "id": 20,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Slowpoke001",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
response = requests.put (url, json = data_new_pet2)
print(response.text)



url = "https://petstore.swagger.io/v2/pet/18"
response = requests.get (url)
print(response.text)

url = "https://petstore.swagger.io/v2/pet/19"
response = requests.get (url)
print(response.text)

url = "https://petstore.swagger.io/v2/pet/20"
response = requests.get (url)
print(response.text)