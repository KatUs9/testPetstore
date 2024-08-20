from dtos.pet import get_pet_dto
from fixtures.pet import pet


def test_update_with_form(pet):
    payload = get_pet_dto(pet.id, "kakawa", "https://i.pinimg.com/474x/47/56/1a/47561a958df86a9de9a1c441e63c9c12.jpg")
    status, json = pet.update_with_form(payload)
    assert status == 200

    status, json = pet.get()
    assert status == 200
    assert json["name"] == payload["name"]
