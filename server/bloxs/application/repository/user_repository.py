from abc import ABC, abstractmethod

from bloxs.domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def get(self, user_id: str) -> User:
        pass
