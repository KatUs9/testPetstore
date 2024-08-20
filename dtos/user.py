def get_user_dto(
    id=0,
    username="katus9",
    email="mail@mail.com",
    password="secret_pass",
    phone="+79991112233",
    first_name="Katya",
    last_name="Us",
    user_status=1337,
):
    return {
        "id": id,
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": user_status,
    }
