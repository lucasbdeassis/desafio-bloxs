from bloxs.application.service.auth_service import AuthService
from bloxs.infra.repository.orm_user_repository import OrmUserRepository


def test_login(session):
    user_repo = OrmUserRepository(session)
    auth_service = AuthService(user_repo)
    token = auth_service.login("john.doe@example.com", "password")
    assert isinstance(token, str)


def test_validade_token(session):
    user_repo = OrmUserRepository(session)
    auth_service = AuthService(user_repo)
    token = auth_service.login("john.doe@example.com", "password")
    user_id = auth_service.validate_token(token)
    assert isinstance(user_id, str)
