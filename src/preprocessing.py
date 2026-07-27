import pandas as pd
import numpy as np


def get_feature_types(df):
    numerical = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical = df.select_dtypes(include=["object", "category"]).columns.tolist()
    return numerical, categorical


def fill_categorical_missing(df):
    df = df.copy()

    cat_cols = df.select_dtypes(include=["object", "category"]).columns

    for col in cat_cols:
        df[col] = df[col].fillna("Unknown").astype(str)

    return df


def fill_numeric_missing(df):
    df = df.copy()

    num_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    return df


def remove_id(df):
    df = df.copy()

    if "id" in df.columns:
        df = df.drop(columns=["id"])

    return df


def preprocess(df):
    df = fill_categorical_missing(df)
    df = fill_numeric_missing(df)
    df = remove_id(df)

    return df