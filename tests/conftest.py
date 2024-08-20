import pytest

from dtos.order import get_order_dto
from dtos.pet import get_pet_dto
from dtos.user import get_user_dto
from models.order import Order
from models.pet import Pet
from models.user import User


@pytest.fixture()
def pet():
    pet = Pet()
    pet.create(
        get_pet_dto(
            111122223333,
            "pipis",
            "https://i.pinimg.com/474x/47/56/1a/47561a958df86a9de9a1c441e63c9c12.jpg",
        )
    )

    return pet


@pytest.fixture()
def order(pet):
    order = Order()
    order.create(
        get_order_dto(
            5,
            pet.id,
            123,
            "2024-08-20T20:00:35.208+0000",
            "placed",

        )
    )

    return order


@pytest.fixture()
def user():
    user = User()
    user.create(
        get_user_dto(
            5,
            "lala",
            "lala@mail.com",
            "lala123",
            "+79999999999",

        )
    )

    return user
