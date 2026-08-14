from sqlalchemy import Column, Integer, String, Float

from database.database import Base


class Student(Base):

    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    department = Column(
        String
    )

    year_of_study = Column(
        Integer
    )

    attendance_percentage = Column(
        Float
    )

    cgpa = Column(
        Float
    )

    entrance_exam_score = Column(
        Float
    )

    activity_points = Column(
        Integer
    )

    reward_points = Column(
        Integer
    )

    arrear_count = Column(
        Integer
    )

    discipline_count = Column(
        Integer
    )

    fee_due_days = Column(
        Integer
    )

    lms_login_count = Column(
        Integer
    )

    hostel_status = Column(
        String
    )

    family_income_category = Column(
        String
    )

    extracurricular_participation = Column(
        String
    )

    attendance_trend = Column(
        String
    )

    backlog_trend = Column(
        String
    )

    dropout = Column(
        Integer
    )