"""
Streamlit app for the Capstone project.

Loads model.pkl (produced by train_model.py) and serves an interactive
prediction form. Run with: streamlit run app.py
"""

import joblib
import pandas as pd
import streamlit as st

from src.features import add_derived_features

st.set_page_config(page_title="House Price Estimator", page_icon="🏠")

st.title("🏠 House Price Estimator")
st.write(
    "A demo Capstone deployment. Replace this form and the model behind it "
    "with your own project's inputs and trained model."
)


@st.cache_resource
def load_model():
    bundle = joblib.load("model.pkl")
    return bundle["model"], bundle["scaler"], bundle["feature_columns"]


model, scaler, feature_columns = load_model()

st.subheader("Enter property details")
sqft = st.number_input("Square footage", min_value=200, max_value=10000, value=1500)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
neighborhood = st.selectbox("Neighborhood", ["Downtown", "Suburb", "Rural"])

if st.button("Estimate price"):
    # Build a single-row DataFrame matching the training pipeline exactly
    input_df = pd.DataFrame([{
        "sqft": sqft,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "neighborhood": neighborhood,
    }])

    input_df = add_derived_features(input_df)

    numeric_cols = ["sqft", "bedrooms", "bathrooms", "rooms_total", "sqft_per_bedroom"]
    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

    input_df = pd.get_dummies(input_df, columns=["neighborhood"], drop_first=True)

    # Add any dummy columns the training set had that this single row doesn't
    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[feature_columns]

    prediction = model.predict(input_df)[0]
    st.success(f"Estimated price: **${prediction:,.0f}**")

st.divider()
st.caption(
    "This is a starter template. Swap the training data, features, and form "
    "fields in train_model.py and app.py for your own Capstone project."
)
