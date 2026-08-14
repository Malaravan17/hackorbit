from pydantic import BaseModel


class StudentResponse(BaseModel):

    student_id: str
    name: str
    department: str
    year_of_study: int

    attendance_percentage: float
    cgpa: float
    entrance_exam_score: float

    activity_points: int
    reward_points: int

    arrear_count: int
    discipline_count: int

    fee_due_days: int
    lms_login_count: int

    hostel_status: str
    family_income_category: str

    extracurricular_participation: str
    attendance_trend: str
    backlog_trend: str

    dropout: int

    class Config:
        from_attributes = True


class ShapExplanation(BaseModel):

    feature: str
    impact: float
    direction: str


class DropoutPredictionResponse(BaseModel):

    student_id: str
    student_name: str

    dropout_prediction: int

    dropout_probability: float
    dropout_percentage: float

    threshold_percentage: float

    risk_level: str

    explanation: list[ShapExplanation]

    intervention: str | None