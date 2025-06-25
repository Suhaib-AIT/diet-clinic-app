from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from .. import schemas, auth, models
from ..database import get_session

router = APIRouter(prefix="/food-logs", tags=["food_logs"])


def add_log(session: Session, data: schemas.FoodLogCreate) -> models.FoodLog:
    log = models.FoodLog.from_orm(data)
    session.add(log)
    session.commit()
    session.refresh(log)
    return log


@router.post("/", response_model=schemas.FoodLogRead)
def create_food_log(
    log: schemas.FoodLogCreate,
    current_user: schemas.UserRead = Depends(auth.get_current_user),
    session: Session = Depends(get_session),
):
    return add_log(session, log)
