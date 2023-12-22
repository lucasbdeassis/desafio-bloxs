from datetime import date
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    surname: str
    email: str
    password: str
    cpf: str
    birthdate: date

    def check_password(self, password):
        return self.password == password
