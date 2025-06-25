from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session
from .. import crud, schemas, auth
from ..database import get_session

router = APIRouter(prefix="/appointments", tags=["appointments"])


@router.get("/", response_model=List[schemas.AppointmentRead])
def read_appointments(session: Session = Depends(get_session)):
    return crud.list_appointments(session)


@router.post("/", response_model=schemas.AppointmentRead)
def create_appointment(
    appointment: schemas.AppointmentCreate,
    current_user: schemas.UserRead = Depends(auth.get_current_user),
    session: Session = Depends(get_session),
):
    return crud.create_appointment(session, appointment)
