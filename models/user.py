import requests

from data import base_url


class User:
    username = None
    password = None

    def create(self, payload):
        response = requests.post(f"{base_url}/user", json=payload)
        json = response.json()

        self.username = json["username"]
        self.password = json["password"]

        return response.status_code, json

    def login(self):
        response = requests.post(f"{base_url}/user/login?username={self.username}&password={self.password}")

        return response.status_code, response.json

    def logout(self):
        response = requests.post(f"{base_url}/user/logout")

        return response.status_code, response.json

    def get(self):
        response = requests.get(f"{base_url}/user/{self.username}")
        return response.status_code, response.json()

    def delete(self):
        response = requests.delete(f"{base_url}/user/{self.username}")
        return response.status_code, response.json()
