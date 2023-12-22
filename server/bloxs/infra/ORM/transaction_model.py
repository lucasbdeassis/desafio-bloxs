from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

from bloxs.infra.ORM.account_model import AccountModel

Base = declarative_base()


class TransactionModel(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True)
    account_id = Column(String, ForeignKey(AccountModel.id))
    account_name = Column(String, ForeignKey(AccountModel.name))
    amount = Column(Integer)
    transaction_date = Column(DateTime)
