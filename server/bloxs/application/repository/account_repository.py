from abc import ABC, abstractmethod

from bloxs.domain.account import Account


class AccountRepository(ABC):
    @abstractmethod
    def save(self, account: Account):
        pass

    @abstractmethod
    def get(self, account_id) -> Account:
        pass

    @abstractmethod
    def update(self, account: Account) -> Account:
        pass

    @abstractmethod
    def list_accounts_by_user(self, user_id: str) -> list[Account]:
        pass
