from datetime import datetime
from typing import TypedDict

from bloxs.application.repository.account_repository import AccountRepository
from bloxs.application.repository.transaction_repository import TransactionRepository
from bloxs.application.repository.user_repository import UserRepository
from bloxs.domain.account import Account
from bloxs.domain.transaction import Transaction


class CreateAccountInput(TypedDict):
    user_id: str
    balance: int
    max_daily_withdraw: int
    is_active: bool
    type: int


class AccountService:
    account_repository: AccountRepository
    user_repository: UserRepository
    transaction_repository: TransactionRepository

    def __init__(
        self, account_repository, user_repository, transaction_repository
    ) -> None:
        self.account_repository = account_repository
        self.user_repository = user_repository
        self.transaction_repository = transaction_repository

    def get(self, account_id: str):
        account = self.account_repository.get(account_id)
        if not account:
            raise Exception("Account not found")
        return account

    def update(self, account: Account):
        self.account_repository.update(account)
        return account

    def create(self, input: CreateAccountInput):
        user = self.user_repository.get(input["user_id"])
        if not user:
            raise Exception("User not found")
        account = Account(**input)
        self.account_repository.save(account)
        return account

    def make_deposit(self, account_id: str, amount: int):
        account = self.get(account_id)
        account.deposit(amount)
        self.update(account)
        self._save_transaction(account_id, account.name, amount)
        return account

    def make_withdraw(self, account_id: str, amount: int):
        account = self.get(account_id)
        account.withdraw(amount)
        self.update(account)
        self._save_transaction(account_id, account.name, -amount)
        return account

    def block_account(self, account_id: str):
        account = self.get(account_id)
        account.block()
        self.update(account)
        return account

    def unblock_account(self, account_id: str):
        account = self.get(account_id)
        account.unblock()
        self.update(account)
        return account

    def _save_transaction(self, account_id: str, account_name, amount: int):
        transaction = Transaction(
            account_id=account_id,
            account_name=account_name,
            amount=amount,
            transaction_date=datetime.now(),
        )
        self.transaction_repository.save(transaction)

    def list_accounts_by_user(self, user_id: str):
        return self.account_repository.list_accounts_by_user(user_id)
