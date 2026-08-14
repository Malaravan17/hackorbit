<img width="1919" height="909" alt="Screenshot 2026-08-14 151038" src="https://github.com/user-attachments/assets/719a477f-93b5-4ade-943e-39695f08001e" /> DropoutGuard
Explainable Student Early-Warning System

DropoutGuard is an AI-powered student early-warning system designed to identify students who may be at risk of dropping out and explain the factors behind each prediction.

The system combines academic performance, attendance, engagement, and student activity data with an XGBoost machine-learning model. It then uses Gemini to convert the model's important factors into a clear, human-readable explanation so that faculty and mentors can understand the prediction and take appropriate early action.

Output:
1 )
<img width="1915" height="912" alt="Screenshot 2026-08-14 150947" src="https://github.com/user-attachments/assets/4c4ba1ed-0cd7-41eb-a7d7-29fca2969f26" />

2 ) 
<img width="1919" height="914" alt="Screenshot 2026-08-14 151626" src="https://github.com/user-attachments/assets/430735a7-22c9-43c6-a9fc-63451823ec1b" />

3 )
<img width="1919" height="909" alt="Screenshot 2026-08-14 151038" src="https://github.com/user-attachments/assets/5a341be7-bc67-43df-93f5-e28ec3dc3627" />

4 )
<img width="1919" height="905" alt="Screenshot 2026-08-14 151059" src="https://github.com/user-attachments/assets/06728ad7-5d50-477a-977e-d3b7d644e8f8" />

🚀 Key Features
Student Search – Retrieve a student's academic and engagement information using their roll number.
Dropout Risk Prediction – Predict the probability that a student may be at risk of dropping out.
XGBoost Model – Uses XGBoost for the core risk-prediction model.
Explainable AI – Displays the strongest factors influencing the model's prediction.
Risk and Protective Factors – Clearly separates factors that increase risk from factors that reduce risk.
AI-Generated Explanation – Gemini translates model results into an easy-to-understand explanation.
Recommended Actions – Provides practical intervention suggestions for faculty and mentors.
Student Dashboard – Presents attendance, CGPA, arrears, discipline, activity points, reward points, LMS logins, and fee-related information in a simple interface.
🎯 Problem Statement

Student dropout is often preceded by warning signs such as poor attendance, declining academic engagement, low academic performance, and changes in student activity.

Traditional approaches may identify these issues only after a student has already experienced significant academic difficulties. DropoutGuard aims to provide an early-warning mechanism by analyzing multiple student-related indicators and highlighting students who may require timely support.

The goal is not simply to predict risk, but to answer an important question:

Why is this student at risk, and what can be done about it?

🧠 How the System Works

The application follows an explainable AI workflow:

Student Roll Number
        ↓
Retrieve Student Data
        ↓
Academic & Engagement Features
        ↓
XGBoost Risk Prediction
        ↓
Identify Important Risk Factors
        ↓
Gemini AI Explanation
        ↓
Recommended Intervention Actions

This approach combines machine-learning prediction with explainability and actionable recommendations.

📊 Student Data Used

The system considers multiple indicators, including:

Feature	Description
Attendance Percentage	Percentage of classes attended by the student
CGPA	Current cumulative grade point average
Arrears	Number of academic arrears/backlogs
Discipline	Discipline-related indicator
Activity Points	Student activity/engagement points
Reward Points	Recognition or reward points
LMS Logins	Learning Management System engagement
Fee Due Days	Number of days associated with pending fees
Entrance Exam Score	Student's entrance examination performance
Attendance Trend	Whether attendance is improving or declining
Backlog Trend	Whether academic backlogs are increasing or decreasing
🔍 Explainable Risk Analysis

After prediction, DropoutGuard presents the strongest factors influencing the XGBoost model.

For each factor, the system displays:

Feature name
Student value
Model impact
Whether the feature increases or reduces risk
Example Risk Factors
Attendance Percentage – strong contribution toward increased risk.
Activity Points – contribution toward increased risk.
Entrance Exam Score – contribution toward increased risk.
Attendance Trend – protective factor when the trend is not declining.
CGPA – protective factor when academic performance is relatively strong.

This allows users to understand the prediction instead of treating the model as a black box.
