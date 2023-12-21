from abc import ABC, abstractmethod

from bloxs.domain.transaction import Transaction


class TransactionRepository(ABC):
    @abstractmethod
    def list_transaction_by_account(self, account_id: str) -> list[Transaction]:
        pass

    @abstractmethod
    def save(self, transaction: Transaction) -> Transaction:
        pass

    @abstractmethod
    def list_transactions_by_user(self, user_id: str) -> list[Transaction]:
        pass
