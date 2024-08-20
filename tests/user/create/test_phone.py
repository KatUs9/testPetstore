from dtos import get_user_dto
from models import User


def test_valid_phone():
    payload = get_user_dto(phone="+78989778832")
    user = User()
    status, _ = user.create(payload)

    assert status == 200


def test_invalid_phone():
    payload = get_user_dto(phone="kaka")
    user = User()
    status, _ = user.create(payload)

    assert status == 200
