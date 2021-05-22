import requests

API_URL = "https://opentdb.com/api.php"

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url=API_URL, params=parameters)
response.raise_for_status()
result = response.json()
question_data = result["results"]
