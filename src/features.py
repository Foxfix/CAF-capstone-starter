"""
Feature engineering helpers for the Capstone project.

Replace or extend these with logic specific to your own dataset.
Every function here is deliberately small and does one thing, so you
can import just what you need into your notebook or app.py.
codeaiflow.cloud
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def handle_missing_values(df: pd.DataFrame, strategy: str = "median") -> pd.DataFrame:
    """Fill missing numeric values with the column median (or mean),
    and missing categorical values with the string 'missing'.

    This is a starting point, not a rule — decide per-column whether
    dropping, filling, or flagging is more appropriate for your data.
    """
    df = df.copy()
    numeric_cols = df.select_dtypes(include="number").columns
    categorical_cols = df.select_dtypes(exclude="number").columns

    for col in numeric_cols:
        if df[col].isna().any():
            fill_value = df[col].median() if strategy == "median" else df[col].mean()
            df[col] = df[col].fillna(fill_value)

    for col in categorical_cols:
        df[col] = df[col].fillna("missing")

    return df


def encode_categorical(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """One-hot encode the given categorical columns."""
    return pd.get_dummies(df, columns=columns, drop_first=True)


def scale_numeric(df: pd.DataFrame, columns: list[str]) -> tuple[pd.DataFrame, StandardScaler]:
    """Scale the given numeric columns to zero mean / unit variance.
    Returns both the transformed DataFrame and the fitted scaler —
    you'll need the scaler again at prediction time (see app.py).
    """
    df = df.copy()
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df, scaler


def add_derived_features(df: pd.DataFrame) -> pd.DataFrame:
    """Example derived features for a housing-price-style dataset.
    Replace this with feature logic specific to your own project —
    this function exists to show the *pattern*, not to be reused as-is.
    """
    df = df.copy()
    if "bedrooms" in df.columns and "bathrooms" in df.columns:
        df["rooms_total"] = df["bedrooms"] + df["bathrooms"]
    if "sqft" in df.columns and "bedrooms" in df.columns:
        df["sqft_per_bedroom"] = df["sqft"] / df["bedrooms"].replace(0, 1)
    return df


def check_target_leakage(df: pd.DataFrame, target_col: str, threshold: float = 0.98) -> list[str]:
    """Flag any feature that correlates with the target above `threshold` —
    a common sign that the feature is leaking information that wouldn't
    actually be available at prediction time.
    """
    numeric_df = df.select_dtypes(include="number")
    if target_col not in numeric_df.columns:
        return []
    correlations = numeric_df.corr()[target_col].drop(target_col)
    suspicious = correlations[correlations.abs() > threshold].index.tolist()
    return suspicious
