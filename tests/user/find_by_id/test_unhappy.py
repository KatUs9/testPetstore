from models import User


def test_not_found_username():
    user = User()
    user.username = "fmfm"
    status, _ = user.get()

    assert status == 404
