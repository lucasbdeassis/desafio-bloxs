from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

from bloxs.application.service.account_service import AccountService
from bloxs.application.service.auth_service import AuthService
from bloxs.application.service.transaction_service import TransactionService
from bloxs.infra.repository.orm_account_repository import OrmAccountRepository
from bloxs.infra.repository.orm_transaction_repository import OrmTransactionRepository
from bloxs.infra.repository.orm_user_repository import OrmUserRepository


class InjectorFactory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(InjectorFactory, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def init(self, engine):
        self.engine = engine

    @contextmanager
    def get_session(self) -> Generator[sessionmaker, None, None]:
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    @contextmanager
    def get_auth_service(self) -> Generator[AuthService, None, None]:
        with self.get_session() as session:
            user_repository = OrmUserRepository(session)
            yield AuthService(user_repository)

    @contextmanager
    def get_account_service(self) -> Generator[AccountService, None, None]:
        with self.get_session() as session:
            account_repository = OrmAccountRepository(session)
            user_repository = OrmUserRepository(session)
            transaction_repository = OrmTransactionRepository(session)
            yield AccountService(
                account_repository, user_repository, transaction_repository
            )

    @contextmanager
    def get_transaction_service(self) -> Generator[TransactionService, None, None]:
        with self.get_session() as session:
            transaction_repository = OrmTransactionRepository(session)
            yield TransactionService(transaction_repository)
