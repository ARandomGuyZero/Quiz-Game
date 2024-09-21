from requests import get

# Parameters we will need
parameters = {
    "amount": 10,
    "type": "boolean"
}

# Request the quiz data from opentdb.com
response = get(url="https://opentdb.com/api.php", params=parameters)

# Raises an error if we get one
response.raise_for_status()

# Get the data
data = response.json()

# List that contains dictionaries with questions and their answer
question_data = data["results"]