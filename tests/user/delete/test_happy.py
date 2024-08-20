def test_delete(user):
    status = user.delete()
    assert status == 200
