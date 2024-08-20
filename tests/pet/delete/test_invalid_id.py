from models.pet import Pet


def test_delete_not_found():
    pet = Pet()
    pet.id = 11992921381231

    status, _ = pet.delete()
    assert status == 404


def test_delete_invalid_id():
    pet = Pet()
    pet.id = True

    status, _ = pet.delete()
    assert status == 404
