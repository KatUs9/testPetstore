def test_happy(order):
    status, json = order.get()

    assert status == 200
    assert json["id"] == order.id
