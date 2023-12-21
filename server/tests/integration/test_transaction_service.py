from bloxs.application.service.transaction_service import TransactionService
from bloxs.infra.repository.orm_transaction_repository import OrmTransactionRepository


def test_list_transaction_by_account(session):
    transaction_repository = OrmTransactionRepository(session)
    transaction_service = TransactionService(transaction_repository)
    transactions = transaction_service.list_transaction_by_account(
        "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"
    )
    assert len(transactions) == 1
    assert str(transactions[0].account_id) == "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"
    assert transactions[0].amount == 200
