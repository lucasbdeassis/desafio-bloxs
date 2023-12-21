from datetime import datetime
from uuid import uuid4

from bloxs.domain.transaction import Transaction


def test_transaction_create():
    account_id = uuid4()
    transaction_date = datetime.now()
    transaction = Transaction(
        account_id=account_id, amount=10000, transaction_date=transaction_date
    )
    assert transaction.account_id == account_id
    assert transaction.amount == 10000
    assert transaction.transaction_date == transaction_date
