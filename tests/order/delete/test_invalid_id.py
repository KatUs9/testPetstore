from models import User


def test_delete_not_found():
    user = User()
    user.username = "85666"

    status = user.delete()
    assert status == 404
