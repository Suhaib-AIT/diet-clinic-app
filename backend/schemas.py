from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    username: Optional[str] = None


class UserBase(SQLModel):
    username: str
    role: str = "patient"


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int


class AppointmentCreate(SQLModel):
    user_id: int
    dietitian_id: int
    datetime: datetime
    notes: str = ""


class AppointmentRead(AppointmentCreate):
    id: int


class DietPlanCreate(SQLModel):
    user_id: int
    description: str


class DietPlanRead(DietPlanCreate):
    id: int
    created_at: datetime


class FoodLogCreate(SQLModel):
    user_id: int
    meal: str


class FoodLogRead(FoodLogCreate):
    id: int
    logged_at: datetime
