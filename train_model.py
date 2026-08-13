"""
Train a baseline model for the Capstone starter and save it to model.pkl.

This script uses a synthetic housing dataset so the repo runs end-to-end
with no external download required. Swap `load_data()` for your own
dataset loader — everything after that stays the same shape.

Run with: python train_model.py
codeaiflow.cloud
"""

import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

from src.features import (
    handle_missing_values,
    encode_categorical,
    scale_numeric,
    add_derived_features,
    check_target_leakage,
)


def load_data(n_rows: int = 500, seed: int = 42) -> pd.DataFrame:
    """Synthetic housing dataset. Replace with pd.read_csv('data/your_file.csv')
    once you're working with your own real Capstone dataset."""
    rng = np.random.default_rng(seed)
    sqft = rng.integers(500, 4000, size=n_rows)
    bedrooms = rng.integers(1, 6, size=n_rows)
    bathrooms = rng.integers(1, 4, size=n_rows)
    neighborhood = rng.choice(["Downtown", "Suburb", "Rural"], size=n_rows)
    neighborhood_premium = pd.Series(neighborhood).map(
        {"Downtown": 1.3, "Suburb": 1.0, "Rural": 0.7}
    ).values

    price = (
        sqft * 150
        + bedrooms * 8000
        + bathrooms * 5000
    ) * neighborhood_premium + rng.normal(0, 15000, size=n_rows)

    df = pd.DataFrame({
        "sqft": sqft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "neighborhood": neighborhood,
        "price": price.round(0),
    })

    # Introduce a few missing values, like a real dataset would have
    missing_idx = rng.choice(df.index, size=10, replace=False)
    df.loc[missing_idx, "sqft"] = np.nan
    return df


def main():
    df = load_data()

    df = handle_missing_values(df)
    df = add_derived_features(df)

    leaky_cols = check_target_leakage(df, target_col="price")
    if leaky_cols:
        print(f"WARNING: possible target leakage in columns: {leaky_cols}")

    numeric_cols = ["sqft", "bedrooms", "bathrooms", "rooms_total", "sqft_per_bedroom"]
    df, scaler = scale_numeric(df, numeric_cols)
    df = encode_categorical(df, columns=["neighborhood"])

    X = df.drop(columns=["price"])
    y = df["price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    print(f"Test MAE: {mae:,.0f}")
    print(f"Test R^2: {r2:.3f}")

    joblib.dump(
        {"model": model, "scaler": scaler, "feature_columns": list(X.columns)},
        "model.pkl",
    )
    print("Saved model.pkl")


if __name__ == "__main__":
    main()
