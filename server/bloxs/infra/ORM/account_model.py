from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from bloxs.infra.ORM.user_model import UserModel

Base = declarative_base()


class AccountModel(Base):
    __tablename__ = "accounts"

    id = Column(String, primary_key=True)
    name = Column(String)
    user_id = Column(String, ForeignKey(UserModel.id))
    balance = Column(Integer)
    max_daily_withdraw = Column(Integer)
    is_active = Column(Boolean)
    type = Column(Integer)
    created_at = Column(DateTime)
