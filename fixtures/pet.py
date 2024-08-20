import pytest

from dtos.pet import get_pet_dto
from models.pet import Pet


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
