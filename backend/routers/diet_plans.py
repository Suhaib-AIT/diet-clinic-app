from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from .. import crud, schemas, auth, models
from ..database import get_session

router = APIRouter(prefix="/diet-plans", tags=["diet_plans"])


def create_plan(session: Session, data: schemas.DietPlanCreate) -> models.DietPlan:
    plan = models.DietPlan.from_orm(data)
    session.add(plan)
    session.commit()
    session.refresh(plan)
    return plan


@router.post("/", response_model=schemas.DietPlanRead)
def add_diet_plan(
    plan: schemas.DietPlanCreate,
    current_user: schemas.UserRead = Depends(auth.get_current_user),
    session: Session = Depends(get_session),
):
    return create_plan(session, plan)


@router.get("/{plan_id}", response_model=schemas.DietPlanRead)
def get_plan(plan_id: int, session: Session = Depends(get_session)):
    return session.get(models.DietPlan, plan_id)
