from fixtures.pet import pet


def test_update_with_form(pet):
    payload = {
        "petId": pet.id,
        "name": "kakawa"
    }
    status, json = pet.update_with_form(payload)
    assert status == 200

    status, json = pet.get()
    assert status == 200
    assert json["name"] == payload["name"]
