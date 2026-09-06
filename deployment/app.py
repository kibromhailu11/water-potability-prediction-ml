import streamlit as st
import pandas as pd
import joblib

# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="Water Potability Prediction",
    page_icon="💧",
    layout="centered"
)

# ============================================
# Load Model, Imputer, and Features
# ============================================

model = joblib.load("deployment/water_potability_model.pkl")
imputer = joblib.load("deployment/water_potability_imputer.pkl")
features = joblib.load("deployment/water_potability_features.pkl")

# ============================================
# Page Title
# ============================================

st.title("💧 Water Potability Prediction")

st.write(
    "Enter the water-quality measurements below "
    "to predict whether the water is potable or not potable."
)

# ============================================
# User Input
# ============================================

ph = st.number_input(
    "pH",
    min_value=0.0,
    max_value=14.0,
    value=7.0,
    step=0.01
)

hardness = st.number_input(
    "Hardness",
    min_value=47.432,
    max_value=323.124,
    value=200.0,
    step=0.001
)

solids = st.number_input(
    "Solids",
    min_value=320.942611,
    max_value=61227.196008,
    value=20000.0,
    step=0.001
)

chloramines = st.number_input(
    "Chloramines",
    min_value=0.352,
    max_value=13.127,
    value=7.0,
    step=0.001
)

sulfate = st.number_input(
    "Sulfate",
    min_value=129.0,
    max_value=481.030642,
    value=330.0,
    step=0.001
)

conductivity = st.number_input(
    "Conductivity",
    min_value=181.483754,
    max_value=753.342620,
    value=400.0,
    step=0.001
)

organic_carbon = st.number_input(
    "Organic Carbon",
    min_value=2.2,
    max_value=28.3,
    value=14.0,
    step=0.001
)

trihalomethanes = st.number_input(
    "Trihalomethanes",
    min_value=0.738,
    max_value=124.0,
    value=66.0,
    step=0.001
)

turbidity = st.number_input(
    "Turbidity",
    min_value=1.45,
    max_value=6.739,
    value=4.0,
    step=0.001
)

# ============================================
# Create Input DataFrame
# ============================================

new_water_sample = pd.DataFrame([{
    "ph": ph,
    "Hardness": hardness,
    "Solids": solids,
    "Chloramines": chloramines,
    "Sulfate": sulfate,
    "Conductivity": conductivity,
    "Organic_carbon": organic_carbon,
    "Trihalomethanes": trihalomethanes,
    "Turbidity": turbidity
}])

# ============================================
# Make Sure Feature Order is Correct
# ============================================

new_water_sample = new_water_sample[features]

# ============================================
# Handle Missing Values
# ============================================

new_water_sample_imputed = imputer.transform(new_water_sample)

# ============================================
# Prediction
# ============================================

if st.button("Predict Water Potability"):

    prediction = model.predict(new_water_sample_imputed)[0]

    probability = model.predict_proba(
        new_water_sample_imputed
    )[0]

    # ========================================
    # Display Result
    # ========================================

    st.subheader("Prediction Result")

    if prediction == 1:

        st.success(
            "The water is predicted to be POTABLE."
        )

        st.write(
            f"Probability of Potable Water: "
            f"{probability[1] * 100:.2f}%"
        )

    else:

        st.error(
            "The water is predicted to be NOT POTABLE."
        )

        st.write(
            f"Probability of Not Potable Water: "
            f"{probability[0] * 100:.2f}%"
        )

# ============================================
# Disclaimer
# ============================================

st.info(
    "This is a machine-learning prediction and "
    "should not replace laboratory water-quality testing."
)