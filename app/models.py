from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship

from .database import Base

class Role(str, Enum):
    admin = "admin"
    dietitian = "dietitian"
    patient = "patient"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default=Role.patient.value)

    appointments_as_patient = relationship(
        "Appointment", back_populates="patient", foreign_keys="Appointment.patient_id"
    )
    appointments_as_dietitian = relationship(
        "Appointment", back_populates="dietitian", foreign_keys="Appointment.dietitian_id"
    )
    diet_plans = relationship("DietPlan", back_populates="patient")
    food_logs = relationship("FoodLog", back_populates="patient")

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    description = Column(Text, nullable=True)
    patient_id = Column(Integer, ForeignKey("users.id"))
    dietitian_id = Column(Integer, ForeignKey("users.id"))

    patient = relationship("User", back_populates="appointments_as_patient", foreign_keys=[patient_id])
    dietitian = relationship("User", back_populates="appointments_as_dietitian", foreign_keys=[dietitian_id])

class DietPlan(Base):
    __tablename__ = "diet_plans"
    id = Column(Integer, primary_key=True, index=True)
    details = Column(Text, nullable=False)
    patient_id = Column(Integer, ForeignKey("users.id"))
    dietitian_id = Column(Integer, ForeignKey("users.id"))

    patient = relationship("User", back_populates="diet_plans", foreign_keys=[patient_id])

class FoodLog(Base):
    __tablename__ = "food_logs"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    meal_details = Column(Text, nullable=False)
    patient_id = Column(Integer, ForeignKey("users.id"))

    patient = relationship("User", back_populates="food_logs")
