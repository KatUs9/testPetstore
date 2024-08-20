from dtos import get_pet_dto


def test_invalid_status(pet):
    payload = get_pet_dto(
        pet.id,
        "kakawa",
        "https://i.pinimg.com/474x/47/56/1a/47561a958df86a9de9a1c441e63c9c12.jpg",
        status="qwe",
    )
    status, json = pet.update_with_form(payload)
    assert status == 200

    status, json = pet.get()
    assert status == 200
    assert json["status"] == payload["status"]
