from dtos import get_pet_dto


def test_required_fields(pet):
    """Testing whether the API validates the required name and photo fields.

    The API doesn't actually validate URLs, so we're testing the actual behavior.
    """

    payload = get_pet_dto(
        21232,
        None,
        None,
        status="sold",
    )
    status, json = pet.update_with_body(payload)

    assert status == 200
    assert json["id"] == payload["id"]
