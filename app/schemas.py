from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr

class Role(str, Enum):
    admin = "admin"
    dietitian = "dietitian"
    patient = "patient"

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    role: Role = Role.patient

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class AppointmentBase(BaseModel):
    date: datetime
    description: Optional[str] = None

class AppointmentCreate(AppointmentBase):
    patient_id: int
    dietitian_id: int

class Appointment(AppointmentBase):
    id: int
    patient_id: int
    dietitian_id: int

    class Config:
        orm_mode = True

class DietPlanBase(BaseModel):
    details: str

class DietPlanCreate(DietPlanBase):
    patient_id: int
    dietitian_id: int

class DietPlan(DietPlanBase):
    id: int
    patient_id: int
    dietitian_id: int

    class Config:
        orm_mode = True

class FoodLogBase(BaseModel):
    date: datetime
    meal_details: str

class FoodLogCreate(FoodLogBase):
    patient_id: int

class FoodLog(FoodLogBase):
    id: int
    patient_id: int

    class Config:
        orm_mode = True
