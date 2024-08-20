from dtos import get_order_dto
from models import Order


def test_ship_date():
    payload = get_order_dto(
        999,
        999,
        999,
        "2024-08-20T20:00:35.208+0000",
        "approved",
    )
    order = Order()
    status, json = order.create(payload)

    assert status == 200
    assert json["shipDate"] == payload["shipDate"]


def test_number_ship_date():
    payload = get_order_dto(
        999,
        999,
        999,
        777,
        "approved",
    )
    order = Order()
    status, json = order.create(payload)

    assert status == 200
    assert json["shipDate"] == "1970-01-01T00:00:00.777+0000"


def test_invalid_ship_date():
    payload = get_order_dto(
        999,
        999,
        999,
        "qqq",
        "approved",
    )
    order = Order()
    status, json = order.create(payload)

    assert status == 500
