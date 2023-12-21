from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Account(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    user_id: UUID
    balance: int
    max_daily_withdraw: int
    is_active: bool = True
    type: int = 1
    created_at: datetime = datetime.now()

    def deposit(self, amount: int):
        if amount <= 0:
            raise Exception("The deposit value must be greater than 0")
        self.balance += amount

    def withdraw(self, amount: int):
        if self.balance - amount <= 0:
            raise Exception("Insufficient funds")
        self.balance -= amount

    def block(self):
        if not self.is_active:
            raise Exception("The account is already blocked")
        self.is_active = False

    def unblock(self):
        if self.is_active:
            raise Exception("The account is already active")
        self.is_active = True
