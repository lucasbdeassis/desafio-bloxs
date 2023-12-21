from uuid import UUID

from sqlalchemy.orm import Session

from bloxs.application.repository.account_repository import AccountRepository
from bloxs.domain.account import Account
from bloxs.infra.ORM.account_model import AccountModel


class OrmAccountRepository(AccountRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, account: Account):
        account_model = AccountModel(
            id=str(account.id),
            name=account.name,
            user_id=str(account.user_id),
            balance=account.balance,
            max_daily_withdraw=account.max_daily_withdraw,
            is_active=account.is_active,
            type=account.type,
            created_at=account.created_at,
        )
        self.session.add(account_model)

    def get(self, account_id: str):
        account_model = (
            self.session.query(AccountModel)
            .filter(AccountModel.id == account_id)
            .first()
        )
        account = Account(
            id=UUID(account_model.id),
            name=account_model.name,
            user_id=UUID(account_model.user_id),
            balance=account_model.balance,
            max_daily_withdraw=account_model.max_daily_withdraw,
            is_active=account_model.is_active,
            type=account_model.type,
            created_at=account_model.created_at,
        )
        return account

    def update(self, account: Account):
        account_model = (
            self.session.query(AccountModel)
            .filter(AccountModel.id == str(account.id))
            .first()
        )
        account_model.user_id = str(account.user_id)
        account_model.name = account.name
        account_model.balance = account.balance
        account_model.max_daily_withdraw = account.max_daily_withdraw
        account_model.is_active = account.is_active
        account_model.type = account.type
        self.session.add(account_model)
        return account

    def list_accounts_by_user(self, user_id: str):
        account_models = (
            self.session.query(AccountModel)
            .filter(AccountModel.user_id == user_id)
            .all()
        )
        return [
            Account(
                id=UUID(account_model.id),
                user_id=UUID(account_model.user_id),
                name=account_model.name,
                balance=account_model.balance,
                max_daily_withdraw=account_model.max_daily_withdraw,
                is_active=account_model.is_active,
                type=account_model.type,
                created_at=account_model.created_at,
            )
            for account_model in account_models
        ]
