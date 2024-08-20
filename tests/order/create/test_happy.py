from dtos import get_order_dto
from models import Order


def test_happy_base():
    payload = get_order_dto(999, 999, 999, "2024-08-20T20:00:35.208Z")

    order = Order()
    status, json = order.create(payload)

    assert status == 200
    assert json["id"] == payload["id"]
