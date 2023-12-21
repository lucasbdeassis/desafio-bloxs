import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from bloxs.main import create_app


@pytest.fixture()
def session():
    engine = create_engine("sqlite:///:memory:")
    Session = sessionmaker(bind=engine)
    session = Session()
    with open("tests/db_test.sql", "r") as f:
        sql_script = f.read()
    sql_statements = sql_script.split(";")
    for statement in sql_statements:
        if statement.strip():
            session.execute(text(statement))
    session.commit()
    yield session
    session.close()


@pytest.fixture()
def app():
    app = create_app()
    with app.app_context():
        yield app


@pytest.fixture()
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture()
def auth_token(client):
    response = client.post(
        "/auth/login",
        json={
            "email": "john.doe@example.com",
            "password": "password",
        },
    )
    yield response.json["token"]
