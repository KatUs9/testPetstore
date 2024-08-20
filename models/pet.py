import requests

from data import base_url


class Pet:
    id = None

    def create(self, payload):
        response = requests.post(f"{base_url}/pet", json=payload)
        json = response.json()

        self.id = json["id"]

        return response.status_code, json

    def get(self):
        response = requests.get(f"{base_url}/pet/{self.id}")
        return response.status_code, response.json()

    def update_with_body(self, payload):
        response = requests.put(f"{base_url}/pet", json=payload)
        return response.status_code, response.json()

    def update_with_form(self, payload):
        response = requests.post(f"{base_url}/pet/{self.id}", data=payload)
        return response.status_code, response.json()

    def delete(self):
        response = requests.delete(f"{base_url}/pet/{self.id}")
        return response.status_code, response.json()
