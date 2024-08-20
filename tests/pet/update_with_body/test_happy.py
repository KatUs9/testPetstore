from dtos.pet import get_pet_dto
from fixtures.pet import pet


def test_happy(pet):
    payload = get_pet_dto(
        21232,
        "aboba",
        "https://i.pinimg.com/474x/47/56/1a/47561a958df86a9de9a1c441e63c9c12.jpg",
        status="sold",
    )
    status, json = pet.update_with_body(payload)

    assert status == 200
    assert json["id"] == payload["id"]
