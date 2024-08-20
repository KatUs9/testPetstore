from dtos import get_pet_dto
from models import Pet


def test_empty_id():
    payload = get_pet_dto("", "", "")

    pet = Pet()
    status, json = pet.create(payload)

    assert status == 200
    assert isinstance(json["id"], int)


def test_no_id():
    payload = get_pet_dto(None, "Pips", "string")

    pet = Pet()
    status, json = pet.create(payload)

    assert status == 200
    assert isinstance(json["id"], int)
