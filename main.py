from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.database import Base, engine
from database import models
from routers.student import router as student_router


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Student Dropout Prediction API"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    student_router
)


@app.get("/")
def root():
    return {
        "message": "Student Dropout Prediction API"
    }