from fixtures.pet import pet


def test_delete(pet):
    status, json = pet.delete()
    assert status == 200
