import pytest

from bloxs.application.service.account_service import AccountService
from bloxs.infra.repository.orm_account_repository import OrmAccountRepository
from bloxs.infra.repository.orm_transaction_repository import OrmTransactionRepository
from bloxs.infra.repository.orm_user_repository import OrmUserRepository


def test_get_account(session):
    account_repository = OrmAccountRepository(session)
    user_repository = OrmUserRepository(session)
    transaction_repository = OrmTransactionRepository(session)
    account_service = AccountService(
        account_repository, user_repository, transaction_repository
    )
    account = account_service.get(
        "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11", "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"
    )
    assert account.balance == 1000
    assert account.max_daily_withdraw == 10000
    assert account.is_active is True
    assert account.type == 1


def test_create_account(session):
    account_repository = OrmAccountRepository(session)
    user_repository = OrmUserRepository(session)
    transaction_repository = OrmTransactionRepository(session)
    account_service = AccountService(
        account_repository, user_repository, transaction_repository
    )
    account_data = {
        "user_id": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
        "balance": 1000,
        "name": "Test",
        "max_daily_withdraw": 10000,
        "is_active": True,
        "type": 1,
    }
    account_id = account_service.create(account_data).id
    account = account_service.get(
        "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11", str(account_id)
    )
    assert str(account.id) == str(account_id)
    assert str(account.user_id) == account_data["user_id"]
    assert account.balance == account_data["balance"]
    assert account.max_daily_withdraw == account_data["max_daily_withdraw"]
    assert account.is_active == account_data["is_active"]
    assert account.type == account_data["type"]


def test_make_deposit(session):
    account_repository = OrmAccountRepository(session)
    user_repository = OrmUserRepository(session)
    transaction_repository = OrmTransactionRepository(session)
    account_service = AccountService(
        account_repository, user_repository, transaction_repository
    )
    account_service.make_deposit(
        "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
        "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12",
        100,
    )
    account = account_service.get(
        "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11", "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"
    )
    assert account.balance == 1100


def test_make_withdraw(session):
    account_repository = OrmAccountRepository(session)
    user_repository = OrmUserRepository(session)
    transaction_repository = OrmTransactionRepository(session)
    account_service = AccountService(
        account_repository, user_repository, transaction_repository
    )
    account_service.make_withdraw(
        "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
        "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12",
        100,
    )
    account = account_service.get(
        "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11", "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"
    )
    assert account.balance == 900


def test_block_account(session):
    account_repository = OrmAccountRepository(session)
    user_repository = OrmUserRepository(session)
    transaction_repository = OrmTransactionRepository(session)
    account_service = AccountService(
        account_repository, user_repository, transaction_repository
    )
    account = account_service.block_account(
        "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11", "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"
    )
    assert account.is_active is False


def test_unblock_account(session):
    account_repository = OrmAccountRepository(session)
    user_repository = OrmUserRepository(session)
    transaction_repository = OrmTransactionRepository(session)
    account_service = AccountService(
        account_repository, user_repository, transaction_repository
    )
    account_service.block_account(
        "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11", "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"
    )
    account = account_service.unblock_account(
        "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11", "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12"
    )
    assert account.is_active is True


def test_list_accounts_by_user(session):
    account_repository = OrmAccountRepository(session)
    user_repository = OrmUserRepository(session)
    transaction_repository = OrmTransactionRepository(session)
    account_service = AccountService(
        account_repository, user_repository, transaction_repository
    )
    accounts = account_service.list_accounts_by_user(
        "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
    )
    assert isinstance(accounts, list)


def test_exceed_daily_withdraw(session):
    account_repository = OrmAccountRepository(session)
    user_repository = OrmUserRepository(session)
    transaction_repository = OrmTransactionRepository(session)
    account_service = AccountService(
        account_repository, user_repository, transaction_repository
    )
    with pytest.raises(Exception):
        account_service.make_withdraw(
            "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
            "b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12",
            10000000,
        )
