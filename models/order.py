import requests

from data import base_url


class Order:
    id = None

    def create(self, payload):
        response = requests.post(f"{base_url}/store/order", json=payload)
        json = response.json()

        self.id = json["id"]

        return response.status_code, json

    def get_by_id(self):
        response = requests.get(f"{base_url}/store/order/{self.id}")
        return response.status_code, response.json()

    def delete(self):
        response = requests.delete(f"{base_url}/store/order/{self.id}")
        return response.status_code, response.json()
