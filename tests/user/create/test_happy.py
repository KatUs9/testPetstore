from dtos import get_user_dto
from models import User


def test_happy_base():
    payload = get_user_dto()
    user = User()
    status, _ = user.create(payload)

    assert status == 200
