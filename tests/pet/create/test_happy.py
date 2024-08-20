from models.pet import Pet


def test_happy_base():
    payload = {
        "id": 999,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Pips",
        "photoUrls": [
            "https://i.pinimg.com/474x/47/56/1a/47561a958df86a9de9a1c441e63c9c12.jpg"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    pet = Pet()
    status, json = pet.create(payload)

    assert status == 200
    assert json["id"] == payload['id']
