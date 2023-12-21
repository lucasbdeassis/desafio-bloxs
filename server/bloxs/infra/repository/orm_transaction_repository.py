from uuid import UUID

from sqlalchemy.orm import Session

from bloxs.application.repository.transaction_repository import TransactionRepository
from bloxs.domain.transaction import Transaction
from bloxs.infra.ORM.account_model import AccountModel
from bloxs.infra.ORM.transaction_model import TransactionModel


class OrmTransactionRepository(TransactionRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def list_transaction_by_account(self, account_id: str) -> [TransactionModel]:
        transactions = (
            self.session.query(TransactionModel)
            .filter(TransactionModel.account_id == account_id)
            .all()
        )
        return [
            Transaction(
                id=UUID(transaction.id),
                account_id=UUID(transaction.account_id),
                account_name=transaction.account_name,
                amount=transaction.amount,
                transaction_date=transaction.transaction_date,
            )
            for transaction in transactions
        ]

    def save(self, transaction: Transaction) -> Transaction:
        transaction_model = TransactionModel(
            id=str(transaction.id),
            account_id=str(transaction.account_id),
            account_name=transaction.account_name,
            amount=transaction.amount,
            transaction_date=transaction.transaction_date,
        )
        self.session.add(transaction_model)
        return transaction

    def list_transactions_by_user(self, user_id: str) -> [TransactionModel]:
        transactions = (
            self.session.query(TransactionModel)
            .join(AccountModel, TransactionModel.account_id == AccountModel.id)
            .filter(AccountModel.user_id == user_id)
            .all()
        )
        return [
            Transaction(
                id=UUID(transaction.id),
                account_id=UUID(transaction.account_id),
                account_name=transaction.account_name,
                amount=transaction.amount,
                transaction_date=transaction.transaction_date,
            )
            for transaction in transactions
        ]
