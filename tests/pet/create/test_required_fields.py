from models.pet import Pet


def test_empty_id():
    payload = {
        "id": "",
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": ""
    }

    pet = Pet()
    status, json = pet.create(payload)

    assert status == 200


def test_no_id():
    payload = {
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "kaka",
        "photoUrls": [
            "string"
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
