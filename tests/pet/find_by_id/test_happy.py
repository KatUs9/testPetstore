def test_happy(pet):
    status, json = pet.get()

    assert status == 200
    assert json["id"] == pet.id
