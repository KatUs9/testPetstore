from dtos import get_pet_dto


def test_required_fields(pet):  # переделать
    payload = get_pet_dto(
        None,
        None,
        "https://i.pinimg.com/474x/47/56/1a/47561a958df86a9de9a1c441e63c9c12.jpg",
        status="sold",
    )
    status, json = pet.update_with_form(payload)

    assert status == 200

    status, json = pet.get()
    assert status == 200
    assert json["name"] == pet.name
