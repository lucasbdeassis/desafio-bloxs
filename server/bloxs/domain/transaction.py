from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Transaction(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    account_id: UUID
    account_name: str = ""
    amount: int
    transaction_date: datetime
