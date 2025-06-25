from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    hashed_password: str
    role: str = "patient"

    appointments: List["Appointment"] = Relationship(back_populates="user")
    diet_plans: List["DietPlan"] = Relationship(back_populates="user")
    food_logs: List["FoodLog"] = Relationship(back_populates="user")


class Appointment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    dietitian_id: int = Field(foreign_key="user.id")
    datetime: datetime
    notes: str = ""

    user: Optional[User] = Relationship(back_populates="appointments")


class DietPlan(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    description: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional[User] = Relationship(back_populates="diet_plans")


class FoodLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    logged_at: datetime = Field(default_factory=datetime.utcnow)
    meal: str

    user: Optional[User] = Relationship(back_populates="food_logs")
