import os
import joblib
import pandas as pd
import shap

from database.models import Student

from services.gemini_service import (
    generate_intervention
)


MODEL_PATH = "model/dropout_xgboost.pkl"

DROPOUT_THRESHOLD = 0.70




if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model not found at: {MODEL_PATH}"
    )


pipeline = joblib.load(
    MODEL_PATH
)


# ============================================================
# CREATE STUDENT DATAFRAME
# ============================================================

def create_student_dataframe(
    student: Student
):

    student_data = {
        "Department": student.department,
        "YearOfStudy": student.year_of_study,
        "AttendancePercentage": student.attendance_percentage,
        "CGPA": student.cgpa,
        "EntranceExamScore": student.entrance_exam_score,
        "ActivityPoints": student.activity_points,
        "RewardPoints": student.reward_points,
        "ArrearCount": student.arrear_count,
        "DisciplineCount": student.discipline_count,
        "FeeDueDays": student.fee_due_days,
        "LMSLoginCount": student.lms_login_count,
        "HostelStatus": student.hostel_status,
        "FamilyIncomeCategory": student.family_income_category,
        "ExtracurricularParticipation": (
            student.extracurricular_participation
        ),
        "AttendanceTrend": student.attendance_trend,
        "BacklogTrend": student.backlog_trend,
    }

    return pd.DataFrame(
        [student_data]
    )


# ============================================================
# SHAP EXPLANATION
# ============================================================

def get_shap_explanation(
    student_df
):

    preprocessor = pipeline.named_steps[
        "preprocessor"
    ]

    xgb_model = pipeline.named_steps[
        "model"
    ]

    transformed_data = preprocessor.transform(
        student_df
    )

    feature_names = (
        preprocessor
        .get_feature_names_out()
    )

    explainer = shap.TreeExplainer(
        xgb_model
    )

    shap_values = explainer.shap_values(
        transformed_data
    )

    if isinstance(shap_values, list):
        shap_values = shap_values[0]

    student_shap_values = shap_values[0]

    explanation = []

    for feature_name, shap_value in zip(
        feature_names,
        student_shap_values
    ):

        explanation.append(
            {
                "feature": feature_name,
                "impact": round(
                    float(shap_value),
                    4
                )
            }
        )

    explanation.sort(
        key=lambda x: abs(x["impact"]),
        reverse=True
    )

    explanation = explanation[:5]

    for item in explanation:

        if item["impact"] > 0:

            item["direction"] = (
                "increases_dropout_risk"
            )

        else:

            item["direction"] = (
                "reduces_dropout_risk"
            )

    return explanation


# ============================================================
# DROPOUT PREDICTION
# ============================================================

def predict_dropout(
    student: Student
):

    # --------------------------------------------------------
    # 1. Convert DB record to DataFrame
    # --------------------------------------------------------

    student_df = create_student_dataframe(
        student
    )


    # --------------------------------------------------------
    # 2. XGBoost prediction
    # --------------------------------------------------------

    probability = pipeline.predict_proba(
        student_df
    )[0][1]

    prediction = pipeline.predict(
        student_df
    )[0]


    # --------------------------------------------------------
    # 3. Check threshold
    # --------------------------------------------------------

    if probability >= DROPOUT_THRESHOLD:

        risk_level = "HIGH"

        # ----------------------------------------------------
        # 4. Generate SHAP explanation
        # ----------------------------------------------------

        explanation = get_shap_explanation(
            student_df
        )


        # ----------------------------------------------------
        # 5. Send high-risk student to Gemini
        # ----------------------------------------------------

        intervention = generate_intervention(
            student=student,
            dropout_probability=probability,
            shap_explanation=explanation
        )

    else:

        risk_level = "LOW"

        explanation = []

        intervention = None


    # --------------------------------------------------------
    # 6. Final result
    # --------------------------------------------------------

    return {

        "student_id": student.student_id,

        "student_name": student.name,

        "dropout_prediction": int(
            prediction
        ),

        "dropout_probability": round(
            float(probability),
            4
        ),

        "dropout_percentage": round(
            float(probability * 100),
            2
        ),

        "threshold_percentage": (
            DROPOUT_THRESHOLD * 100
        ),

        "risk_level": risk_level,

        "explanation": explanation,

        "intervention": intervention
    }