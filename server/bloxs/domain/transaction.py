from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel


class Transaction(BaseModel):
    id: UUID = uuid4()
    account_id: UUID
    account_name: str = ""
    amount: int
    transaction_date: datetime
