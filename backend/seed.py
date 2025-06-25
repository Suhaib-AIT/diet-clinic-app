from .database import engine
from .models import SQLModel, User
from .crud import create_user
from sqlmodel import Session
from .schemas import UserCreate


def seed():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        if not session.exec("SELECT * FROM user").first():
            create_user(session, UserCreate(username="admin", password="admin", role="admin"))


if __name__ == "__main__":
    seed()
