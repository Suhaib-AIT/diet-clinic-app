from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=get_password_hash(user.password),
        role=user.role.value if hasattr(user.role, "value") else user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_appointment(db: Session, appointment: schemas.AppointmentCreate) -> models.Appointment:
    db_obj = models.Appointment(
        date=appointment.date,
        description=appointment.description,
        patient_id=appointment.patient_id,
        dietitian_id=appointment.dietitian_id,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_diet_plan(db: Session, plan: schemas.DietPlanCreate) -> models.DietPlan:
    db_obj = models.DietPlan(
        details=plan.details,
        patient_id=plan.patient_id,
        dietitian_id=plan.dietitian_id,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def create_food_log(db: Session, log: schemas.FoodLogCreate) -> models.FoodLog:
    db_obj = models.FoodLog(
        date=log.date,
        meal_details=log.meal_details,
        patient_id=log.patient_id,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
