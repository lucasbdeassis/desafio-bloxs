from datetime import date

from bloxs.domain.user import User


def test_user_creation():
    user = User(
        name="Rodrigo",
        surname="Borges da Silva",
        email="rodrigo_borges@gmail.com",
        password="123456",
        cpf="123.456.789-00",
        birthdate=date(1990, 1, 1),
    )
    assert user.name == "Rodrigo"
    assert user.surname == "Borges da Silva"
    assert user.cpf == "123.456.789-00"
    assert user.birthdate == date(1990, 1, 1)
