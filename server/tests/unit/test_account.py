from uuid import uuid4

from bloxs.domain.account import Account


def test_account_create():
    user_id = uuid4()
    account = Account(
        user_id=user_id,
        name="Test",
        balance=1000,
        max_daily_withdraw=20000,
        is_active=True,
        type=1,
    )
    assert account.id is not None
    assert account.user_id == user_id
    assert account.balance == 1000
    assert account.max_daily_withdraw == 20000
    assert account.is_active
    assert account.type == 1


def test_account_deposit():
    user_id = uuid4()
    account = Account(
        user_id=user_id,
        balance=1000,
        name="Test",
        max_daily_withdraw=20000,
        is_active=True,
        type=1,
    )
    account.deposit(100)
    assert account.balance == 1100


def test_account_withdraw():
    user_id = uuid4()
    account = Account(
        user_id=user_id,
        balance=1000,
        name="Test",
        max_daily_withdraw=20000,
        is_active=True,
        type=1,
    )
    account.withdraw(100)
    assert account.balance == 900


def test_account_block():
    user_id = uuid4()
    account = Account(
        user_id=user_id,
        balance=1000,
        name="Test",
        max_daily_withdraw=20000,
        is_active=True,
        type=1,
    )
    account.block()
    assert account.is_active is False


def test_account_unblock():
    user_id = uuid4()
    account = Account(
        user_id=user_id,
        balance=1000,
        name="Test",
        max_daily_withdraw=20000,
        is_active=False,
        type=1,
    )
    account.unblock()
    assert account.is_active is True
