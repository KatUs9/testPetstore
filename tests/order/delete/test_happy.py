def test_delete(order):
    status, json = order.delete()
    assert status == 200
