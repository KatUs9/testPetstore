import pytest

from models.pet import Pet


@pytest.fixture()
def pet():
    pet = Pet()
    pet.create({
        "id": 111122223333,
        "category": {
            "id": 1,
            "name": "cats"
        },
        "name": "pipis",
        "photoUrls": [
            "https://i.pinimg.com/474x/47/56/1a/47561a958df86a9de9a1c441e63c9c12.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "kaka"
            }
        ],
        "status": "available"
    })

    return pet
