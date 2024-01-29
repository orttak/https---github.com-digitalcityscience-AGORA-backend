from fastapi.testclient import TestClient
import pytest
from jose import JWTError, jwt
from app.main import app
from app.schemas import user_login
from app.auth.config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.auth.database import Base
from sqlalchemy.ext.declarative import declarative_base


# # at the end of the URL we define our test database
# SQL_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'
# # postgresql://hello_fastapi:hello_fastapi@db:5432/hello_fastapi_dev_test
# print(SQL_DATABASE_URL)
# engine = create_engine(SQL_DATABASE_URL)
# TestingSessionLocal = sessionmaker(
#     autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def overrite_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# client come from conftest.py
def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world"}


def test_create_user(client):
    response = client.post(
        "/users/", json={"email": "user_test@user.com", "password": "user_test"}
    )
    new_user = user_login.UserOut(**response.json())
    assert new_user.email == "user_test@user.com"
    assert response.status_code == 201


# if you run upper test, first you can get an error after firts calling because we save the test user in the database
# and after second call we get an error because the user is already in the database so
# we need to delete the user before we can create a new one. we'll do it with pytest.fixture


def test_login(client, test_user):
    # we should call create test user function again because pytest.fixture scope. if we don't define scope we'll get an error
    # because user'll delete it before we start this test
    # For general purpose, we add scope definition into decarator> @pytest.fixture(scope="module") it means, each test.py call it once
    # or decorator> @pytest.fixture(scope="session") it means each test session this fixture calling it once
    # our solution is to call create test user function again
    response = client.post(
        "/login",
        data={"username": test_user["email"], "password": test_user["password"]},
    )

    login_res = user_login.Token(**response.json())
    payload = jwt.decode(
        login_res.access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert response.status_code == 200


@pytest.mark.parametrize(
    "email, password, status_code",
    [
        ("wrongemail@user.com", "user1", 403),
        ("user1@user.com", "user2", 403),
        ("wrongemail@user.com", "user2", 403),
        (None, "user1", 422),
        ("user1@user.com", None, 422),
    ],
)
def test_login_fail(test_user, client, email, password, status_code):
    response = client.post("/login", data={"username": email, "password": password})

    assert response.status_code == status_code
