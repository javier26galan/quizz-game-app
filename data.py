import requests

# make the request to take the questions from the api
parameters = {
    "amount": 10,
    "type": "boolean"
}

URL = "https://opentdb.com/api.php"


response = requests.get(URL, params=parameters)
question_data = response.json()["results"]
