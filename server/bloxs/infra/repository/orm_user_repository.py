from uuid import UUID

from sqlalchemy.orm import Session

from bloxs.application.repository.user_repository import UserRepository
from bloxs.domain.user import User
from bloxs.infra.ORM.user_model import UserModel


class OrmUserRepository(UserRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_email(self, email: str) -> User:
        user_model = (
            self.session.query(UserModel).filter(UserModel.email == email).first()
        )
        user = User(
            id=UUID(user_model.id),
            name=user_model.name,
            surname=user_model.surname,
            email=user_model.email,
            password=user_model.password,
            cpf=user_model.cpf,
            birthdate=user_model.birthdate,
        )
        return user

    def get(self, user_id: str) -> User:
        user_model = (
            self.session.query(UserModel).filter(UserModel.id == user_id).first()
        )
        user = User(
            id=UUID(user_model.id),
            name=user_model.name,
            surname=user_model.surname,
            email=user_model.email,
            password=user_model.password,
            cpf=user_model.cpf,
            birthdate=user_model.birthdate,
        )
        return user
