from sqlmodel import Session, select
from . import models, schemas
from typing import List, Optional
from passlib.hash import bcrypt


def get_user_by_username(session: Session, username: str) -> Optional[models.User]:
    statement = select(models.User).where(models.User.username == username)
    return session.exec(statement).first()


def create_user(session: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(username=user.username, hashed_password=bcrypt.hash(user.password), role=user.role)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def authenticate_user(session: Session, username: str, password: str) -> Optional[models.User]:
    user = get_user_by_username(session, username)
    if user and bcrypt.verify(password, user.hashed_password):
        return user
    return None


def create_appointment(session: Session, data: schemas.AppointmentCreate) -> models.Appointment:
    appt = models.Appointment.from_orm(data)
    session.add(appt)
    session.commit()
    session.refresh(appt)
    return appt


def list_appointments(session: Session) -> List[models.Appointment]:
    return session.exec(select(models.Appointment)).all()
