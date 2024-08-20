from dtos import get_order_dto
from models import Order


def test_status():
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
    assert json["status"] == payload["status"]


def test_invalid_status():
    """Test whether API validates order status.

    In fact, API does not validate received order statuses, so we test actual behavior.
    """

    payload = get_order_dto(
        999,
        999,
        999,
        "2024-08-20T20:00:35.208Z",
        "qwq",
    )

    order = Order()
    status, json = order.create(payload)

    assert status == 200
    assert json["status"] == payload["status"]
