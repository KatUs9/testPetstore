from models.pet import Pet


def test_not_found_id():
    pet = Pet()
    pet.id = 99900991122332211

    status, _ = pet.get()

    assert status == 404


def test_invalid_id():
    pet = Pet()
    pet.id = "qwe"

    status, _ = pet.get()

    assert status == 404
