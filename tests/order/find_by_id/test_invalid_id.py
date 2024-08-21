from models import Order


def test_not_found_id():
    order = Order()
    order.id = 99900991122332211

    status, _ = order.get()

    assert status == 404


def test_invalid_id():
    order = Order()
    order.id = "qwe"

    status, json = order.get()

    assert status == 404


def test_less_than_one_id():
    order = Order()
    order.id = -12

    status, json = order.get()

    assert status == 404


def test_more_than_ten_id():
    order = Order()
    order.id = 99121

    status, json = order.get()

    assert status == 404
