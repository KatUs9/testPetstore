from dtos import get_pet_dto
from models import Pet


def test_valid_remote_photo():
    payload = get_pet_dto(
        999,
        "Pips",
        "https://i.pinimg.com/474x/47/56/1a/47561a958df86a9de9a1c441e63c9c12.jpg",
    )

    pet = Pet()
    status, json = pet.create(payload)

    assert status == 200
    assert json["photoUrls"] == payload["photoUrls"]


def test_invalid_photo():
    payload = get_pet_dto(999, "Pips", "u2u2u2")
    pet = Pet()
    status, json = pet.create(payload)

    assert status == 200
    assert json["photoUrls"] == payload["photoUrls"]
