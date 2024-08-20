from fixtures.pet import pet


def test_happy(pet):
    payload = {
        "id": 21232,
        "name": "aboba",
        "status": "sold"
    }
    status, json = pet.update_with_body(payload)

    assert status == 200
    assert json["id"] == payload["id"]
