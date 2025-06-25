from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from .database import engine
from .routers import appointments, diet_plans, food_logs
from . import models, schemas, crud, auth
from .database import get_session
from fastapi.responses import JSONResponse

app = FastAPI(title="Diet Clinic API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(appointments.router)
app.include_router(diet_plans.router)
app.include_router(food_logs.router)

