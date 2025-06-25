import pytest

pytest.importorskip("sqlmodel")

from sqlmodel import Session
from .. import models, schemas, crud
from ..database import engine

@pytest.fixture()
def session():
    models.SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_create_user(session):
    user = crud.create_user(session, schemas.UserCreate(username="u", password="p"))
    assert user.id is not None
    fetched = crud.get_user_by_username(session, "u")
    assert fetched
