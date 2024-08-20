def test_happy(user):
    status, json = user.get()

    assert status == 200
    assert json["username"] == user.username
