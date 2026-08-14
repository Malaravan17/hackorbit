from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.database import get_db

from schemas.student_schema import (
    StudentResponse,
    DropoutPredictionResponse,
)

from services.student_service import (
    get_student_by_id
)

from services.prediction_service import (
    predict_dropout
)


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# ============================================================
# GET STUDENT
# ============================================================

@router.get(
    "/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: str,
    db: Session = Depends(get_db)
):

    student = get_student_by_id(
        db,
        student_id
    )

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# ============================================================
# DROPOUT PREDICTION
# ============================================================

@router.get(
    "/{student_id}/dropout-prediction",
    response_model=DropoutPredictionResponse
)
def dropout_prediction(
    student_id: str,
    db: Session = Depends(get_db)
):

    # --------------------------------------------------------
    # 1. Get student from PostgreSQL
    # --------------------------------------------------------

    student = get_student_by_id(
        db,
        student_id
    )

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # --------------------------------------------------------
    # 2. Send student to XGBoost
    # --------------------------------------------------------

    result = predict_dropout(
        student
    )

    # --------------------------------------------------------
    # 3. Return prediction
    # --------------------------------------------------------

    return result