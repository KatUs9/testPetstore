from models.pet import Pet


def test_valid_status():
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
        "status": "sold"
    }

    pet = Pet()
    status, json = pet.create(payload)

    assert status == 200
    assert json["status"] == payload["status"]


def test_invalid_status():
    """Test whether API validates pet status.

    In fact, API does not validate received pet statuses, so we test actual behavior.
    """

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
        "status": "qwe"
    }

    pet = Pet()
    status, json = pet.create(payload)

    assert status == 200
    assert json["status"] == payload["status"]
