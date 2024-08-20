from dtos import get_user_dto
from models import User


def test_valid_email():
    payload = get_user_dto(email="mama@papa.net")
    user = User()
    status, _ = user.create(payload)

    assert status == 200


def test_invalid_email():
    payload = get_user_dto(email="kaka")
    user = User()
    status, _ = user.create(payload)

    assert status == 200
