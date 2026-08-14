import json

from google import genai
from settings.config import settings


# ============================================================
# GEMINI CONFIGURATION
# ============================================================

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


MODEL_NAME = "gemini-3.5-flash-lite"


# ============================================================
# GENERATE EXPLANATION
# ============================================================

def generate_intervention(
    student,
    dropout_probability,
    shap_explanation
):

    student_information = {
        "student_id": student.student_id,
        "name": student.name,
        "department": student.department,
        "year_of_study": student.year_of_study,

        "attendance_percentage":
            student.attendance_percentage,

        "cgpa":
            student.cgpa,

        "activity_points":
            student.activity_points,

        "reward_points":
            student.reward_points,

        "arrear_count":
            student.arrear_count,

        "discipline_count":
            student.discipline_count,

        "fee_due_days":
            student.fee_due_days,

        "lms_login_count":
            student.lms_login_count,

        "attendance_trend":
            student.attendance_trend,

        "backlog_trend":
            student.backlog_trend,
    }


    prompt = f"""
You are an explainable AI assistant for a college
student early-warning system.

An XGBoost model has predicted a high dropout risk
for a student.

Your job is NOT to make a new prediction.

Your job is to clearly explain:

"WHY did the model give this student such a high
dropout probability?"

The explanation MUST be based on the SHAP feature
contributions provided below.

IMPORTANT RULES:

1. Do not invent reasons that are not present in
   the student data or SHAP explanation.

2. Do not say that a factor definitely CAUSED the
   student to drop out.

3. Explain that these factors CONTRIBUTED TO THE
   MODEL'S PREDICTION.

4. Positive SHAP impact means the feature pushed
   the prediction toward higher dropout risk.

5. Negative SHAP impact means the feature pushed
   the prediction toward lower dropout risk.

6. Focus primarily on the strongest SHAP contributors.

7. Explain the student's actual values when possible.

8. Do not simply repeat feature names.
   Explain them in natural language that a faculty
   member can understand.

9. Do not give generic explanations such as
   "the student may have academic problems" unless
   supported by the provided data.

10. The dropout probability is a MODEL ESTIMATE,
    not a certainty.


STUDENT INFORMATION:

{json.dumps(
    student_information,
    indent=2
)}


XGBOOST DROPOUT PROBABILITY:

{dropout_probability * 100:.2f}%


SHAP FEATURE CONTRIBUTIONS:

{json.dumps(
    shap_explanation,
    indent=2
)}


Provide the response in exactly these sections:


WHY THIS STUDENT IS HIGH RISK:

Explain clearly why the model produced this
high dropout probability.

Mention the strongest contributing factors and
their actual values.


MAIN RISK FACTORS:

- Explain the first major contributing factor.
- Explain the second major contributing factor.
- Explain the third major contributing factor.


PROTECTIVE FACTORS:

Mention important factors that pushed the model
away from dropout risk, if any.


RECOMMENDED ACTIONS:

Give 3-5 practical actions that faculty or mentors
could take based specifically on the identified
risk factors.


IMPORTANT:

Do not claim that the student will definitely
drop out.

Use wording such as:

"The model predicts..."

"The model considers..."

"This factor contributed to the prediction..."

instead of:

"This factor will cause dropout."
"""


    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )


    return response.text