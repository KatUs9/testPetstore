from fixtures.pet import pet


def test_delete(pet):
    status, _ = pet.delete()
    assert status == 200
