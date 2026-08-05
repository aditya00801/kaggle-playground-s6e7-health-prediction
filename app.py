import streamlit as st
import pandas as pd
from catboost import CatBoostClassifier
from src.feature_engineering import create_features

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Student Health Risk Prediction",
    page_icon="🏥",
    layout="wide"
)

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    model = CatBoostClassifier()
    model.load_model("output/models/shrp_catboost_pro_v1_0.94985.cbm")
    return model

model = load_model()

st.title("🏥 Student Health Risk Prediction")
st.write("Predict a student's health condition using a trained CatBoost model.")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.header("Student Information")

sleep_duration = st.sidebar.slider("Sleep Duration (hours)", 0.0, 12.0, 7.0)
heart_rate = st.sidebar.slider("Heart Rate", 40, 180, 75)

bmi = st.sidebar.slider("BMI", 10.0, 45.0, 23.0)

calorie_expenditure = st.sidebar.number_input(
    "Calorie Expenditure",
    0,
    10000,
    2500
)

step_count = st.sidebar.number_input(
    "Step Count",
    0,
    50000,
    8000
)

exercise_duration = st.sidebar.number_input(
    "Exercise Duration (minutes)",
    0,
    300,
    45
)

water_intake = st.sidebar.slider(
    "Water Intake (Liters)",
    0.0,
    10.0,
    2.5
)

diet_type = st.sidebar.selectbox(
    "Diet Type",
    ["balanced", "high-protein", "vegetarian", "junk"]
)

stress_level = st.sidebar.selectbox(
    "Stress Level",
    ["low", "medium", "high"]
)

sleep_quality = st.sidebar.selectbox(
    "Sleep Quality",
    ["poor", "average", "good"]
)

physical_activity_level = st.sidebar.selectbox(
    "Physical Activity",
    ["low", "medium", "high"]
)

smoking_alcohol = st.sidebar.selectbox(
    "Smoking / Alcohol",
    ["none", "smoking", "alcohol", "both"]
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Health Risk"):

    data = pd.DataFrame([{
        "id": 0,
        "sleep_duration": sleep_duration,
        "heart_rate": heart_rate,
        "bmi": bmi,
        "calorie_expenditure": calorie_expenditure,
        "step_count": step_count,
        "exercise_duration": exercise_duration,
        "water_intake": water_intake,
        "diet_type": diet_type,
        "stress_level": stress_level,
        "sleep_quality": sleep_quality,
        "physical_activity_level": physical_activity_level,
        "smoking_alcohol": smoking_alcohol,
        "gender": gender
    }])

    # Apply feature engineering
    data = create_features(data)

    X = data.drop(columns=["id"])

    prediction = model.predict(X)[0]

    st.success(f"Predicted Health Condition: **{prediction}**")

    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(X)[0]

        prob_df = pd.DataFrame({
            "Health Condition": model.classes_,
            "Probability": probs
        })

        st.subheader("Prediction Probabilities")
        st.dataframe(prob_df)

        st.bar_chart(
            prob_df.set_index("Health Condition")
        )