import os
import random
import joblib
import numpy as np


def set_seed(seed=42):
    """
    Set random seed for reproducibility.
    """
    random.seed(seed)
    np.random.seed(seed)


def save_model(model, filepath):
    """
    Save trained model.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    joblib.dump(model, filepath)
    print(f"Model saved to: {filepath}")


def load_model(filepath):
    """
    Load saved model.
    """
    model = joblib.load(filepath)
    print(f"Model loaded from: {filepath}")
    return model


def save_submission(ids, predictions, filepath):
    """
    Save Kaggle submission file.
    """
    import pandas as pd

    submission = pd.DataFrame({
        "id": ids,
        "health_condition": predictions
    })

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    submission.to_csv(filepath, index=False)

    print(f"Submission saved to: {filepath}")

    return submission


def check_missing_values(df):
    """
    Display missing values in DataFrame.
    """
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if len(missing) == 0:
        print("No missing values found.")
    else:
        print(missing)


def get_feature_types(df):
    """
    Return numerical and categorical columns.
    """
    numerical = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical = df.select_dtypes(include=["object", "category"]).columns.tolist()

    return numerical, categorical