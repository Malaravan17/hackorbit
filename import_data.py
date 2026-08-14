import pandas as pd

from database.database import SessionLocal
from database.models import Student


CSV_PATH = "data/dropout_prediction_dataset.csv"


def import_students():

    df = pd.read_csv(
        CSV_PATH
    )

    db = SessionLocal()

    try:

        for _, row in df.iterrows():

            student = Student(
                student_id=row["StudentID"],
                name=row["Name"],
                department=row["Department"],
                year_of_study=row["YearOfStudy"],
                attendance_percentage=row["AttendancePercentage"],
                cgpa=row["CGPA"],
                entrance_exam_score=row["EntranceExamScore"],
                activity_points=row["ActivityPoints"],
                reward_points=row["RewardPoints"],
                arrear_count=row["ArrearCount"],
                discipline_count=row["DisciplineCount"],
                fee_due_days=row["FeeDueDays"],
                lms_login_count=row["LMSLoginCount"],
                hostel_status=row["HostelStatus"],
                family_income_category=row["FamilyIncomeCategory"],
                extracurricular_participation=row[
                    "ExtracurricularParticipation"
                ],
                attendance_trend=row["AttendanceTrend"],
                backlog_trend=row["BacklogTrend"],
                dropout=row["Dropout"],
            )

            db.add(student)

        db.commit()

        print(
            f"{len(df)} students imported successfully."
        )

    except Exception as e:

        db.rollback()

        print(
            "Error:",
            e
        )

    finally:

        db.close()


if __name__ == "__main__":
    import_students()