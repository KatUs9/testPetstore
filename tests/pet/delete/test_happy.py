def test_delete(pet):
    status = pet.delete()
    assert status == 200
