def get_order_dto(id, petId, quantity, shipDate, status="placed", complete=False):
    return {
        "id": id,
        "petId": petId,
        "quantity": quantity,
        "shipDate": shipDate,
        "status": status,
        "complete": complete,
    }
