from dtos.pet import get_pet_dto
from models.pet import Pet


def test_empty_id():
    payload = get_pet_dto(0, "", "")

    pet = Pet()
    status, _ = pet.create(payload)

    assert status == 200


def test_no_id():
    payload = get_pet_dto(0, "Pips", "string")

    pet = Pet()
    status, json = pet.create(payload)

    assert status == 200
