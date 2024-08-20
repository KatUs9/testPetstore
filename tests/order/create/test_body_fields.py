from dtos import get_order_dto
from models import Order


def test_body_fields():
    payload = get_order_dto(None, None, None, None)

    order = Order()
    status, json = order.create(payload)

    assert status == 200
    assert isinstance(json["id"], int)
    assert json["petId"] == 0
    assert json["quantity"] == 0
    assert "shipDate" not in json
