import pandas as pd
import numpy as np


def create_features(df):
    df = df.copy()

    # -------------------------------
    # Fill Missing Numeric Values
    # -------------------------------
    numeric_cols = [
        "exercise_duration",
        "step_count",
        "calorie_expenditure",
        "water_intake",
        "sleep_duration",
        "heart_rate",
        "bmi",
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())

    # -------------------------------
    # Fill Missing Categorical Values
    # -------------------------------
    cat_cols = [
        "diet_type",
        "stress_level",
        "sleep_quality",
        "physical_activity_level",
        "smoking_alcohol",
        "gender",
    ]

    for col in cat_cols:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown").astype(str)

    # =========================================================
    # Existing Features
    # =========================================================

    df["activity_score"] = (
        df["exercise_duration"] *
        df["step_count"]
    )

    df["calories_per_step"] = (
        df["calorie_expenditure"] /
        (df["step_count"] + 1)
    )

    df["water_per_exercise"] = (
        df["water_intake"] /
        (df["exercise_duration"] + 1)
    )

    df["exercise_sleep_ratio"] = (
        df["exercise_duration"] /
        (df["sleep_duration"] + 1)
    )

    # =========================================================
    # NEW NUMERIC FEATURES
    # =========================================================

    # Activity
    df["steps_per_minute"] = (
        df["step_count"] /
        (df["exercise_duration"] + 1)
    )

    df["calories_per_minute"] = (
        df["calorie_expenditure"] /
        (df["exercise_duration"] + 1)
    )

    df["activity_density"] = (
        df["step_count"] *
        df["exercise_duration"]
    )

    # Heart
    df["heart_activity"] = (
        df["heart_rate"] *
        df["exercise_duration"]
    )

    df["heart_steps"] = (
        df["heart_rate"] *
        df["step_count"]
    )

    # BMI
    df["bmi_sleep"] = (
        df["bmi"] *
        df["sleep_duration"]
    )

    df["bmi_water"] = (
        df["bmi"] *
        df["water_intake"]
    )

    # Hydration
    df["hydration_score"] = (
        df["water_intake"] /
        (df["calorie_expenditure"] + 1)
    )

    # Overall Health Index
    df["health_index"] = (
        df["sleep_duration"] +
        df["exercise_duration"] +
        df["water_intake"]
    )

    # =========================================================
    # BMI Categories
    # =========================================================

    df["bmi_category"] = pd.cut(
        df["bmi"],
        bins=[-np.inf, 18.5, 25, 30, np.inf],
        labels=[
            "underweight",
            "normal",
            "overweight",
            "obese"
        ]
    ).astype(str)

    df["bmi_risk"] = pd.cut(
        df["bmi"],
        bins=[-np.inf, 18.5, 25, 30, 35, np.inf],
        labels=[
            "under",
            "normal",
            "over",
            "obese",
            "severe_obese"
        ]
    ).astype(str)

    # =========================================================
    # NEW CATEGORICAL INTERACTION FEATURES
    # =========================================================

    df["stress_sleep"] = (
        df["stress_level"] + "_" +
        df["sleep_quality"]
    )

    df["activity_diet"] = (
        df["physical_activity_level"] + "_" +
        df["diet_type"]
    )

    df["gender_activity"] = (
        df["gender"] + "_" +
        df["physical_activity_level"]
    )

    df["smoking_stress"] = (
        df["smoking_alcohol"] + "_" +
        df["stress_level"]
    )

    df["diet_smoking"] = (
        df["diet_type"] + "_" +
        df["smoking_alcohol"]
    )

    return df