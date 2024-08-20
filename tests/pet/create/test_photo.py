from models.pet import Pet


def test_valid_remote_photo():
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

    status, json = Pet.create(payload)

    assert status == 200
    assert json["photoUrls"] == payload["photoUrls"]


def test_invalid_photo():
    """Test whether API validates pet photo URL.

    In fact, API does not validate URLs, so we test actual behavior.
    """

    payload = {
        "id": 999,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Pips",
        "photoUrls": [
            "u2u2u2"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    status, json = Pet.create(payload)

    assert status == 200
    assert json["photoUrls"] == payload["photoUrls"]
