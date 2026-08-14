from sqlalchemy.orm import Session

from database.models import Student


def get_student_by_id(
    db: Session,
    student_id: str
):

    student = (
        db.query(Student)
        .filter(
            Student.student_id == student_id
        )
        .first()
    )

    return student