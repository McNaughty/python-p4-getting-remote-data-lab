import requests
import json

class GetRequester:
    url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'


    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content #Return the body of the response as a string

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body) # Parse the JSON response and return it as a Python list or dictionary

    