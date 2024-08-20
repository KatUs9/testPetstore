def get_pet_dto(id, name, photo_url, status="available"):
    return {
        "id": id,
        "category": {
            "id": 1,
            "name": "pet"
        },
        "name": name,
        "photoUrls": [
            photo_url
        ],
        "tags": [
            {
                "id": 1,
                "name": "kaka"
            }
        ],
        "status": status
    }
