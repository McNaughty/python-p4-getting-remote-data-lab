import requests
import json

class GetRequester:
    url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'


    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        try:
            json_data = response_body.json()
        except ValueError:
            # If the response content is not valid JSON, return None
            json_data = None
        return json_data
    