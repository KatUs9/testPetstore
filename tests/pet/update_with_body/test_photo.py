from dtos.pet import get_pet_dto
from fixtures.pet import pet


def test_empty_photo(pet):
    payload = get_pet_dto(999, "Pips", "", status="sold")

    status, json = pet.update_with_body(payload)

    assert status == 200
    assert json["photoUrls"] == payload["photoUrls"]
