import json

def extract_data():

    with open("../sample_sushi_response.json", "r") as file:
        data = json.load(file)

    return data