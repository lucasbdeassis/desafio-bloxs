from bloxs.application.repository.transaction_repository import TransactionRepository
from bloxs.domain.transaction import Transaction


class TransactionService:
    transaction_repository: TransactionRepository

    def __init__(self, transaction_repository) -> None:
        self.transaction_repository = transaction_repository

    def list_transaction_by_account(self, account_id: str) -> list[Transaction]:
        return self.transaction_repository.list_transaction_by_account(account_id)

    def list_transactions_by_user(self, user_id: str) -> list[Transaction]:
        return self.transaction_repository.list_transactions_by_user(user_id)
