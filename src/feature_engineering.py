import pandas as pd
import numpy as np


def create_features(df):
    df = df.copy()

    # Fill missing numeric values
    numeric_cols = [
        "exercise_duration",
        "step_count",
        "calorie_expenditure",
        "water_intake",
        "sleep_duration",
        "bmi",
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())

    # Activity Score
    df["activity_score"] = (
        df["exercise_duration"] *
        df["step_count"]
    )

    # Calories per Step
    df["calories_per_step"] = (
        df["calorie_expenditure"] /
        (df["step_count"] + 1)
    )

    # Water per Exercise Minute
    df["water_per_exercise"] = (
        df["water_intake"] /
        (df["exercise_duration"] + 1)
    )

    # Exercise / Sleep Ratio
    df["exercise_sleep_ratio"] = (
        df["exercise_duration"] /
        (df["sleep_duration"] + 1)
    )

    # BMI Category
    df["bmi_category"] = pd.cut(
        df["bmi"],
        bins=[-np.inf, 18.5, 25, 30, np.inf],
        labels=[
            "underweight",
            "normal",
            "overweight",
            "obese"
        ]
    )

    df["bmi_category"] = (
        df["bmi_category"]
        .astype(str)
        .replace("nan", "Unknown")
    )

    # Ensure all categorical columns are strings
    cat_cols = df.select_dtypes(include=["object", "category"]).columns

    for col in cat_cols:
        df[col] = df[col].fillna("Unknown").astype(str)

    return df